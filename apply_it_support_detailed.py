import sys

file_path = "/data/msp-site/it-support-ontario.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Description Meta
content = content.replace(
    '<meta name="description" content="Flat-rate IT support for Ontario SMBs. 15-min response, 24/7 helpdesk, no contracts. Starting at $99/user/mo." />',
    '<meta name="description" content="Flat-rate AI governance and IT support for Ontario. 15-min response, secure automation, shadow AI audits, no contracts." />'
)

# 2. Update Hero text
content = content.replace(
    '<h1>IT that works.<br>Prices that don\'t change.</h1>',
    '<h1>Stop Shadow AI Leaks.<br>Deploy Real Automation.</h1>'
)

content = content.replace(
    '<p class="hero-sub">Get your Ontario business off the break-fix treadmill. <strong>Flat-rate monthly support. 15-minute response times.</strong> We monitor your security, manage your backups, and fix your tech before it breaks. No surprise invoices, no long-term contracts.</p>',
    '<p class="hero-sub">Get your professional services business off the manual task treadmill. We audit your M365 permissions, lock down ChatGPT leaks, and build real automation that scales. <strong>Flat-rate monthly compliance. No enterprise consultant fees. No surprise invoices.</strong></p>'
)

# Fix Pricing Cards
# Card 1
content = content.replace('<p class="offer-card-label">Basic</p>', '<p class="offer-card-label">Compliance</p>')
content = content.replace('<h3>$99<span> / user / mo</span></h3>', '<h3>$1,500<span> / mo</span></h3>')
content = content.replace('<li>Unlimited helpdesk support</li>', '<li>AI Acceptable Use Policy</li>')
content = content.replace('<li>Proactive monitoring</li>', '<li>Shadow AI Audit</li>')
content = content.replace('<li>Automated backups</li>', '<li>M365 Copilot Audit</li>')
content = content.replace('<li>Business hours support</li>', '<li>Employee Training</li>')
# Card 2
content = content.replace('<p class="offer-card-label">Professional</p>', '<p class="offer-card-label">Growth</p>')
content = content.replace('<h3>$149<span> / user / mo</span></h3>', '<h3>$2,500<span> / mo</span></h3>')
content = content.replace('<li>After-hours coverage</li>', '<li>Everything in Compliance</li>')
content = content.replace('<li>Priority response</li>', '<li>1 Custom Automation Build /mo</li>')
content = content.replace('<li>Monthly security report</li>', '<li>Private LLM Deployment</li>')
content = content.replace('<li>Dedicated account manager</li>', '<li>Priority Helpdesk</li>')
# Card 3 
content = content.replace('<p class="offer-card-label">Complete</p>', '<p class="offer-card-label">Scale</p>')
content = content.replace('<h3>$199<span> / user / mo</span></h3>', '<h3>$4,000<span> / mo</span></h3>')
content = content.replace('<li>24/7 emergency support</li>', '<li>Everything in Growth</li>')
content = content.replace('<li>Advanced threat protection</li>', '<li>3 Custom Automation Builds /mo</li>')
content = content.replace('<li>Compliance reporting</li>', '<li>Custom Copilot Plugins</li>')
content = content.replace('<li>Quarterly IT reviews</li>', '<li>Strategic AI Roadmap</li>')


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

