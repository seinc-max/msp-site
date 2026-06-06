import os

schema_block = """<link rel="canonical" href="https://truelineit.com/ai-governance-ontario" />
<meta property="og:image" content="https://truelineit.com/assets/og-image.png" />
<meta name="twitter:image" content="https://truelineit.com/assets/og-image.png" />
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Service",
 "name": "AI Governance & Automation",
 "provider": {
 "@type": "Organization",
 "name": "Trueline IT",
 "url": "https://truelineit.com"
 },
 "areaServed": "Ontario, Canada",
 "serviceType": "AI Governance and Automation",
 "description": "Flat-rate AI governance and automation for Ontario professional services businesses. Documented AI policy, shadow AI audits, Copilot compliance, and secure workflow automation."
}
</script>
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "FAQPage",
 "mainEntity": [
 {
 "@type": "Question",
 "name": "What does AI governance cost in Ontario?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "Trueline IT charges a flat monthly fee per business, starting at $1,500/month. Pricing is per business, not per user. No contracts, cancel anytime."
 }
 },
 {
 "@type": "Question",
 "name": "What is included in AI governance?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "A documented AI Acceptable Use Policy, a shadow AI audit, Microsoft 365 and Copilot configuration, insurer-ready compliance documentation, and ongoing policy updates as regulations change."
 }
 },
 {
 "@type": "Question",
 "name": "Why does my business need an AI policy?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "In May 2026 Canada's Privacy Commissioner ruled ChatGPT violated PIPEDA. The Law Society of Ontario has warned about disciplinary action for AI data misuse. Cyber insurers now require documented AI policies at renewal."
 }
 }
 ]
}
</script>
</head>"""

filepath_1 = "/data/msp-site/ai-governance-ontario.html"
if os.path.exists(filepath_1):
    with open(filepath_1, "r", encoding="utf-8") as f:
        content = f.read()
    if "FAQPage" not in content or "AI Governance & Automation" in content: # just replace last </head>
        parts = content.rsplit("</head>", 1)
        content = parts[0] + schema_block + parts[1]
        with open(filepath_1, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated ai-governance-ontario.html")

filepath_2 = "/data/msp-site/blog/blog-post.html"
if os.path.exists(filepath_2):
    with open(filepath_2, "r", encoding="utf-8") as f:
        content = f.read()
    parts = content.rsplit("</head>", 1)
    content = parts[0] + '<meta name="robots" content="noindex, nofollow" />\n</head>' + parts[1]
    with open(filepath_2, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated blog/blog-post.html")

