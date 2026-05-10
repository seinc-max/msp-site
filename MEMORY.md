⚠️ ATTENTION NANCY: All strategy files dated 2026-03-31 and earlier are DEPRECATED. They contain stale funnel logic from the old direct-close model. Reference only BUSINESS.md (revised 2026-04-03) for current funnel, sales process, and phase triggers.

# MEMORY.md

## Who I Work For
Ben — entrepreneur and closer. His job is to make key decisions and close deals.
My job is to run everything else end-to-end.

## Current Line of Business
Trueline IT — active. See BUSINESS.md for full context.

## Infrastructure
- Hostinger VPS: srv1421891 (IP: 187.77.221.231)
- Docker containers: openclaw-ywis-openclaw-1, n8n-kgmp-n8n-1, nginx-proxy-manager-npm-1
- Cloudflare: CDN and SSL for truelineit.com
- GitHub: https://github.com/seinc-max/msp-site
- n8n: https://n8n-kgmp.srv1421891.hstgr.cloud
- Backup: daily tar to Google Drive (OpenClaw Daily Backups folder)
- Workspace path (HOST): /docker/openclaw-ywis/data/.openclaw/workspace/ | Workspace path (CONTAINER exec): /data/.openclaw/workspace/ — always use container path in Nancy exec commands. See Rule 46.
- Google Ads API n8n integration (confirmed working Apr 22 2026): workflow x7m1HGFyQjImNwyf. DO NOT use login-customer-id header when using predefined googleAdsOAuth2Api credential type in n8n — it causes USER_PERMISSION_DENIED 403. Developer token goes as manual header only. OAuth app: Trueline IT Google Ads, Google Cloud project trueline-it-494200 under truelineit.com org, Client ID: 1019175895760-goolnl4bffsa2sf6j2lq2bd9uqsvrsup.apps.googleusercontent.com. Old leadgibbon.cc project (trueline-it-490303) shut down Apr 22 2026.

- Favicon updated Apr 25 — new favicon.svg with embedded Gelasio glyph path (Georgia-equivalent, no system font dependency). Pushed to staging and merged to main, commit 0189bb0. File at /docker/openclaw-ywis/data/msp-site/favicon.svg.
- Google Ads Search campaign live Apr 26 2026: TL-Search-GTAWest-DiscoveryCall-2026 (ID 23788467252). Budget updated to CA$32/day May 2026. M365 ad group 194650862094 PAUSED Apr 29. 17 zero-impression keywords paused Apr 29. 10 vertical long-tail keywords added to ad group 196695334300 Apr 29. Workflow x7m1HGFyQjImNwyf must always remain read-only GAQL SELECT only — see Rule 48. 3 ad groups: Managed IT High Intent (196695334300), IT Support Medium (198992609947), M365/AI (194650862094). Shared negatives 12063194315 attached. 4 sitelinks attached. Primary conversion: manual_event_SUBMIT_LEAD_FORM via GTM — verified firing Apr 26. HubSpot ↔ Google Ads connected. Auto-tagging ON. PMax campaign 23655945533 permanently PAUSED.
- Brevo Discovery Call Sequence activated Apr 26 2026. Exit condition: added to List #7 Booked a Call. HubSpot→Brevo sync confirmed working (8 contacts in List #8).
## API Access
- All API credentials managed as environment variables in Docker Manager

## Key Decisions
- May 10 2026: Resolved HubSpot form overwrite issue by removing hutk cookie passing and explicitly defining hubspot_owner_id=89556230 to attribute leads successfully. Global layout parity enforced for headers, footers, and mobile CTAs across all 17 templates.
- Google Ads API final URL update — correct method confirmed May 10 2026: Use POST https://googleads.googleapis.com/v23/customers/2424700037/ads:mutate (NOT googleAds:mutate). Operation key is 'operations' not 'mutateOperations'. Resource name is customers/2424700037/ads/{adId}. updateMask is 'finalUrls'. Returns adResult on success. Previous attempts using adGroupAds:mutate and googleAds:mutate returned HTTP 200 silently without updating — do not use those endpoints for finalUrl updates.
- Google Ads mutations execute via n8n internal API (POST http://n8n-kgmp-n8n-1:5678/api/v1/workflows/{id}/execute with X-N8N-API-KEY). Use Manual Trigger node — never webhook trigger for one-off mutations. Workflow x7m1HGFyQjImNwyf query updated May 10 2026 to SELECT from ad_group_ad for campaign 23788467252. Both ad final URLs updated to https://truelineit.com/it-support-ontario May 10 2026 — ads 806865450443 and 806865512399.
- Nancy manages tools as a user, not builder
- Business can pivot at any time via Telegram — update BUSINESS.md immediately on pivot
- SMS → HubSpot n8n workflow: live and working as of March 2026
- Deploy protocol: See GLOBAL_RULES Rule 24.
- OpenRouter cap: $200/mo. Alert Subanan at 70% usage (Rule 20)
- Current model: varies — Ben switches between GPT-5.2 and Gemini 3.1 Pro Preview via OpenRouter. Check OpenRouter Activity tab to confirm current model in use. Never assume a fixed model.
- Heartbeat: disabled (every: 0m) as of Apr 2026 — zero idle cost
- MD files updated via host terminal (use host paths) or via Nancy exec commands (use container path /data/). Never through Nancy built-in edit tool — causes whitespace mismatch failures. See Rule 46 for path context.
