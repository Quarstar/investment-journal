"""Step 3 of the weekly run: the analyst agent (Claude Agent SDK) researches the week and drafts the review.

It reads the repo (checklist, last review, plans, predictions) and agent/out/metrics.json, researches each
name on the web, and writes ONE file: weekly-reviews/drafts/<review-date>.md. It cannot run commands,
cannot write anywhere else, cannot see private files, cannot place trades (it has no broker access at all),
and stops at the budget in agent/config.toml. A person reads the draft and decides; the agent decides nothing.

Usage:
  ANTHROPIC_API_KEY=... python agent/run_agent.py            # real run
  python agent/run_agent.py --dry-run                        # no API call: writes a skeleton draft from metrics.json
"""
from __future__ import annotations

import asyncio
import datetime as dt
import json
import os
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "agent"))
from guard import pre_tool_use_hook, validate_text  # noqa: E402

CONFIG = tomllib.loads((ROOT / "agent" / "config.toml").read_text())
OUT = ROOT / "agent" / "out"


def review_date(price_date: str) -> str:
    """The Wednesday after the price date."""
    d = dt.date.fromisoformat(price_date)
    return (d + dt.timedelta(days=(2 - d.weekday()) % 7 or 7)).isoformat()


def latest_review() -> str | None:
    reviews = sorted(p.name for p in (ROOT / "weekly-reviews").glob("20??-??-??.md"))
    return f"weekly-reviews/{reviews[-1]}" if reviews else None


SYSTEM_PROMPT = """You are the research analyst for a personal, public investment journal (a UK student's ISA
portfolio, documented on GitHub). You draft the Wednesday review; the owner reads it and makes every decision.

How you work:
- Verify, don't estimate. Every price, figure and date in your draft comes from agent/out/metrics.json, a file
  in the repo, or a web source you cite with a link. If you can't verify something, write "not verified" and
  move on. Never fill a gap with a guess, and never present an estimate as a fact.
- Write like a sell-side analyst: support and capitulation levels, valuation at each level, what changed and
  why it matters. Plain British English, short sentences, numbers with units.
- Facts first, then the read. Keep your opinion in clearly labelled "Read:" lines.
- You propose; you never decide. Anything that would change an order or a target goes under
  "Decisions for the owner" as a question with the trade-off stated, never as an instruction.

Hard rules (a validator rejects the draft if any is broken):
- The journal publishes percentages and prices only: no £ amounts, balances, share counts or account values,
  and no personal data of any kind. Weights are filled in by the owner from private records; leave that
  section as a placeholder.
- You may write only to the single draft file named in the task.
- Never fetch api.stockanalysis.com or any URL the guard blocks; if a fetch is refused, use another source.
- This is a personal record, not financial advice; never address readers with recommendations."""


def task_prompt(metrics: dict, draft_path: str) -> str:
    names = ", ".join(CONFIG["research"]["names"])
    return f"""Draft this week's review.

Price date (the previous US close): {metrics.get('price_date')}. Write the draft to: {draft_path}

Read first, in this order:
1. weekly-reviews/_checklist.md (the structure to follow, section by section)
2. {latest_review()} (last week's review: carry forward open items, gates, predictions and decisions)
3. agent/out/metrics.json (computed numbers: zone status and flags, ranking table, drawdown, rotation, VST/CEG,
   week changes) and agent/out/prices.json (closes and their verification status)
4. plans/target-portfolio.md, plans/watch-items.md, predictions.md, trades/limit-orders-2026-10-14.md (skim)

Research, for each of: {names}
- company-specific news since the last review, analyst rating or target changes (firm, old -> new),
  any share issuance or buyback change, and the next results date (company-confirmed or estimate: say which);
- the reason for any move over 5% in a day.
If agent/out/prices.json marks closes as "single source", spot-check the closes of the holdings (NBIS, VST, NVDA, CEG, TSM, NEE, GOOGL) against one independent quote page each and record match / mismatch in a short table; never change a number in the data files.
Then the sector signals in section 5b of the checklist (hyperscaler capex, GPU rental prices, AI funding,
AI-lab revenue) and any results gate that falls due before next Wednesday: what the bar is.
Use two searches per name at most unless something big happened; budget is limited.

Write the draft in the checklist's order, using the same section numbers as last week's review. Include:
- a one-paragraph summary of the week;
- a holdings table (close, week change, forward P/E where metrics has it, next results, the week's news);
- "3. Weights and limits: to be filled from private records" (placeholder only);
- the capture-zone flags from metrics.json exactly as computed, with your read of what each means for that
  name's role (planned buy, exit, carry, sandbox, watch);
- gates, signals, rotation reading, predictions status (score any that are past their deadline using the
  rules written in predictions.md), and open items carried from last week;
- "Decisions for the owner": numbered questions, each with the trade-off;
- a Sources list with links.
Keep it under ~2,500 words. When the file is written, reply with one line: the file path and the three most
important things in it."""


def dry_run(metrics: dict, draft: Path) -> None:
    lines = [f"# Draft weekly review · {draft.stem} (dry run: no research)", "",
             f"Prices: the {metrics.get('price_date')} close. Generated by agent/run_agent.py --dry-run.", "",
             "> Personal record, not financial advice.", "", "## Capture-zone status", "",
             "| Name | Last | Where | Flags |", "|---|---|---|---|"]
    for t, z in metrics.get("zones", {}).items():
        lines.append(f"| {t} | {z['last']} | {z['status']} | {'; '.join(z['flags']) or '–'} |")
    if metrics.get("drawdown"):
        d = metrics["drawdown"]
        lines += ["", f"QQQ {d['qqq']} is {d['from_high_pct']}% from the {d['high']} high."]
    if metrics.get("rotation") and "rsp_minus_qqq" in metrics["rotation"]:
        r = metrics["rotation"]
        lines += [f"Rotation (4 weeks): RSP − QQQ {r['rsp_minus_qqq']} pts, XLP − XLK {r['xlp_minus_xlk']}, "
                  f"XLY − XLK {r['xly_minus_xlk']}; passes this week: {r['this_week_passes']}."]
    lines += ["", "## 3. Weights and limits: to be filled from private records", ""]
    draft.write_text("\n".join(lines) + "\n")


async def real_run(metrics: dict, draft: Path) -> dict:
    from claude_agent_sdk import ClaudeAgentOptions, HookMatcher, ResultMessage, query

    options = ClaudeAgentOptions(
        system_prompt=SYSTEM_PROMPT,
        cwd=str(ROOT),
        model=CONFIG["review"]["model"],
        tools=["Read", "Glob", "Grep", "Write", "Edit", "WebSearch", "WebFetch"],
        allowed_tools=["Read", "Glob", "Grep", "Write", "Edit", "WebSearch", "WebFetch"],
        disallowed_tools=["Bash"],
        permission_mode="dontAsk",
        setting_sources=[],
        max_turns=CONFIG["review"]["max_turns"],
        max_budget_usd=CONFIG["review"]["max_budget_usd"],
        hooks={"PreToolUse": [HookMatcher(matcher=None, hooks=[pre_tool_use_hook])]},
    )
    result = {}
    async for msg in query(prompt=task_prompt(metrics, str(draft.relative_to(ROOT))), options=options):
        if isinstance(msg, ResultMessage):
            result = {"subtype": msg.subtype, "is_error": msg.is_error, "turns": msg.num_turns,
                      "cost_usd": msg.total_cost_usd, "summary": (msg.result or "")[:600],
                      "denied": len(msg.permission_denials or [])}
    return result


def main() -> int:
    metrics = json.loads((OUT / "metrics.json").read_text())
    if not metrics.get("price_date"):
        print("no price date in metrics.json; run agent/prices.py and agent/compute.py first")
        return 1
    draft_dir = ROOT / CONFIG["review"]["draft_dir"]
    draft_dir.mkdir(parents=True, exist_ok=True)
    draft = draft_dir / f"{review_date(metrics['price_date'])}.md"

    if "--dry-run" in sys.argv:
        dry_run(metrics, draft)
        result = {"subtype": "dry_run", "cost_usd": 0}
    else:
        if not os.environ.get("ANTHROPIC_API_KEY"):
            print("ANTHROPIC_API_KEY is not set")
            return 1
        result = asyncio.run(real_run(metrics, draft))

    if not draft.exists():
        print(f"agent finished without writing {draft.relative_to(ROOT)}: {result}")
        return 1
    problems = validate_text(draft.read_text())
    result.update({"draft": str(draft.relative_to(ROOT)), "validator": problems or "clean"})
    (OUT / "run.json").write_text(json.dumps(result, indent=1))
    # Only the summary is printed: Actions logs on a public repo are public.
    print(json.dumps({k: result.get(k) for k in ("subtype", "turns", "cost_usd", "draft", "validator", "denied")}))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
