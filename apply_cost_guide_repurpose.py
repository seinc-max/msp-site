import sys
import re

file_path = "/data/msp-site/it-cost-guide-ontario.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Title, Meta Description, Keywords
content = re.sub(r'<title>.*?</title>', '<title>The ROI of AI Automation vs. The Cost of Shadow AI | Trueline IT</title>', content)
content = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Compare the cost of manual administrative labor, compliance fines, and Shadow AI liability against flat-rate AI Governance and Automation plans." />', content)
content = re.sub(r'<meta name="keywords" content=".*?" />', '<meta name="keywords" content="AI automation ROI Ontario, shadow AI cost, PIPEDA fines AI, AI governance pricing, cost of manual tasks" />', content)

# 2. Update Open Graph Data
content = re.sub(r'<meta property="og:title" content=".*?" />', '<meta property="og:title" content="The ROI of AI Automation vs. The Cost of Shadow AI | Trueline IT" />', content)
content = re.sub(r'<meta property="og:description" content=".*?" />', '<meta property="og:description" content="Compare the cost of manual labor, PIPEDA compliance fines, and Shadow AI liability against flat-rate AI Governance plans." />', content)
content = re.sub(r'<meta name="twitter:title" content=".*?" />', '<meta name="twitter:title" content="The ROI of AI Automation vs. The Cost of Shadow AI | Trueline IT" />', content)
content = re.sub(r'<meta name="twitter:description" content=".*?" />', '<meta name="twitter:description" content="Compare the cost of manual labor, PIPEDA compliance fines, and Shadow AI liability against flat-rate AI Governance plans." />', content)

# 3. Update Hero Section
content = content.replace(
    '<div class="hero-pre">IT Cost Guide for Ontario Business Owners</div>', 
    '<div class="hero-pre">AI ROI & Liability Guide for Ontario Businesses</div>'
)
content = content.replace(
    '<h1>Stop Guessing What Your<br>IT Should Cost.</h1>', 
    '<h1>Stop Ignoring the Hidden Cost<br>of Shadow AI.</h1>'
)
content = content.replace(
    '<p class="hero-sub">Most businesses have no idea if they are overpaying for technology or dangerously under-investing. We built this guide so Southern Ontario business owners can finally understand real market rates for IT support, security, and compliant cloud infrastructure. Calculate your true total cost of ownership and discover the ROI of moving to a predictable flat-rate model.</p>', 
    '<p class="hero-sub">Most professional services businesses wildly underestimate two metrics: The money they are setting on fire by paying humans to do manual data entry, and the catastrophic liability they incur when those humans use unsafe public AI tools to speed up their work. In this guide, we break down the financial reality of AI governance, the cost of non-compliance, and the massive ROI of workflow automation.</p>'
)

# 4. Update Stat Bar
content = content.replace(
    '<strong style="color: #1a2744;">SMBs without managed IT spend up to 40% more</strong> on technology support costs than those with a dedicated provider. — BizTech',
    '<strong style="color: #1a2744;">The average knowledge worker wastes 3 hours a day</strong> on manual administrative tasks that can be fully automated using safe LLMs. — McKinsey'
)

# 5. Update Pain Points
content = content.replace(
    '<p class="section-label">The IT Cost Reality for Ontario Businesses</p>',
    '<p class="section-label">The Financial Reality of Non-Governance</p>'
)
content = content.replace(
    '<h2 class="section-title">The True Cost of Reactive IT.</h2>',
    '<h2 class="section-title">The True Cost of Reactive Automation.</h2>'
)
content = content.replace(
    '<p class="section-sub">Paying for "break-fix" IT feels cheaper until a server goes down, an employee gets phished, or a critical update is missed. Unpredictable invoices destroy budget forecasting. Real IT strategy transforms technology from a variable liability into a fixed, predictable utility.</p>',
    '<p class="section-sub">Turning a blind eye to AI feels cheaper until a major client finds out their PII was used to train a public model, or the IPC fines you for a PIPEDA violation. True AI strategy transforms generative tech from a massive liability into an auditable competitive advantage.</p>'
)

content = content.replace(
    '<h3>"Everything breaks at the worst time."</h3>',
    '<h3>"Manual work is bleeding margin."</h3>'
)
content = content.replace(
    '<p>A server goes down on Friday afternoon. Your point-of-sale freezes mid-transaction. Your team can\'t get online. You\'re scrambling — and losing money every minute.</p>',
    '<p>You are paying six-figure salaries for experts who spend 30% of their week formatting documents, reconciling emails from CRM systems, and manually rewriting reports.</p>'
)

content = content.replace(
    '<h3>"I never know what IT is going to cost."</h3>',
    '<h3>"Shadow AI liability."</h3>'
)
content = content.replace(
    '<p>Random invoices. Emergency callout fees. Hardware you didn\'t expect. IT feels like a bill that arrives with no warning and no explanation.</p>',
    '<p>Your highest performing employees are using ChatGPT right now to do their jobs. They are uploading confidential files. The cost of a breach dwarfs your annual software budget.</p>'
)

content = content.replace(
    '<h3>"I don\'t know if we\'re actually secure."</h3>',
    '<h3>"Fake enterprise deployments."</h3>'
)
content = content.replace(
    '<p>You\'ve heard the horror stories — ransomware, phishing, stolen data. You don\'t know if it could happen to you, and honestly, you don\'t know who to ask.</p>',
    '<p>Enterprise AI consultants quote $50K for "roadmaps." We skip the fluff and deploy fully audited Copilot and secure private models for a predictable flat monthly fee.</p>'
)

# 6. Update Offer
content = content.replace(
    '<div class="offer-badge">Predictable IT Budgeting</div>',
    '<div class="offer-badge">The Trueline IT Service</div>'
)
content = content.replace(
    '<h2 class="section-title">Stop the Billing Surprises. Switch to Flat Rate.</h2>',
    '<h2 class="section-title">AI governance and automation — handled. One flat monthly fee.</h2>'
)
content = content.replace(
    '<p class="section-sub">We align your IT strategy with your business goals. For a fixed monthly fee per user, you get unlimited helpdesk support, proactive monitoring, enterprise-grade cybersecurity, and fully managed backups. No spikes, no hidden fees. Just IT that works.</p>',
    '<p class="section-sub">No per-seat billing. No enterprise consultant invoices. Every plan includes a documented AI Acceptable Use Policy, shadow AI audit, and ongoing compliance management. Automation builds included from Growth tier.</p>'
)

content = content.replace('<li>Unlimited helpdesk support — call, email, or chat</li>', '<li>AI Acceptable Use Policy — created and maintained</li>')
content = content.replace('<li>Cybersecurity essentials included</li>', '<li>Shadow AI audits — full visibility into workforce tools</li>')
content = content.replace('<li>Automated backups &amp; disaster recovery</li>', '<li>Every client gets a documented AI acceptable use policy on day one</li>')
# Drop other bullet points by just replacing the whole block or keeping them as standard bullet structure

# Pricing Cards Update
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

# 7. How it works
content = content.replace(
    '<h2 class="section-title">The Path to Predictable IT</h2>',
    '<h2 class="section-title">AI Deployment Process</h2>'
)
content = content.replace(
    '<p class="section-sub">Assessment → Stabilization → Optimization. We transition Southern Ontario businesses from reactive chaos to proactive utility in 30 days.</p>',
    '<p class="section-sub">Shadow Audit → Acceptable Use Policy → Permissions Hardening → Safe AI Deployment. Most businesses are secured within 4 weeks.</p>'
)

content = content.replace(
    '<p>A 30-minute chat to understand your business, your current setup, and where we can help most.</p>',
    '<p>A 30-minute call to understand your business, your AI exposure, and which tier fits your situation. No sales pitch — just a diagnosis.</p>'
)
# Assuming steps 2 and 3 need adjustment too:
content = content.replace('<p>We put together a tailored plan with flat-rate pricing — no jargon, no surprises.</p>', '<p>We audit your M365 permissions, look for data leakage, and draft an Acceptable Use Policy.</p>')
content = content.replace('<p>Onboarding, setup, monitoring — all handled. You get back to running your business.</p>', '<p>We safely deploy Copilot or private LLMs, train your staff, and actively monitor compliance.</p>')


# 8. Stats
content = content.replace('<h2 class="section-title">The True Cost of IT Issues</h2>', '<h2 class="section-title">Numbers we stand behind.</h2>')
content = content.replace('<p class="section-sub">Unmanaged environments suffer 65% more downtime. Hourly intervention rates peak over $200/hr. Real IT strategy saves money over 12 months by preventing the initial disaster.</p>', '<p class="section-sub">AI without governance is a massive liability. We fix the foundation so you can scale safely.</p>')

content = content.replace('<div class="stat-label">Average response time</div>', '<div class="stat-label">To full AI governance</div>')
content = content.replace('<div class="stat-desc">For all support requests during business hours</div>', '<div class="stat-desc">From discovery call to documented AI policy and shadow audit</div>')

content = content.replace('<div class="stat-label">Uptime guarantee</div>', '<div class="stat-label">AI policy coverage</div>')
content = content.replace('<div class="stat-desc">Proactive monitoring keeps your team online</div>', '<div class="stat-desc">Every client gets a documented AI acceptable use policy on day one</div>')

content = content.replace('<div class="stat-label">Surprise invoices</div>', '<div class="stat-label">Flat fee</div>')
content = content.replace('<div class="stat-desc">Flat monthly rate — you always know what you\'ll pay</div>', '<div class="stat-desc">Per business, per month. No per-seat billing tricks.</div>')


# 9. FAQ Section
content = content.replace('<h2 class="section-title text-center">IT Cost Questions for Ontario Businesses</h2>', '<h2 class="section-title text-center">Common Questions About AI Governance</h2>')

content = content.replace('<summary>How much should an Ontario SMB budget for IT?</summary>', '<summary>What is a Shadow AI Audit?</summary>')
content = content.replace('<p class="faq-answer">Industry standard is 3-5% of total revenue. For a professional service business with 25 employees, engaging a flat-rate Managed Service Provider is usually 40% cheaper than hiring a single internal tier-1 technician.</p>', '<p class="faq-answer">It\'s a structured review of every AI tool your team is using, how it handles your data, and whether your current setup creates regulatory or insurance exposure. We deliver it as a written report with a risk score and a recommended action plan.</p>')

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
content = content.replace('Is your Southern Ontario business protected? Find out in 15 minutes. Book your free Trueline IT Health Score', 'Are you unprotected against Shadow AI data leaks? Find out in 15 minutes. Book your free Trueline IT Audit')


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

