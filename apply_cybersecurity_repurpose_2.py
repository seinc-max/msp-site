import sys

file_path = "/data/msp-site/cybersecurity-southern-ontario.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix Hero h1
content = content.replace(
    "<h1>Enterprise Cybersecurity<br>Without the Enterprise Cost.</h1>", 
    "<h1>Your Employees Are Leaking<br>Confidential Data to Public AI.</h1>"
)

# Fix Shadow AI reality
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

content = content.replace(
    '<p class="section-sub">Ransomware payouts in Canada averaged $1.3M in 2026. Data breaches bring PIPEDA fines and reputational ruin. Proactive cybersecurity is vastly cheaper than disaster recovery.</p>',
    '<p class="section-sub">AI without governance is a massive liability. We fix the foundation so you can scale safely.</p>'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

