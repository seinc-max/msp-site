import sys
import re

file_path = "/data/msp-site/cybersecurity-southern-ontario.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Title, Meta Description, Keywords
content = re.sub(r'<title>.*?</title>', '<title>Shadow AI Prevention & AI Data Security | Trueline IT</title>', content)
content = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Enterprise-grade AI data security and PIPEDA compliance for Southern Ontario businesses. Prevent employees from leaking confidential IP into public LLMs." />', content)
content = re.sub(r'<meta name="keywords" content=".*?" />', '<meta name="keywords" content="Shadow AI prevention, AI data security, PIPEDA AI compliance, stop ChatGPT data leaks, AI acceptable use policy Ontario" />', content)

# 2. Update Open Graph Data
content = re.sub(r'<meta property="og:title" content=".*?" />', '<meta property="og:title" content="Shadow AI Prevention & AI Data Security | Trueline IT" />', content)
content = re.sub(r'<meta property="og:description" content=".*?" />', '<meta property="og:description" content="Enterprise-grade AI data security. Prevent employees from leaking confidential IP into public LLMs." />', content)
content = re.sub(r'<meta name="twitter:title" content=".*?" />', '<meta name="twitter:title" content="Shadow AI Prevention & AI Data Security | Trueline IT" />', content)
content = re.sub(r'<meta name="twitter:description" content=".*?" />', '<meta name="twitter:description" content="Enterprise-grade AI data security. Prevent employees from leaking confidential IP into public LLMs." />', content)

# 3. Update Hero Section
content = content.replace(
    '<div class="hero-pre">Cybersecurity for Southern Ontario SMBs</div>', 
    '<div class="hero-pre">Shadow AI Prevention & AI Data Security</div>'
)
content = content.replace(
    '<h1>Is Your Data Safe<br>From Your Own Team?</h1>', 
    '<h1>Your Employees Are Leaking<br>Confidential Data to Public AI.</h1>'
)
content = content.replace(
    '<p class="hero-sub">In 2026, Southern Ontario professional services (law, accounting, finance) are prime targets for ransomware. One click on a phishing link can compromise years of client data, violating PIPEDA and threatening your license to operate. Traditional antivirus isn\'t enough anymore. Trueline IT delivers enterprise-grade endpoint security, real-time threat monitoring, staff training, and rapid incident response — built into every managed IT plan.</p>', 
    '<p class="hero-sub">Traditional cybersecurity focuses on keeping hackers out. The new threat is your own team feeding confidential client IP, financial records, and PII into unapproved public AI tools like ChatGPT just to get their work done faster. This is Shadow AI, and it explicitly violates PIPEDA and exposes you to massive liability.</p>'
)

# 4. Update Stat Bar
content = content.replace(
    '<strong style="color: #1a2744;">60% of small businesses close within 6 months</strong> of a significant data breach or ransomware attack. — Inc. Magazine',
    '<strong style="color: #1a2744;">76% of employees admit to using unauthorized AI tools at work.</strong> Most of their managers don\'t know. — IBM Institute for Business Value, 2025'
)

# 5. Update Pain Points
content = content.replace(
    '<p class="section-label">The Cybersecurity Reality Set for Ontario</p>',
    '<p class="section-label">The Shadow AI Reality Set for Ontario</p>'
)
content = content.replace(
    '<h2 class="section-title">Ontario businesses are targeted hourly.</h2>',
    '<h2 class="section-title">Your Data is Training Someone Else\'s Model.</h2>'
)
content = content.replace(
    '<p class="section-sub">Phishing, unpatched software, and weak passwords are the entry points. But the real cost isn\'t just IT recovery — it\'s reputational damage and regulatory fines from the Information and Privacy Commissioner of Ontario (IPC).</p>',
    '<p class="section-sub">If you do not provide a structured, approved, and private AI environment for your team, they will circumvent you to use free public versions. The data they enter into those prompts becomes training data for public models.</p>'
)

content = content.replace(
    '<h3>"We just have basic antivirus."</h3>',
    '<h3>"We just blocked ChatGPT."</h3>'
)
content = content.replace(
    '<p>Legacy antivirus only catches known threats. Modern attacks use compromised credentials and silent lateral movement. You need an active SOC monitoring anomalies, 24/7.</p>',
    '<p>Blindly banning AI doesn\'t stop its use. It just drives it underground. Employees will access it on personal devices or bypass network filters to keep their productivity edge.</p>'
)

content = content.replace(
    '<h3>"Our cyber insurance requires MFA."</h3>',
    '<h3>"We don\'t even know what they use."</h3>'
)
content = content.replace(
    '<p>Insurance providers are denying claims if security controls aren\'t actively maintained. We deploy the exact controls (MFA, EDR, backups) underwriters demand.</p>',
    '<p>When a team member uses an unsanctioned tool to summarize a contract or draft a proposal, that PII leaves your secure perimeter instantly. Shadow AI audits reveal this invisible footprint.</p>'
)

content = content.replace(
    '<h3>"What if we get breached today?"</h3>',
    '<h3>"What happens if client data leaks?"</h3>'
)
content = content.replace(
    '<p>Most SMBs have no formal incident response plan. Every second of downtime costs money. Our team acts immediately to isolate threats and begin the recovery from verified backups.</p>',
    '<p>If confidential information is ingested by a public LLM, your business is directly liable for the PIPEDA breach. Waiting for a disaster isn\'t a strategy.</p>'
)

# 6. Update Offer
content = content.replace(
    '<div class="offer-badge">Advanced Cybersecurity</div>',
    '<div class="offer-badge">The Trueline IT Service</div>'
)
content = content.replace(
    '<h2 class="section-title">End-to-End Threat Protection & Compliance</h2>',
    '<h2 class="section-title">AI governance and automation — handled. One flat monthly fee.</h2>'
)
content = content.replace(
    '<p class="section-sub">We deploy the same security stack used by Fortune 500s, scaled and priced for Guelph, Hamilton, and Burlington SMBs. SentinelOne EDR, zero-trust access, spam filtering, phishing simulations, and compliance tracking.</p>',
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
    '<h2 class="section-title">Cybersecurity Implementation</h2>',
    '<h2 class="section-title">AI Deployment Process</h2>'
)
content = content.replace(
    '<p class="section-sub">Risk Assessment → Deploy Defenses → Continuous Monitoring. We protect Ontario businesses invisibly, so you can work securely without friction.</p>',
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
content = content.replace('<h2 class="section-title">The Cost of Doing Nothing</h2>', '<h2 class="section-title">Numbers we stand behind.</h2>')
content = content.replace('<p class="section-sub">Ransomware payouts in Canada averaged $1.3M in 2026. Data breaches bring PIPEDA fines and reputational ruin. Proactive cybersecurity is vastly cheaper than disaster recovery.</p>', '<p class="section-sub">AI without governance is a massive liability. We fix the foundation so you can scale safely.</p>')

content = content.replace('<div class="stat-label">Average response time</div>', '<div class="stat-label">To full AI governance</div>')
content = content.replace('<div class="stat-desc">For all support requests during business hours</div>', '<div class="stat-desc">From discovery call to documented AI policy and shadow audit</div>')

content = content.replace('<div class="stat-label">Uptime guarantee</div>', '<div class="stat-label">AI policy coverage</div>')
content = content.replace('<div class="stat-desc">Proactive monitoring keeps your team online</div>', '<div class="stat-desc">Every client gets a documented AI acceptable use policy on day one</div>')

content = content.replace('<div class="stat-label">Surprise invoices</div>', '<div class="stat-label">Flat fee</div>')
content = content.replace('<div class="stat-desc">Flat monthly rate — you always know what you\'ll pay</div>', '<div class="stat-desc">Per business, per month. No per-seat billing tricks.</div>')


# 9. FAQ Section
content = content.replace('<h2 class="section-title text-center">Cybersecurity Questions for Ontario SMBs</h2>', '<h2 class="section-title text-center">Common Questions About AI Governance</h2>')

content = content.replace('<summary>What is required for PIPEDA compliance in Ontario?</summary>', '<summary>What is a Shadow AI Audit?</summary>')
content = content.replace('<p class="faq-answer">Reasonable safeguards to protect personal information. This practically means enforcing access controls, encrypting data at rest/transit, retaining activity logs, and managing vendor risk. Trueline IT configures these frameworks directly in M365.</p>', '<p class="faq-answer">It\'s a structured review of every AI tool your team is using, how it handles your data, and whether your current setup creates regulatory or insurance exposure. We deliver it as a written report with a risk score and a recommended action plan.</p>')

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

