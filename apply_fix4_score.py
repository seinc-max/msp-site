import sys
import re

file_path = "/data/msp-site/ai-exposure-score.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# CHANGE 1
content = content.replace(
    'This diagnostic covers the 15 most critical IT risks: proactive monitoring, verified backups, security patching, multi-factor authentication, PIPEDA compliance, disaster recovery, hardware inventory, password management, after-hours support, and staff training. Each question is scored 0 or 1. Your total score (out of 15) tells you exactly where your business stands.',
    'This diagnostic covers the most critical AI exposure risks: shadow AI usage, client data leakage, AI acceptable use policy, M365 Copilot configuration, PIPEDA compliance, employee AI training, vendor risk, and cyber insurance readiness. Each question is scored. Your total score tells you exactly where your business stands.'
)

# CHANGE 2
content = content.replace(
    '<h3>"Everything breaks at the worst time."</h3>\n        <p>A server goes down on Friday afternoon. Your point-of-sale freezes mid-transaction. Your team can\'t get online. You\'re scrambling — and losing money every minute.</p>',
    '<h3>"My team is using ChatGPT with client data and I found out by accident."</h3>\n        <p>Employees paste contracts, financials, and client notes into public AI tools every day. You didn\'t authorize it. You don\'t know how much has already left the building.</p>'
)

# CHANGE 3
content = content.replace(
    '<h3>"I never know what IT is going to cost."</h3>\n        <p>Random invoices. Emergency callout fees. Hardware you didn\'t expect. IT feels like a bill that arrives with no warning and no explanation.</p>',
    '<h3>"My cyber insurer sent a renewal form asking about AI governance. I don\'t have answers."</h3>\n        <p>Insurers are now asking which AI tools your team uses, what policies are in place, and who is responsible. Businesses that can\'t answer are seeing premiums rise — or claims denied.</p>'
)

# CHANGE 4
content = content.replace(
    '<h3>"I don\'t know if we\'re actually secure."</h3>\n        <p>You\'ve heard the horror stories — ransomware, phishing, stolen data. You don\'t know if it could happen to you, and honestly, you don\'t know who to ask.</p>',
    '<h3>"A client asked me directly: what is your AI data handling policy?"</h3>\n        <p>You didn\'t have a good answer. Neither does most of your competition — yet. The businesses that get ahead of this question will win the clients who ask it.</p>'
)

# CHANGE 5
content = content.replace(
    'Flat per-user pricing',
    'Flat monthly fee — no per-seat billing'
)

# CHANGE 6
content = content.replace(
    '<li>Unlimited helpdesk support — call, email, or chat</li>\n        <li>Microsoft 365 &amp; Google Workspace management</li>\n        <li>Automated backups &amp; disaster recovery</li>\n        <li>Proactive monitoring — we catch problems before you do</li>\n        <li>Cybersecurity essentials included</li>\n        <li>A real person who knows your business</li>',
    '<li>AI Acceptable Use Policy — created, maintained, and updated</li>\n        <li>Shadow AI audit — full visibility into what tools your team is using</li>\n        <li>M365 and Google Workspace AI configuration — ring-fenced and safe</li>\n        <li>Insurer-ready compliance documentation — updated annually</li>\n        <li>Monthly 30-minute review call</li>\n        <li>A flat monthly fee — no per-seat billing, ever</li>'
)

# CHANGE 7
content = content.replace(
    '<p class="offer-card-label">Basic</p>\n          <h3>$99<span> / user / mo</span></h3>\n          <p class="offer-price-note">Everything included. No hidden fees.</p>',
    '<p class="offer-card-label">Foundation</p>\n          <h3>$1,500<span> / mo</span></h3>\n          <p class="offer-price-note">For businesses with 15–30 employees.</p>'
)

# CHANGE 8
content = content.replace(
    '<li>Unlimited helpdesk support</li>\n            <li>Proactive monitoring</li>\n            <li>Automated backups</li>\n            <li>Business hours support</li>\n            <li>Cancel anytime</li>',
    '<li>AI Acceptable Use Policy — created and maintained</li>\n            <li>Shadow AI audit — quarterly</li>\n            <li>M365 AI configuration</li>\n            <li>Insurer-ready compliance report</li>\n            <li>Cancel anytime</li>'
)

# CHANGE 9
content = content.replace(
    '<p class="offer-card-label">Professional</p>\n          <h3>$149<span> / user / mo</span></h3>\n          <p class="offer-price-note">Everything in Basic, plus:</p>',
    '<p class="offer-card-label">Growth</p>\n          <h3>$2,500<span> / mo</span></h3>\n          <p class="offer-price-note">For businesses with 30–75 employees.</p>'
)

# CHANGE 10
content = content.replace(
    '<li>After-hours coverage</li>\n            <li>Priority response</li>\n            <li>Monthly security report</li>\n            <li>Dedicated account manager</li>',
    '<li>Up to 3 active automations maintained</li>\n            <li>1 new automation build per quarter</li>\n            <li>Monthly AI usage report</li>\n            <li>Dedicated account manager</li>'
)

# CHANGE 11
content = content.replace(
    '<div class="stat-number">&lt; 15 min</div>\n        <div class="stat-label">Average response time</div>\n        <div class="stat-desc">For all support requests during business hours</div>',
    '<div class="stat-number">30 days</div>\n        <div class="stat-label">To full AI governance</div>\n        <div class="stat-desc">From discovery call to documented AI policy, shadow audit, and M365 configuration</div>'
)

# CHANGE 12
content = content.replace(
    '<div class="stat-number">99.9%</div>\n        <div class="stat-label">Uptime guarantee</div>\n        <div class="stat-desc">Proactive monitoring keeps your team online</div>',
    '<div class="stat-number">100%</div>\n        <div class="stat-label">AI policy coverage</div>\n        <div class="stat-desc">Every client gets a documented AI acceptable use policy on day one</div>'
)

# CHANGE 13
content = content.replace(
    'You pay a fixed monthly fee per user. Doesn\'t matter how many support tickets you submit, how long calls take, or what we have to fix. Your bill is the same every month.',
    'You pay a fixed monthly fee per business — not per user. It doesn\'t matter if you add two people or ten. Your bill is the same every month. No surprise invoices, no per-seat charges, no break-fix fees.'
)

# CHANGE 14
content = content.replace(
    '6. Do you have a tested disaster recovery plan?',
    '6. Do you have a documented AI incident response plan?'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

