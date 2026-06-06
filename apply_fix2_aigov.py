import sys

file_path = "/data/msp-site/ai-governance-ontario.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Make sure we don't mess up previously completed alignments
# CHANGE 1
content = content.replace(
    '<title>IT Support & AI Automation in Ontario | Trueline IT</title>',
    '<title>AI Governance & Automation in Ontario | Trueline IT</title>'
)

# CHANGE 2
content = content.replace(
    'Flat-rate AI governance and IT support for Ontario. 15-min response, secure automation, shadow AI audits, no contracts.',
    'Flat-rate AI governance and automation for Ontario professional services businesses. Documented AI policy, shadow AI audits, Copilot compliance, no contracts.'
)

# CHANGE 3
content = content.replace(
    'Ontario IT Support — Starting at $99/user/mo',
    'AI Governance & Automation for Ontario Professional Services'
)

# CHANGE 4
content = content.replace(
    'Flat-rate IT support.<br><em>No surprise bills.</em><br>15-min response.',
    'Your team is using AI with client data.<br><em>One mistake</em> can cost you everything.'
)

# CHANGE 5
content = content.replace(
    'Your dedicated IT team — without the cost of hiring one. Built for Southern Ontario businesses with 10–50 employees. Unlimited helpdesk, cybersecurity, and 24/7 monitoring.',
    'In May 2026, Canada\'s Privacy Commissioner ruled that ChatGPT violated PIPEDA. The Law Society of Ontario has warned lawyers that using public AI tools with client data risks disciplinary action. Trueline IT gives your business a documented AI policy, safe tools, and ongoing compliance management — for a flat monthly fee.'
)

# ... (the rest were already done in align-city-pages-batch-3.py which ran previously)
# Verifying text specifically needed from the new instruction set

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

