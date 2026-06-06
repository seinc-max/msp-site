#!/bin/bash
set -e

# Change directory
cd /data/msp-site

# 1. Rename files
mv it-support-ontario.html ai-governance-ontario.html
mv cybersecurity-southern-ontario.html shadow-ai-prevention-ontario.html
mv it-cost-guide-ontario.html ai-automation-roi-guide.html
mv microsoft-365-ontario-smbs.html safe-copilot-deployment.html
mv health-score.html ai-exposure-score.html
mv blog/20-southern-ontario-it-audits-2026.html blog/20-southern-ontario-shadow-ai-audits-2026.html

# 2. Update all internal links across the site to point to the new slugs
find . -type f -name "*.html" -exec sed -i 's/it-support-ontario/ai-governance-ontario/g' {} +
find . -type f -name "*.html" -exec sed -i 's/cybersecurity-southern-ontario/shadow-ai-prevention-ontario/g' {} +
find . -type f -name "*.html" -exec sed -i 's/it-cost-guide-ontario/ai-automation-roi-guide/g' {} +
find . -type f -name "*.html" -exec sed -i 's/microsoft-365-ontario-smbs/safe-copilot-deployment/g' {} +
find . -type f -name "*.html" -exec sed -i 's/health-score/ai-exposure-score/g' {} +
find . -type f -name "*.html" -exec sed -i 's/blog\/20-southern-ontario-it-audits-2026/blog\/20-southern-ontario-shadow-ai-audits-2026/g' {} +

# 3. Create Cloudflare _redirects file
cat << 'REDIR' > _redirects
/it-support-ontario /ai-governance-ontario 301
/cybersecurity-southern-ontario /shadow-ai-prevention-ontario 301
/it-cost-guide-ontario /ai-automation-roi-guide 301
/microsoft-365-ontario-smbs /safe-copilot-deployment 301
/health-score /ai-exposure-score 301
/blog/20-southern-ontario-it-audits-2026 /blog/20-southern-ontario-shadow-ai-audits-2026 301
REDIR

# 4. Also update sitemap.xml
if [ -f sitemap.xml ]; then
    sed -i 's/it-support-ontario/ai-governance-ontario/g' sitemap.xml
    sed -i 's/cybersecurity-southern-ontario/shadow-ai-prevention-ontario/g' sitemap.xml
    sed -i 's/it-cost-guide-ontario/ai-automation-roi-guide/g' sitemap.xml
    sed -i 's/microsoft-365-ontario-smbs/safe-copilot-deployment/g' sitemap.xml
    sed -i 's/health-score/ai-exposure-score/g' sitemap.xml
    sed -i 's/blog\/20-southern-ontario-it-audits-2026/blog\/20-southern-ontario-shadow-ai-audits-2026/g' sitemap.xml
fi

