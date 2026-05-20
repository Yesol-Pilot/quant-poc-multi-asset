# Social automation — weekly progress posters

Owner model: **one-time setup per channel, then full automation.** Once a
channel's credentials are present, the weekly poster runs on a schedule with
zero owner involvement.

Telegram is already live (see `.github/workflows/weekly-progress-telegram.yml`,
secrets `CLAUDE_ALERT_BOT_TOKEN` + `OWNER_TELEGRAM_CHAT_ID` — set 2026-05-16).
Twitter and Discord are scaffolded here and activate the moment their tokens
land.

## Files

- `weekly_stats.py` — gathers the shared stats (commits/files from `git log`,
  stars/forks/issues from the public GitHub API). No credentials required.
- `post_weekly.py` — builds + posts the per-channel message. **Dry-run by
  default**; pass `--post` to go live. Safe to run in CI (formatting check).

## Dry-run (no setup, no posting)

```bash
python scripts/automation/post_weekly.py --channel all      # both, dry-run
python scripts/automation/post_weekly.py --channel twitter  # twitter only
```

Prints the exact thread/message that would be posted. Used by CI to verify
formatting and the <280 / <2000 char limits.

## One-time owner setup per channel

### Discord (~5 min — easiest)
1. In your Discord server: Server Settings → Integrations → Webhooks → New
   Webhook → pick a channel → Copy Webhook URL.
2. Add to `.env` (and, for the cron, to GitHub repo secrets):
   `DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...`
3. Verify: `python scripts/automation/post_weekly.py --channel discord --post`

That's it — no bot application needed for posting. (A full bot for
mention-handling is a W3+ upgrade.)

### Twitter / X (~15 min)
1. https://developer.twitter.com → create a Free-tier project + app
   (1,500 posts/month is plenty for weekly).
2. In the app's Keys & Tokens: generate API Key + Secret and an Access Token +
   Secret with **Read and Write** permission (posting needs OAuth1 user
   context, not just the bearer token).
3. Add to `.env` + repo secrets:
   ```
   TWITTER_API_KEY=...
   TWITTER_API_SECRET=...
   TWITTER_ACCESS_TOKEN=...
   TWITTER_ACCESS_SECRET=...
   TWITTER_BEARER_TOKEN=...
   ```
4. The OAuth1 posting path is wired at W2 once these exist; until then the
   poster prints the thread and reports `[skip]` for the live post.

## Scheduling (after setup)

Add a GitHub Actions workflow mirroring the Telegram one (Monday 08:00 KST),
calling:

```bash
python scripts/automation/post_weekly.py --channel all --post
```

The poster no-ops any channel whose credentials are still absent, so a partial
setup (e.g. Discord live, Twitter pending) posts only where it can.

## Safety

- Dry-run is the default; `--post` is required to publish.
- Each channel independently skips (never crashes) when its credentials are
  absent.
- Stats gathering never fails the post: a flaky GitHub API returns zeros, git
  errors return empty strings.
- No credential is ever printed; the script reads them from the environment.
