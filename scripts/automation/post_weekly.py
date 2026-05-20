"""Post the weekly progress update to Twitter and/or Discord.

Owner mandate: one-time setup per channel, then full automation. Once the
relevant env vars are present, this script (driven by a cron/CI schedule)
posts every Monday with zero owner involvement.

DRY-RUN IS THE DEFAULT. Nothing is posted unless `--post` is passed AND the
channel's credentials are present. This makes the script safe to run in CI for
formatting verification.

Channels
--------
twitter : Twitter API v2 tweet/thread. Requires
          TWITTER_BEARER_TOKEN (or the OAuth1 quartet for posting).
discord : Discord channel webhook. Requires DISCORD_WEBHOOK_URL.

Usage
-----
    python scripts/automation/post_weekly.py --channel twitter            # dry-run
    python scripts/automation/post_weekly.py --channel discord --post     # live
    python scripts/automation/post_weekly.py --channel all                # dry-run both
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).parent))
from weekly_stats import WeeklyStats, gather_stats  # noqa: E402

REPO_URL = "https://github.com/Yesol-Pilot/quant-poc-multi-asset"
LIVE_URL = "https://quant.heoyesol.kr"


# ── message builders ────────────────────────────────────────────────────
def build_twitter_thread(s: WeeklyStats) -> list[str]:
    """Return the tweets of the weekly thread (<=280 chars each). Honest-failure
    voice, mirrors docs/marketing/twitter-pinned-tweet.md."""
    head = (
        f"quant-poc-multi-asset — Week {s.week}/12\n\n"
        f"This week: {s.commits_7d} commits, {s.files_touched_7d} files touched.\n"
        f"GitHub: {s.stars}⭐ / {s.forks} forks / {s.open_issues} open issues.\n\n"
        f"Open-source multi-asset quant rebuild. Honest failure first.\n"
        f"\U0001f9f5 ↓"
    )
    body = (
        f"Every alpha ships with a Deflated Sharpe Ratio + Probability of "
        f"Backtest Overfitting before it touches paper money.\n\n"
        f"The 38-day crypto PoC closed at −15.1% — that loss is on the "
        f"record so the kill switch reads as safety, not a victory lap."
    )
    tail = f"Code: {REPO_URL}\nLive: {LIVE_URL}\n\nNo upsell. No course. No paywall."
    return [head, body, tail]


def build_discord_message(s: WeeklyStats) -> str:
    """Discord markdown (2000-char limit; this is well under)."""
    return (
        f"**\U0001f4ca quant-poc-multi-asset — Weekly Progress**\n"
        f"_Week {s.week} of 12 · {s.date_kst}_\n\n"
        f"• Commits this week: `{s.commits_7d}`\n"
        f"• Files touched: `{s.files_touched_7d}`\n"
        f"• GitHub stars: `{s.stars}`  ·  Forks: `{s.forks}`  ·  Open issues: `{s.open_issues}`\n\n"
        f"\U0001f517 <{REPO_URL}>  ·  <{LIVE_URL}>\n"
        f"_Automated weekly report · honest failure first_"
    )


# ── posters (no-op unless --post + credentials) ──────────────────────────
def post_discord(message: str, *, live: bool) -> str:
    webhook = os.environ.get("DISCORD_WEBHOOK_URL", "")
    if not live:
        return "[dry-run] discord message built (not posted)"
    if not webhook:
        return "[skip] DISCORD_WEBHOOK_URL absent — owner one-time setup pending"
    payload = json.dumps({"content": message}).encode("utf-8")
    req = Request(
        webhook, data=payload, headers={"Content-Type": "application/json"}, method="POST"
    )
    with urlopen(req, timeout=15) as resp:  # noqa: S310
        return f"[posted] discord HTTP {resp.status}"


def post_twitter(tweets: list[str], *, live: bool) -> str:
    bearer = os.environ.get("TWITTER_BEARER_TOKEN", "")
    if not live:
        return f"[dry-run] twitter thread built ({len(tweets)} tweets, not posted)"
    if not bearer:
        return "[skip] TWITTER_BEARER_TOKEN absent — owner one-time setup pending"
    # NOTE: posting tweets requires OAuth1 user context (not just bearer).
    # The live posting path is wired at W2 once the owner provisions the
    # Twitter dev app + access tokens; until then this returns a clear skip.
    return "[skip] live Twitter posting needs OAuth1 user tokens (W2 owner setup)"


# ── cli ───────────────────────────────────────────────────────────────────
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Post weekly progress to social channels")
    ap.add_argument("--channel", choices=["twitter", "discord", "all"], default="all")
    ap.add_argument("--post", action="store_true", help="actually post (default: dry-run)")
    ap.add_argument("--repo-dir", default=None, help="git repo dir (default: cwd)")
    args = ap.parse_args(argv)

    stats = gather_stats(args.repo_dir)
    live = args.post
    results: list[str] = []

    if args.channel in ("twitter", "all"):
        tweets = build_twitter_thread(stats)
        print("=== Twitter thread ===")
        for i, t in enumerate(tweets, 1):
            print(f"--- tweet {i} ({len(t)} chars) ---\n{t}\n")
        results.append(post_twitter(tweets, live=live))

    if args.channel in ("discord", "all"):
        msg = build_discord_message(stats)
        print("=== Discord message ===")
        print(msg, "\n")
        results.append(post_discord(msg, live=live))

    print("=== results ===")
    for r in results:
        print(r)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
