⚠️ ATTENTION NANCY: Trueline IT has pivoted to AI consultancy as of June 2026. BUSINESS.md (updated June 2026) is the source of truth for current positioning, ICP, funnel, and strategy. Google Ads campaigns and competitor intelligence below reflect the old MSP model — treat as historical reference only until explicitly updated.

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
⚠️ NOTE (June 2026): Google Ads campaigns below target MSP keywords from the old positioning. Campaign messaging needs updating to reflect AI consultancy pivot. Do not create new ads or modify copy based on old MSP positioning without Ben instruction.
- Google Ads Search campaign live Apr 26 2026: TL-Search-GTAWest-DiscoveryCall-2026 (ID 23788467252). Budget updated to CA$32/day May 2026. M365 ad group 194650862094 PAUSED Apr 29. 17 zero-impression keywords paused Apr 29. 10 vertical long-tail keywords added to ad group 196695334300 Apr 29. Workflow x7m1HGFyQjImNwyf must always remain read-only GAQL SELECT only — see Rule 48. 3 ad groups: Managed IT High Intent (196695334300), IT Support Medium (198992609947), M365/AI (194650862094). Shared negatives 12063194315 attached. 6 sitelinks attached (2 new May 11 2026 with unique UTM URLs: ?utm_content=no-contract and ?utm_content=15min-response). Primary conversion: Native Lead Form Submit — GTM tag live May 11 2026 (Conversion ID: 18016129581, Label: y5qwCMmpsKscEK2k4Y5D). GA4 imported conversions demoted to secondary. Google Ads Daily Optimize workflow 0n1YhNFNkoLXDJU2 runs 6am daily.. HubSpot ↔ Google Ads connected. Auto-tagging ON. PMax campaign 23655945533 permanently PAUSED.
- Brevo Discovery Call Sequence activated Apr 26 2026. Exit condition: added to List #7 Booked a Call. HubSpot→Brevo sync confirmed working (8 contacts in List #8).
- Brevo MCP: LIVE as of May 12 2026 on OpenClaw 2026.5.7. Config: transport streamable-http, URL https://mcp.brevo.com/v1/brevo/mcp, auth header BREVO_MCP_TOKEN. Full brevo__* tool suite available natively in agent session. All Brevo automation and template edits can now be done via MCP — no longer UI-only.
## API Access
- All credentials managed as environment variables in Docker Manager
- Full variable list documented in TOOLS.md under Environment Variables section
- Never ask Ben for a credential — check TOOLS.md and printenv first

## Key Decisions
- May 10 2026: Resolved HubSpot form overwrite issue by removing hutk cookie passing and explicitly defining hubspot_owner_id=89556230 to attribute leads successfully. Global layout parity enforced for headers, footers, and mobile CTAs across all 17 templates.
- Google Ads API final URL update — correct method confirmed May 10 2026: Use POST https://googleads.googleapis.com/v23/customers/2424700037/ads:mutate (NOT googleAds:mutate). Operation key is 'operations' not 'mutateOperations'. Resource name is customers/2424700037/ads/{adId}. updateMask is 'finalUrls'. Returns adResult on success. Previous attempts using adGroupAds:mutate and googleAds:mutate returned HTTP 200 silently without updating — do not use those endpoints for finalUrl updates.
- Google Ads mutations execute via n8n internal API (POST http://n8n-kgmp-n8n-1:5678/api/v1/workflows/{id}/execute with X-N8N-API-KEY). Use Manual Trigger node — never webhook trigger for one-off mutations. Workflow x7m1HGFyQjImNwyf query updated May 10 2026 to SELECT from ad_group_ad for campaign 23788467252. Both ad final URLs updated to https://truelineit.com/it-support-ontario May 10 2026 — ads 806865450443 and 806865512399.
- Nancy manages tools as a user, not builder
- Business can pivot at any time via Telegram — update BUSINESS.md immediately on pivot
- SMS → HubSpot n8n workflow: live and working as of March 2026
- Deploy protocol: See GLOBAL_RULES Rule 24.
- OpenRouter cap: $200/mo. Alert Subanan at 70% usage (Rule 20)
- Current model: varies — Ben switches models via OpenRouter. Check OpenRouter Activity tab to confirm current model in use. Never assume a fixed model. Direct Google AI Studio integration attempted May 16 2026 but reverted due to performance issues — OpenRouter is primary.
- Heartbeat: disabled (every: 0m) as of Apr 2026 — zero idle cost
- MD files updated via host terminal (use host paths) or via Nancy exec commands (use container path /data/). Never through Nancy built-in edit tool — causes whitespace mismatch failures. See Rule 46 for path context.
- Do not use the OpenClaw Daily Backups Google Drive folder (1at6yE2lUFP89GTwuNNF3RZJ6xArKJUNh) for general file uploads. Only use it for actual backup files. For other files, ask Ben for a destination folder ID or upload them to the root.
- Never store general data extraction artifacts (e.g. CSVs, lead lists) permanently on the server. Always push exports directly to Drive and delete the local CSV artifacts immediately after successful upload.

- PDF Generation Tool initialized May 25 2026: Local Weasyprint script created at /data/.openclaw/workspace/scripts/generate_pdf.py for all HTML-to-PDF formatting to avoid failed dependency chaining or unauthorized external API usage.

- AI Search Visibility Report Template saved to /data/.openclaw/workspace/templates/AI_Search_Visibility_Report_Template.pdf for future client reports.
- Branded AI Search Visibility Report Template (final) saved to /data/.openclaw/workspace/templates/Branded_AI_Search_Visibility_Report.pdf

## Branding Assets
- Permanent vault: `/data/.openclaw/workspace/assets/branding/`
- Contents: Ben's HTML/JPG email signatures, and 4 Trueline logo variations (dark/light, transparent).

## PDF TEMPLATE (LOCKED):
- Build script: /data/.openclaw/workspace/templates/trueline_pdf_template.py
- Logo file: /data/.openclaw/workspace/assets/trueline_logo_transparent.png
- To generate a new client PDF: copy the build script, change the
  content only (company name, report content, data). Do NOT change
  any style functions, colours, or layout. Run with Python 3 using
  reportlab. The logo path in the script must point to the assets
  location above.
- The finished PDF design is at:
  /data/.openclaw/workspace/templates/Branded_AI_Search_Visibility_Report.pdf
  (reference only — this is the output, not the template)

## Frameworks & Influences

### Ash Maurya
- Fall in love with the problem, not your idea. Your first idea is usually wrong. What hurts the customer matters more than what you want to build.
- Sell it before you build it. Get someone to pay before you write a line of code or deliver a service.
- Words are cheap. Someone saying "I'd use that" means nothing. Money or committed time is the only real proof.
- A deposit beats a waiting list. Someone paying upfront proves the problem is real.
- Talk to customers, not spreadsheets. Real conversations reveal things that surveys and data never will.
- The fastest learner wins. Run small cheap tests, learn quickly, and repeat. Speed of learning beats speed of building.
- Test your biggest risk first. Figure out what could kill the business and test that before anything else.
- If people don't come back, you don't have a real business. Getting new customers just hides the problem temporarily.
- Busy is not the same as progress. Redesigning, adding features, and making pitch decks feel productive. They're not. Progress is customers paying and coming back.
- The way you sell and deliver matters as much as what you sell. Most businesses fail because of how they reach customers and charge them, not because the product was bad.
- Having less forces better decisions. Limited money and time make you focus and move faster. Too much money delays reality.
- One person with AI can now compete with a full team. But judgment, taste, and customer understanding still require the founder.
- Building a business is really just a process of removing unknowns one by one.

### Alex Hormozi
- If you can't charge more, fix the offer not the price. Price follows value.
- Good marketing doesn't feel like marketing. The best messages feel like helpful advice, not a sales pitch.
- Treat every lead the same way regardless of how they found you. Getting lazy with warm leads or referrals loses deals.
- Build systems that anyone can follow, not ones that depend on you. Scale comes from clear processes, not talented people.
- Do a lot before you optimise. Quality comes from repetition. Don't try to perfect things before you have enough data.
- Saying no is how you grow. Every opportunity you chase takes focus away from the one thing that's working.

### Gary Vaynerchuk
- Attention is the only asset that matters. Platforms come and go. Find where people's attention is cheap right now and go there.
- Getting your content seen matters more than making perfect content. Most people spend too much time creating and not enough time distributing.
- Give a lot before you ask for anything. Consistently helping people earns you the right to eventually make an ask.
- You're already living your content. Write down what you're doing, learning, and deciding. That's more valuable than invented topics.
- Done beats perfect. Launching something imperfect teaches you more than planning something perfect.
- Copy your own strengths, not someone else's strategy. You'll move faster doing what comes naturally to you.
- More attempts create more opportunities. Most people stop too early, just before things start compounding.
- AI makes creating content easier for everyone, which means being real, being consistent, and having good judgment matters more than ever.

### Dan Martell
- You are probably the thing slowing your business down. The goal is to make yourself less needed over time, not more busy.
- Hire or delegate before you need to, not after. You can't grow beyond your current capacity.
- Spend your time on the work only you can do. Everything else should be done by someone or something else.
- If Nancy can do something 80% as well as you, let her. Your time is worth more on the things only you can do.
- If you're solving the same problem twice, build a system. A business that needs you to function personally is fragile.
- Every quarter, ask what you should stop doing. Most founders add too much. Removing things creates more progress than adding them.
- Nancy is a tool to buy back your time. Use the time you save to focus on sales, relationships, and decisions only you can make.
- If growing the business makes your life harder, something is wrong with the model.

### Loom
- You can only find your real product by talking to people, not by looking at data. Loom spent 7 months going the wrong direction before a customer showed them the right one.
- The moment that makes customers love your product is rarely the one you think. Don't assume you know it until they show you.
- Every output should make the recipient want to take the next step or share it with someone else.
- Never pivot based on a feeling. Only change direction when a real customer gives you a clear signal.

## Competitor Intelligence
⚠️ NOTE (June 2026): Competitors listed below are MSP competitors from the old positioning. AI consultancy competitive landscape has not yet been researched. Treat this section as historical reference only.

### Tier 1 — Primary Competitors (study and copy)
- **NetFusion Designs (nfd.ca)** — Deep city-specific SEO pages for every GTA market. Copy: build dedicated it-support-[city] landing pages for every Southern Ontario city.
- **Wingman Solutions (wingmansolutions.ca)** — 101 five-star reviews, tight local geographic focus, flat-rate pricing. Copy: dominate Burlington/Hamilton local search before expanding.
- **Third Octet (thirdoctet.com)** — MSP Select Canada 2026 award, healthcare vertical specialization. Copy: earn one credible third-party credential or award as trust anchor.
- **ActiveIT Burlington** — Does not exist. Burlington local search is wide open. Copy: own Burlington IT support SEO aggressively.
- **Starport (starport.ca)** — Branded proprietary methodology ("IT Support PODs"). Copy: brand the Trueline IT Audit as a proprietary process that cannot be price-shopped.
- **Outsource IT Corp (outsourceitcorp.com)** — $39k/mo spend, 17 years, upper-funnel lead magnets (free eBooks, security quizzes) capture traffic not ready to book. Copy: promote Health Score tool as the primary lead magnet for ad traffic that bounces before booking.

## RESEARCH INTEGRITY RULE
Before running any multi-candidate research loop, you must run a single-candidate connectivity test on every API in the stack.

The test must confirm:
- API connected successfully
- API returned non-empty, non-default, non-error data
- Raw response shown to Ben for approval

If ANY API returns:
- Zero results across all candidates
- Default/neutral scores
- Error messages
- "Flat" for every trend

STOP IMMEDIATELY. Do not proceed. Do not assign default scores. Do not fabricate data. Report the specific failure and wait for instructions.

A research run with failed APIs is worse than no research run. It produces false confidence in bad data.
This rule applies to every research task, forever.

## PERMANENT RESEARCH METHODOLOGY RULES

REDDIT RULES:
- Minimum 5 unique posts required across minimum 3 subreddits
- Posts do NOT need to explicitly request an interactive tool
- Count posts that: describe the problem, ask how to solve it, complain about existing solutions, or ask for recommendations
- This is DEMAND signal not TOOL REQUEST signal
- Still require non-null scores where possible
- Still flag null scores

SERP RULES:
- Must return minimum 5 results per candidate
- For each result classify it as: interactive tool / static PDF / gated content / vendor landing page / blog post
- Gap score only counts if zero "interactive tool" results found
- Always paste exact titles and URLs — no summaries

GOOGLE TRENDS RULES:
- Always report trend DIRECTION based on last 30 days vs previous 30 days
- Do not describe a declining trend as "growing" or "stable"
- Flag any abnormal spikes and note they may be event-driven not organic
- Always show first value, peak value, last value, and direction arrow (↑↓→)

PRODUCT HUNT RULES:
- Search query must include the exact candidate problem keywords
- Validate results are actually relevant before scoring — irrelevant results = 0/10
- If returned results have zero topical relevance, report "no relevant results found"
- Never score irrelevant results as confirming a supply gap

SCORING RULES:
- Never assign a positive score to null, empty, or irrelevant data
- If an API returns insufficient data, score that component 0 — do not use neutral defaults
- Always show component scores separately before calculating total
- Never describe data as confirming a trend it does not confirm

REPORTING RULES:
- Never use qualitative language that goes beyond what the data shows
- "High engagement" requires minimum 10 unique posts with non-null scores
- "Growing trend" requires last 30 days average higher than previous 30 days average
- "Supply gap confirmed" requires zero interactive free tools in SerpAPI results
- Always distinguish between what the data shows and what you interpret

## CANDIDATE GENERATION RULES (PERMANENT)

1. NEVER generate candidates from your own knowledge or assumptions
2. ALL candidates must come from real data sources only
3. Candidate generation process must follow this exact order:

 STEP 1 - Mine real search data first:
 - Use SerpAPI to collect "People Also Ask" and "Related Searches" for broad queries
 - Use SerpAPI to find what people search for with "free [tool] for small business"

 STEP 2 - Mine real community data:
 - Use Apify Reddit scraper across minimum 4 relevant subreddits
 - Look for: complaints, questions, tool requests, workaround discussions
 - Minimum 12 month lookback period

 STEP 3 - Build candidate list from data:
 - Every candidate must cite the source that generated it
 - Format: "Candidate: [tool name] | Source: [Reddit post URL or SerpAPI query]"
 - No candidate is valid without a real data source citation

 STEP 4 - Present for approval:
 - Show Ben the candidate list with source citations
 - Wait for approval before running any research loop
 - Never run a loop on unapproved candidates

4. This rule applies to every future research task permanently
5. The current 20 candidates are grandfathered for this run only

## EARLY ELIMINATION RULE

Stage 1 - Google Trends pre-filter (run first):
- Purpose: Is the underlying problem growing?
- Use broad parent topic terms ONLY (e.g., "HR compliance", not "AI HR compliance tool").
- Check 5-year trend with "today 5-y" timeframe, global, no geo restriction.
- Score 0-15 based on YoY growth:
  - 0-3: flat/declining (ELIMINATE)
  - 4-7: steady growth
  - 8-11: strong growth
  - 12-15: exponential >200% YoY
- Only candidates with trend score 4 or above proceed to Stage 2.

Stage 2 - SERP pre-filter & Search Volume (SerpAPI, run second):
- Run only on Stage 1 survivors.
- Query format: "free [specific tool name]"
- Purpose A (Search Volume): How many people search for this specific tool? Score 0-10 based on monthly search volume estimates from SerpAPI.
- Purpose B (Supply Gap/Competition): Do free interactive tools already exist?
  - Classify top 5 organic results as: interactive tool / PDF / gated / blog
  - If 3 or more interactive free tools exist in top 5 → ELIMINATE immediately.
- Only candidates with 0-2 interactive free tools and sufficient search volume proceed to Stage 3.

Stage 3 - Full scoring (survivors only):
- Reddit via Apify
- Product Hunt via SerpAPI
- YouTube Data API
- Full SerpAPI scoring
- Apply complete 58-point model

## REDDIT VALIDATION METHODOLOGY (UPDATED)
- Primary method: SerpAPI queries using `site:reddit.com/[subreddit] "[topic]"` format.
- Secondary method: Apify Reddit scraper (trudax~reddit-scraper-lite) when working.

## PERMANENT ERROR PREVENTION RULES

ERROR 1 - NEVER SIMULATE DATA:
You previously claimed to use Apify, YouTube, and Product Hunt APIs but actually used simulated or estimated data. This is forbidden. If an API fails, stop and report the error. Never estimate, simulate, or fabricate API responses. Real data only, always.

ERROR 2 - NEVER USE GOOGLE RESULT COUNTS AS VOLUME:
You previously used numbers like "124,000,000 results" as search volume. This is meaningless. Search volume = PAA count + Related Searches count + ad presence only.

ERROR 3 - NEVER ASSIGN IDENTICAL SCORES TO ALL CANDIDATES:
If every candidate scores the same, the methodology is broken. Real data always has variance. Identical scores across all candidates = stop and recheck your data source.

ERROR 4 - NEVER ELIMINATE WITHOUT VERIFYING COMPETING TOOLS:
You previously eliminated candidates based on tool counts without verifying those tools were actually free, interactive, and solving the exact same problem. Always name tools with URLs and verify before eliminating.

ERROR 5 - NEVER USE WRONG SEARCH TERMS:
For Google Trends: use broad parent topics only (e.g. "AI policy" not "free AI acceptable use policy generator for small business")
For SerpAPI: use specific tool queries only (e.g. "free AI acceptable use policy generator" not "AI policy")
These are opposite requirements. Never confuse them.

ERROR 6 - NEVER CLAIM AN API WAS USED WHEN IT WASN'T:
You previously reported YouTube API data that was not actually fetched. If an API was not called, do not report its results. Honesty about API failures is required.

ERROR 7 - NEVER PROCEED AFTER A RESEARCH INTEGRITY RULE VIOLATION:
If any API returns zero results across all candidates, flat data, or errors — stop immediately. Do not pad scores. Do not use defaults. Report the failure and wait for instructions.

## PERMANENT METHODOLOGY FIXES (June 2026)

FIX 1 - GOOGLE TRENDS PARENT TOPIC MAPPING:
Always map each candidate to its AI-specific parent topic before running Stage 1.
Never use legacy/generic versions of topics.
Wrong: "acceptable use policy" Right: "AI policy"
Wrong: "standard operating procedure" Right: "AI automation"
Wrong: "HR compliance" Right: "AI HR compliance"
The AI prefix matters — it captures the explosive growth curve not the flat legacy curve.

FIX 2 - SEARCH VOLUME SIGNALS (in order of reliability):
1. SerpAPI monthly volume field if available
2. PAA (People Also Ask) count — more PAA = higher intent
3. Related Searches count
4. Ad presence (ads = commercial intent = real volume)
Score: 0 PAA + 0 ads = 1/10, 1-2 PAA = 4/10, 3-4 PAA = 7/10, 5+ PAA + ads = 10/10
Never use total result counts as volume proxy.

FIX 3 - ELIMINATION VERIFICATION CHECKLIST:
Before eliminating any candidate, verify each competing tool against all 3 criteria:
- Is it actually free? (not freemium, not trial, not gated behind signup)
- Is it actually interactive? (not a PDF, not a static template, not a download)
- Is it solving the exact same problem for the exact same audience?
A tool fails if it does not pass all 3 criteria.
Only count tools that pass all 3 toward the elimination threshold.

FIX 4 - PREVIOUS WINNER PROTECTION:
Any candidate scoring 45+ out of 58 in a prior validated run cannot be eliminated in Stage 2 without:
- Naming all competing tools with URLs
- Verifying each tool passes the 3-criteria checklist above
- Ben approving the elimination explicitly

FIX 5 - PRODUCT HUNT QUERY FORMAT:
Use exact quoted phrases: site:producthunt.com "exact tool name"
Not: site:producthunt.com "general category"
Verify top 3 results are topically relevant before scoring.
Generic tools in adjacent categories do not count as supply.

FIX 6 - YOUTUBE SCORING BY VIEW COUNT:
Score based on maximum view count of top 3 relevant videos:
- 0 relevant videos = 0/7
- Videos under 10K views = 2/7
- Highest under 100K views = 4/7
- Videos with 100K-500K views = 6/7
- Videos with 500K+ views = 7/7
Never score based on video count alone.

FIX 7 - REDDIT VALIDATION METHOD:
Primary method: SerpAPI site:reddit.com "[topic]" queries
Secondary method: Apify trudax~reddit-scraper-lite (when working)
Minimum requirement: 5 unique posts across 3 different subreddits
Posts and comments are different — count separately
Null scores must be flagged — never assign positive scores to null data

FIX 8 - STAGE EXECUTION ORDER:
Always run in this exact order:
Stage 1: Google Trends (parent topic, 5-year, global, no geo)
Stage 2: SerpAPI SERP gap + search volume (specific tool query)
Stage 3: Reddit + Product Hunt + YouTube (full scoring)
Never run Stage 3 before Stage 1 and 2 are complete and approved.

FIX 9 - VARIANCE CHECK:
After scoring any batch of candidates, check for variance.
If 3 or more candidates score identically on any single component — stop.
Recheck the data source and scoring logic before proceeding.
Real data always has variance. Identical scores = broken methodology.
