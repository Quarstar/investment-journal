# Weekly analyst agent

An AI agent, built on the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview), that prepares my Wednesday portfolio review. Every Wednesday morning it:

1. **fetches Tuesday's closing prices** for every holding and watch-list name (Yahoo Finance), cross-checks each close against Twelve Data when its free key is set (otherwise the agent spot-checks the holdings on the web), and appends them to the price files ([`prices.py`](prices.py));
2. **computes every number that can be computed:** where each stock sits on its capture-zone map and which zones broke on the Friday close, the risk-adjusted ranking, the rotation gauge, the drawdown plan's distance from the Nasdaq-100 high ([`compute.py`](compute.py), reusing the scripts in [`analysis/`](../analysis/));
3. **researches the week** (company news, analyst changes, dilution, results dates, the AI build-out signals) and **drafts the review** in the journal's format, with a source for every claim ([`run_agent.py`](run_agent.py));
4. **opens a pull request** with the draft. I read it, check it, make the decisions and merge.

> Personal record, not financial advice.

## Design: what the model does and doesn't do

| | Done by | Why |
|---|---|---|
| Prices, zones, ranking, gauges | **Code** (deterministic, tested) | Numbers must be reproducible; a language model shouldn't be the source of a price |
| News, analyst changes, results dates, the write-up | **The agent** (Claude via the Agent SDK, with web search and fetch) | Judgment and reading, with citations |
| Decisions (orders, targets, rule changes) | **Me** | The agent lists them as questions with the trade-off; it can't act on them |

## Guardrails ([`guard.py`](guard.py), tested in [`tests/`](tests/))

- **One writable file.** A `PreToolUse` hook denies any write outside `weekly-reviews/drafts/`.
- **No shell, no broker.** The agent has no command line and no access to any trading account. It can read the repo, search the web and write a draft, nothing else.
- **No private data.** Reads of private folders are denied (and the cloud runner never has them: they aren't in the repo).
- **Blocked sites.** URLs on the blocked list in [`config.toml`](config.toml) are refused.
- **Publishing rules enforced.** The finished draft is rejected if it contains a £ amount, an email address, an ID-number-like string or a reference to private files. The journal publishes percentages and prices only.
- **Budget cap.** Each run stops at `max_budget_usd` (default $4). Logs print only a one-line summary, because Actions logs on a public repo are public.

## Running it

**In GitHub Actions** ([`.github/workflows/weekly-agent.yml`](../.github/workflows/weekly-agent.yml)): it runs automatically every Wednesday at 05:17 UTC and can be started by hand from the Actions tab ("Run workflow", with a dry-run option that skips the API call).

One-time setup:
1. Create an API key at [platform.claude.com](https://platform.claude.com) and add it to this repo as an Actions secret named `ANTHROPIC_API_KEY` (Settings → Secrets and variables → Actions). Never commit the key.
2. Optional: a free [Twelve Data](https://twelvedata.com) key as a second secret, `TWELVEDATA_API_KEY`, turns on the automatic price cross-check.
3. Settings → Actions → General → Workflow permissions: allow **Read and write** and tick **Allow GitHub Actions to create and approve pull requests**.

**Locally:**
```bash
pip install -r agent/requirements.txt
python -m unittest discover agent/tests
python agent/prices.py && python agent/compute.py
ANTHROPIC_API_KEY=... python agent/run_agent.py      # or --dry-run for no API call
```

## Cost

Claude Sonnet 5.5 at $2 / $10 per million input / output tokens, plus web search at $10 per 1,000 searches. A run of ~17 names with two searches each and a few page reads should come to roughly $1–3; the budget cap stops it at $4 whatever happens. Switch `model` to `"opus"` in `config.toml` for a deeper (dearer) run.

## Editing

- A name joins or leaves the book: edit the lists in [`config.toml`](config.toml).
- The capture-zone map is re-drawn by hand in [`analysis/capture_zones_final.py`](../analysis/capture_zones_final.py); then set `zones.map_week` in the config to that week's Friday so the agent only flags breaks after it.
