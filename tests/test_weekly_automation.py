"""Tests for the weekly social automation (scripts/automation/).

No network: stats use a tmp git repo; posters run in dry-run.
"""

import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts" / "automation"))

from weekly_stats import WeeklyStats, _current_week  # noqa: E402
import post_weekly  # noqa: E402


def test_week_clamped_1_to_12() -> None:
    before = datetime(2026, 5, 1, tzinfo=timezone.utc)  # before week 1
    way_after = datetime(2027, 1, 1, tzinfo=timezone.utc)  # past week 12
    mid = datetime(2026, 5, 28, tzinfo=timezone.utc)  # ~week 3
    assert _current_week(before) == 1
    assert _current_week(way_after) == 12
    assert _current_week(mid) == 3


def _fake_stats() -> WeeklyStats:
    return WeeklyStats(
        week=2, date_kst="2026-05-21 08:00 KST",
        commits_7d=9, files_touched_7d=42, stars=7, forks=1, open_issues=0,
    )


def test_twitter_thread_under_280() -> None:
    tweets = post_weekly.build_twitter_thread(_fake_stats())
    assert len(tweets) == 3
    for t in tweets:
        assert len(t) <= 280, f"tweet too long ({len(t)}): {t!r}"


def test_twitter_thread_has_week_and_links() -> None:
    tweets = post_weekly.build_twitter_thread(_fake_stats())
    joined = "\n".join(tweets)
    assert "Week 2/12" in joined
    assert "github.com/Yesol-Pilot/quant-poc-multi-asset" in joined
    assert "quant.heoyesol.kr" in joined
    assert "−15.1%" in joined  # honest-failure anchor present


def test_discord_message_under_2000() -> None:
    msg = post_weekly.build_discord_message(_fake_stats())
    assert len(msg) <= 2000
    assert "Week 2 of 12" in msg
    assert "Commits this week: `9`" in msg


def test_discord_dry_run_does_not_post() -> None:
    r = post_weekly.post_discord("hello", live=False)
    assert r.startswith("[dry-run]")


def test_discord_skip_when_no_webhook(monkeypatch) -> None:
    monkeypatch.delenv("DISCORD_WEBHOOK_URL", raising=False)
    r = post_weekly.post_discord("hello", live=True)
    assert r.startswith("[skip]")  # no webhook => skip, not crash


def test_twitter_dry_run_does_not_post() -> None:
    r = post_weekly.post_twitter(["a", "b"], live=False)
    assert r.startswith("[dry-run]")


def test_main_dry_run_all_channels_exit_zero() -> None:
    rc = post_weekly.main(["--channel", "all", "--repo-dir", str(REPO_ROOT)])
    assert rc == 0
