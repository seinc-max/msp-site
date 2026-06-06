import sys
import re

file_path = "/data/msp-site/microsoft-365-ontario-smbs.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Title, Meta Description, Keywords
content = re.sub(r'<title>.*?</title>', '<title>Safe Microsoft Copilot Deployment & M365 Security | Trueline IT</title>', content)
content = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Deploy Microsoft Copilot safely in your Ontario business. M365 permission audits, Shadow AI prevention, and DLP configurations for professional services." />', content)
content = re.sub(r'<meta name="keywords" content=".*?" />', '<meta name="keywords" content="Microsoft Copilot setup Ontario, M365 safe AI, Shadow AI prevention, Microsoft 365 permissions audit, legal AI compliance" />', content)

# 2. Update Open Graph Data
content = re.sub(r'<meta property="og:title" content=".*?" />', '<meta property="og:title" content="Safe Microsoft Copilot Deployment & M365 Security | Trueline IT" />', content)
content = re.sub(r'<meta property="og:description" content=".*?" />', '<meta property="og:description" content="Deploy Microsoft Copilot safely. Prevent data leaks with M365 permission audits, DLP configurations, and Shadow AI prevention." />', content)
content = re.sub(r'<meta name="twitter:title" content=".*?" />', '<meta name="twitter:title" content="Safe Microsoft Copilot Deployment & M365 Security | Trueline IT" />', content)
content = re.sub(r'<meta name="twitter:description" content=".*?" />', '<meta name="twitter:description" content="Deploy Microsoft Copilot safely. Prevent data leaks with M365 permission audits, DLP configurations, and Shadow AI prevention." />', content)

# 3. Update Hero Section
content = content.replace(
    '<div class="hero-pre">Microsoft 365 for Ontario SMBs</div>', 
    '<div class="hero-pre">Microsoft Copilot & M365 Security</div>'
)
content = content.replace(
    '<h1>Unlock the Full Power<br>of Microsoft 365.</h1>', 
    '<h1>Deploy Microsoft Copilot<br>Without Leaking Data.</h1>'
)
content = content.replace(
    '<p class="hero-sub">In our 2026 assessment of 20 Southern Ontario businesses, 78% had no verified Microsoft 365 security configuration. Their users weren\'t protected. Data wasn\'t backed up. Compliance was missing. Trueline IT delivers Microsoft 365 setup, security hardening, user training, and compliance as standard. Full stack optimization — Teams, SharePoint, OneDrive, Defender, compliance controls. No configuration guesswork.</p>', 
    '<p class="hero-sub">Microsoft 365 is a trojan horse for data leaks if Copilot is turned on without proper permission audits. If you activate Copilot right now, every employee can instantly surface confidential HR, financial, and client files they shouldn\'t see. We secure your tenant with strict Data Loss Prevention (DLP) and permission audits before AI goes live.</p>'
)

# 4. Update Stat Bar
content = content.replace(
    '<strong style="color: #1a2744;">SMBs without managed IT spend up to 40% more</strong> on technology support costs than those with a dedicated provider. — BizTech',
    '<strong style="color: #1a2744;">76% of employees admit to using unauthorized AI tools at work.</strong> Most of their managers don\'t know. — IBM Institute for Business Value, 2025'
)

# 5. Update Pain Points
content = content.replace(
    '<p class="section-label">The Microsoft 365 Reality for Ontario Businesses</p>',
    '<p class="section-label">The AI Reality for Ontario Businesses</p>'
)
content = content.replace(
    '<h2 class="section-title">78% of Ontario Businesses Misconfig Microsoft 365.</h2>',
    '<h2 class="section-title">Copilot Exposed Your Permissions Mess.</h2>'
)
content = content.replace(
    '<p class="section-sub">Microsoft 365 is powerful but complex. Most Ontario SMBs in Guelph, Hamilton, Burlington activate it but never optimize it. Security is left at defaults. Backups aren\'t verified. Users aren\'t trained. Compliance is forgotten. This guide helps SMBs unlock the full value of M365 — securely.</p>',
    '<p class="section-sub">Microsoft Copilot respects your existing M365 permissions. The problem? Most businesses have terrible internal permissions. Folders are shared globally. Confidential HR spreadsheets are accessible via search. Copilot will instantly find and summarize this data for any employee who asks. You must fix the foundation before turning on the AI.</p>'
)

content = content.replace(
    '<h3>"Everything breaks at the worst time."</h3>',
    '<h3>"Employees seeing salary data."</h3>'
)
content = content.replace(
    '<p>A server goes down on Friday afternoon. Your point-of-sale freezes mid-transaction. Your team can\'t get online. You\'re scrambling — and losing money every minute.</p>',
    '<p>When Copilot is enabled in an un-audited tenant, a simple prompt like "summarize the 2026 payroll spreadsheet" can bypass internal department silos instantly.</p>'
)

content = content.replace(
    '<h3>"I never know what IT is going to cost."</h3>',
    '<h3>"Shadow AI leaking client data."</h3>'
)
content = content.replace(
    '<p>Random invoices. Emergency callout fees. Hardware you didn\'t expect. IT feels like a bill that arrives with no warning and no explanation.</p>',
    '<p>If you don\'t provide a safe, sanctioned AI tool like Copilot, employees will paste confidential client documents into public ChatGPT to get their work done faster.</p>'
)

content = content.replace(
    '<h3>"I don\'t know if we\'re actually secure."</h3>',
    '<h3>"Compliance violations."</h3>'
)
content = content.replace(
    '<p>You\'ve heard the horror stories — ransomware, phishing, stolen data. You don\'t know if it could happen to you, and honestly, you don\'t know who to ask.</p>',
    '<p>The Law Society of Ontario and PIPEDA mandate strict control over client data. Using unapproved AI tools without Data Loss Prevention (DLP) violates these policies.</p>'
)

# 6. Update Offer
content = content.replace(
    '<div class="offer-badge">Microsoft 365 Optimization</div>',
    '<div class="offer-badge">The Trueline IT Service</div>'
)
content = content.replace(
    '<h2 class="section-title">Complete Microsoft 365 Setup, Security & Training</h2>',
    '<h2 class="section-title">AI governance and automation — handled. One flat monthly fee.</h2>'
)
content = content.replace(
    '<p class="section-sub">Tenant hardening. Security baseline. Defender endpoint protection. Teams governance. OneDrive backup verification. SharePoint permissions. User training. Compliance audits. Migration support. All included.</p>',
    '<p class="section-sub">No per-seat billing. No surprise invoices. Every plan includes a documented AI Acceptable Use Policy, shadow AI audit, and ongoing compliance management. Automation builds included from Growth tier.</p>'
)
# Fix offer list items
content = content.replace('<li>Unlimited helpdesk support — call, email, or chat</li>', '<li>AI Acceptable Use Policy — created and maintained</li>')
content = content.replace('<li>Cybersecurity essentials included</li>', '<li>Shadow AI audits — full visibility into workforce tools</li>')
content = content.replace('<li>Automated backups &amp; disaster recovery</li>', '<li>Every client gets a documented AI acceptable use policy on day one</li>')


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


# 7. Update How it Works
content = content.replace(
    '<h2 class="section-title">Microsoft 365 Implementation</h2>',
    '<h2 class="section-title">AI Deployment Process</h2>'
)
content = content.replace(
    '<p class="section-sub">Assessment → Security hardening → User training. Migration support if needed. Most Ontario businesses fully M365-optimized within 3–4 weeks.</p>',
    '<p class="section-sub">Shadow Audit → Acceptable Use Policy → Permissions Hardening → Safe AI Deployment. Most businesses are secured within 4 weeks.</p>'
)

content = content.replace(
    '<p>A 30-minute chat to understand your business, your current setup, and where we can help most.</p>',
    '<p>A 30-minute call to understand your business, your AI exposure, and which tier fits your situation. No sales pitch — just a diagnosis.</p>'
)
# Assuming steps 2 and 3 need adjustment too:
content = content.replace('<p>We put together a tailored plan with flat-rate pricing — no jargon, no surprises.</p>', '<p>We audit your M365 permissions, look for data leakage, and draft an Acceptable Use Policy.</p>')
content = content.replace('<p>Onboarding, setup, monitoring — all handled. You get back to running your business.</p>', '<p>We safely deploy Copilot or private LLMs, train your staff, and actively monitor compliance.</p>')


# 8. By the Numbers (Stats)
content = content.replace('<h2 class="section-title">Microsoft 365 Security Metrics</h2>', '<h2 class="section-title">Numbers we stand behind.</h2>')
content = content.replace('<p class="section-sub">78% of Ontario businesses never verify M365 backups. 85% have no endpoint protection enabled. 100% lack formal compliance documentation. Trueline IT fixes all three as standard.</p>', '<p class="section-sub">AI without governance is a massive liability. We fix the foundation so you can scale safely.</p>')

content = content.replace('<div class="stat-label">Average response time</div>', '<div class="stat-label">To full AI governance</div>')
content = content.replace('<div class="stat-desc">For all support requests during business hours</div>', '<div class="stat-desc">From discovery call to documented AI policy and shadow audit</div>')

content = content.replace('<div class="stat-label">Uptime guarantee</div>', '<div class="stat-label">AI policy coverage</div>')
content = content.replace('<div class="stat-desc">Proactive monitoring keeps your team online</div>', '<div class="stat-desc">Every client gets a documented AI acceptable use policy on day one</div>')

content = content.replace('<div class="stat-label">Surprise invoices</div>', '<div class="stat-label">Flat fee</div>')
content = content.replace('<div class="stat-desc">Flat monthly rate — you always know what you\'ll pay</div>', '<div class="stat-desc">Per business, per month. No per-seat billing tricks.</div>')


# 9. FAQ Section
content = content.replace('<h2 class="section-title text-center">Microsoft 365 Questions for Ontario Businesses</h2>', '<h2 class="section-title text-center">Common Questions About AI Governance</h2>')

content = content.replace('<summary>What is Microsoft 365 security baseline for Ontario compliance?</summary>', '<summary>What is a Shadow AI Audit?</summary>')
content = content.replace('<p class="faq-answer">Multi-factor authentication. Conditional access policies. Defender for cloud apps. Sensitivity labels. Retention policies. Legal hold. DLP (data loss prevention). Audit logging. Threat intelligence. Trueline IT implements all for Ontario SMBs.</p>', '<p class="faq-answer">It\'s a structured review of every AI tool your team is using, how it handles your data, and whether your current setup creates regulatory or insurance exposure. We deliver it as a written report with a risk score and a recommended action plan.</p>')

content = content.replace('<p class="faq-answer">You pay a fixed monthly fee per user. Doesn\'t matter how many support tickets you submit, how long calls take, or what we have to fix. Your bill is the same every month.</p>', '<p class="faq-answer">You pay a fixed monthly fee — not per user. It doesn\'t matter if you add two people or ten. Your bill is the same every month. No surprise invoices, no per-seat charges, no break-fix fees.</p>')

content = content.replace('<summary>What if we already have some IT in place?</summary>', '<summary>My team is already using ChatGPT or Copilot secretly. What should we do?</summary>')
content = content.replace('<p class="faq-answer">No problem. We do a full assessment during onboarding and work with what you have. If something needs to change, we\'ll tell you plainly and give you options.</p>', '<p class="faq-answer">Even better. We audit what you already have, identify what\'s creating risk, configure what\'s safe, and shut down what isn\'t. You keep the tools your team loves — just without the liability.</p>')

content = content.replace('<summary>How fast do you respond when something breaks?</summary>', '<summary>How fast do you respond to issues?</summary>')
content = content.replace('<p class="faq-answer">Critical issues get a technician on it within 15 minutes. For routine requests, we aim to respond within a few hours during business hours. You\'ll always hear back from a real person.</p>', '<p class="faq-answer">For AI policy questions, compliance queries, and automation support we respond within one business day. For urgent issues we respond within 15 minutes during business hours. You will always hear back from a real person who knows your business.</p>')

content = content.replace('<summary>Is there a contract?</summary>', '<summary>Does Trueline IT force businesses into restrictive long-term contracts?</summary>')
content = content.replace('<p class="faq-answer">Month-to-month. We earn your business every month. If you\'re not happy, you can cancel with 30 days notice — no penalties, no drama.</p>', '<p class="faq-answer">Month-to-month. We earn your business every month. If you\'re not happy, you can cancel with 30 days notice — no penalties, no drama.</p>')

# 10. Contact Section
content = content.replace('<p class="section-label">Get in touch</p>', '<p class="section-label">Start here</p>')
content = content.replace('<h2>Ready to stop worrying about IT?</h2>', '<h2>Find out exactly where your business is exposed.</h2>')
content = content.replace('<p class="contact-sub">Tell us a bit about your business and we\'ll be in touch within one business day.</p>', '<p class="contact-sub">Book a 30-minute call. We will assess your AI exposure, answer your questions, and tell you exactly what needs to be done — no sales pitch, no obligation.</p>')


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

