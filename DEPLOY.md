# Deployment Pipeline: Cloudflare Pages

This repository is pre-configured for deployment to Cloudflare Pages as a static site.

## Pipeline Instructions

1. **Connect Repository:** In the Cloudflare dashboard, go to "Workers & Pages" > "Create application" > "Pages" > "Connect to Git" and select this `msp-site` repository.
2. **Build Settings:**
   - **Framework preset:** Next.js (Static HTML Export)
   - **Build command:** `npm run build`
   - **Build output directory:** `out`
3. **Environment Variables:** Include any necessary API keys (none required for the base static build).
4. **Deploy:** Cloudflare will read the `output: "export"` from `next.config.js` and build to the `/out` directory automatically on every push to the `main` branch.
5. **Custom Domain:** Navigate to "Custom Domains" in the Pages project settings and link `truelineit.com` (managed via Namecheap/Cloudflare DNS).
