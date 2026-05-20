"""Gather the weekly-progress stats shared by every channel.

The Telegram cron (.github/workflows/weekly-progress-telegram.yml) computes the
same numbers inline in YAML. This module is the Python equivalent, reused by the
Twitter + Discord posters so all channels report identical figures.

No required credentials: GitHub repo stats come from the public REST API
(GITHUB_TOKEN raises the rate limit if present but isn't required). Commit/file
counts come from `git log` in the working tree.
"""

from __future__ import annotations

import json
import os
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from urllib.request import Request, urlopen

REPO = "Yesol-Pilot/quant-poc-multi-asset"
WEEK0 = datetime(2026, 5, 14, tzinfo=timezone.utc)  # Week 1 D1


@dataclass
class WeeklyStats:
    week: int  # 1..12, clamped
    date_kst: str
    commits_7d: int
    files_touched_7d: int
    stars: int
    forks: int
    open_issues: int

    def as_dict(self) -> dict:
        return asdict(self)


def _git(args: list[str], cwd: str | None = None) -> str:
    """Run a git command, returning stdout. Forces UTF-8 decode (commit
    messages contain non-ASCII like '−15.1%' and emoji; the Windows default
    cp949 would crash). Always returns a string, never None."""
    try:
        out = subprocess.run(
            ["git", *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=20,
        )
        return out.stdout or ""
    except (subprocess.SubprocessError, FileNotFoundError):
        return ""


def _current_week(now: datetime | None = None) -> int:
    now = now or datetime.now(timezone.utc)
    weeks = (now - WEEK0).days // 7 + 1
    return max(1, min(12, weeks))


def _github_repo_stats() -> tuple[int, int, int]:
    """(stars, forks, open_issues) from the public GitHub API. Returns (0,0,0)
    on any failure — a flaky network shouldn't break a weekly post."""
    url = f"https://api.github.com/repos/{REPO}"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "qpm-weekly"}
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=15) as resp:  # noqa: S310 (fixed trusted host)
            data = json.loads(resp.read().decode("utf-8"))
        return (
            int(data.get("stargazers_count", 0)),
            int(data.get("forks_count", 0)),
            int(data.get("open_issues_count", 0)),
        )
    except Exception:  # noqa: BLE001 - intentional: never fail the post on stats
        return (0, 0, 0)


def gather_stats(repo_dir: str | None = None, *, now: datetime | None = None) -> WeeklyStats:
    """Collect this week's stats. `repo_dir` defaults to the current tree."""
    commits = _git(["log", "--since=7 days ago", "--oneline"], cwd=repo_dir)
    commits_7d = len([ln for ln in commits.splitlines() if ln.strip()])

    files = _git(
        ["log", "--since=7 days ago", "--name-only", "--pretty=format:"], cwd=repo_dir
    )
    files_touched_7d = len({ln.strip() for ln in files.splitlines() if ln.strip()})

    stars, forks, issues = _github_repo_stats()

    # KST timestamp (UTC+9)
    n = now or datetime.now(timezone.utc)
    kst = n.timestamp() + 9 * 3600
    date_kst = datetime.fromtimestamp(kst, tz=timezone.utc).strftime("%Y-%m-%d %H:%M KST")

    return WeeklyStats(
        week=_current_week(now),
        date_kst=date_kst,
        commits_7d=commits_7d,
        files_touched_7d=files_touched_7d,
        stars=stars,
        forks=forks,
        open_issues=issues,
    )


__all__ = ["WeeklyStats", "gather_stats", "REPO", "WEEK0"]
