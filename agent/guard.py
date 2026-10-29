"""Guardrails for the weekly analyst agent.

Two layers, both deterministic and tested (agent/tests/test_guard.py):
  1. Tool-call checks, used as PreToolUse hooks: the agent may only write inside the drafts folder,
     may never read or write private files, and may never fetch a blocked URL.
  2. A text validator run on the finished draft before it is committed: the repo publishes
     percentages only, so any £ amount, email address, National Insurance-style number or
     reference to private files fails the run.

Run as a script to validate a file:  python agent/guard.py --validate weekly-reviews/drafts/2026-11-04.md
"""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = tomllib.loads((ROOT / "agent" / "config.toml").read_text())
DRAFT_DIR = (ROOT / CONFIG["review"]["draft_dir"]).resolve()
BLOCKED_URLS = [f.lower() for f in CONFIG["research"]["blocked_url_fragments"]]

# ---------- 1. tool-call checks ----------

def _resolve(path: str) -> Path:
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    return p.resolve()


def check_write(path: str) -> str | None:
    """Return a reason to deny, or None if the write is allowed."""
    p = _resolve(path)
    try:
        p.relative_to(DRAFT_DIR)
    except ValueError:
        return f"writes are only allowed inside {DRAFT_DIR.relative_to(ROOT)}/"
    if p.suffix != ".md":
        return "drafts must be Markdown (.md) files"
    return None


def check_read(path: str) -> str | None:
    p = _resolve(path)
    parts = {part.lower() for part in p.parts}
    if "private" in parts or ".env" in parts or p.name.startswith(".env"):
        return "private files are off-limits to the agent"
    return None


def check_url(url: str) -> str | None:
    u = url.lower()
    for frag in BLOCKED_URLS:
        if frag in u:
            return f"{frag} is on the blocked list (rate limits / terms)"
    return None


def check_tool(tool_name: str, tool_input: dict) -> str | None:
    if tool_name in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        return check_write(tool_input.get("file_path") or tool_input.get("notebook_path") or "")
    if tool_name == "Read":
        return check_read(tool_input.get("file_path", ""))
    if tool_name in ("Glob", "Grep"):
        return check_read(tool_input.get("path") or str(ROOT))
    if tool_name == "WebFetch":
        return check_url(tool_input.get("url", ""))
    if tool_name == "Bash":
        return "the agent has no shell; the numbers come from agent/compute.py"
    return None


async def pre_tool_use_hook(input_data, tool_use_id, context):
    """Agent SDK PreToolUse hook: deny any call that breaks a rule above."""
    reason = check_tool(input_data.get("tool_name", ""), input_data.get("tool_input", {}) or {})
    if reason:
        return {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                       "permissionDecision": "deny",
                                       "permissionDecisionReason": reason}}
    return {}

# ---------- 2. text validator ----------

# £ followed by a number is an amount, except on lines quoting a London ETF's unit price.
_GBP_AMOUNT = re.compile(r"£\s?\d")
_PRICE_LINE_OK = re.compile(r"\b(VUKG|XLVP)\b")
_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
_NINO = re.compile(r"\b[A-Z]{2}\s?\d{2}\s?\d{2}\s?\d{2}\s?[A-D]\b")
_SORT_CODE = re.compile(r"\b\d{2}-\d{2}-\d{2}\b")
_PRIVATE = re.compile(r"\bprivate/")


def validate_text(text: str) -> list[str]:
    problems = []
    for n, line in enumerate(text.splitlines(), 1):
        if _GBP_AMOUNT.search(line) and not _PRICE_LINE_OK.search(line):
            problems.append(f"line {n}: £ amount (the repo publishes percentages only)")
        if _EMAIL.search(line):
            problems.append(f"line {n}: email address")
        if _NINO.search(line):
            problems.append(f"line {n}: looks like a National Insurance number")
        if _SORT_CODE.search(line):
            problems.append(f"line {n}: looks like a sort code")
        if _PRIVATE.search(line):
            problems.append(f"line {n}: refers to private files")
    return problems


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "--validate":
        sys.exit("usage: python agent/guard.py --validate <file.md>")
    found = validate_text(Path(sys.argv[2]).read_text())
    for p in found:
        print("BLOCKED:", p)
    sys.exit(1 if found else 0)
