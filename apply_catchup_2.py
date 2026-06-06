import re

filepath = "/data/msp-site/shadow-ai-prevention-ontario.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# CHANGE 1
content = content.replace(
    """"name": "How much does a ransomware attack cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "One ransomware attack costs $50,000–$200,000 CAD to recover — including downtime, recovery, notification, legal, and reputational damage.\"""",
    """"name": "How much does an AI data breach cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A PIPEDA investigation can cost $50,000 or more in legal fees, fines, and remediation. For a regulated professional, an AI data leak can also trigger a Law Society or CPA disciplinary proceeding that puts their licence at risk.\""""
)

# CHANGE 2
content = content.replace(
    '"text": "Cybersecurity is built into all plans: Essentials $99/user/month, Professional $149/user/month, Complete $199/user/month. Threat detection, encryption, patching, compliance all included."',
    '"text": "AI governance is built into all plans: Foundation $1,500/month, Growth $2,500/month, Transform $4,500/month. Flat fee per business — not per user. AI policy, shadow AI audit, M365 configuration, and compliance documentation all included."'
)

# CHANGE 3
content = content.replace(
    """<h3>"Everything breaks at the worst time."</h3>
        <p>A server goes down on Friday afternoon. Your point-of-sale freezes mid-transaction. Your team can't get online. You're scrambling — and losing money every minute.</p>""",
    """<h3>"My team is using ChatGPT with client data and I found out by accident."</h3>
        <p>Employees paste contracts, financials, and client notes into public AI tools every day. You didn't authorize it. You don't know how much has already left the building.</p>"""
)

# CHANGE 4
content = content.replace(
    """<h3>"I never know what IT is going to cost."</h3>
        <p>Random invoices. Emergency callout fees. Hardware you didn't expect. IT feels like a bill that arrives with no warning and no explanation.</p>""",
    """<h3>"My cyber insurer sent a renewal form asking about AI governance. I don't have answers."</h3>
        <p>Insurers are now asking which AI tools your team uses, what policies are in place, and who is responsible. Businesses that can't answer are seeing premiums rise — or claims denied.</p>"""
)

# CHANGE 5
content = content.replace(
    """<h3>"I don't know if we're actually secure."</h3>
        <p>You've heard the horror stories — ransomware, phishing, stolen data. You don't know if it could happen to you, and honestly, you don't know who to ask.</p>""",
    """<h3>"A client asked me directly: what is your AI data handling policy?"</h3>
        <p>You didn't have a good answer. Neither does most of your competition — yet. The businesses that get ahead of this question will win the clients who ask it.</p>"""
)

# CHANGE 6
# Be careful here to only replace the li tag
content = content.replace(
    """<li>Priority Helpdesk</li>""",
    """<li>Priority support</li>"""
)

# CHANGE 7
content = content.replace(
    """<p class="offer-price-note">Everything in Basic, plus:</p>""",
    """<p class="offer-price-note">For businesses with 30–75 employees.</p>"""
)

# Replace Datto logo block
datto_block = r"<!-- Datto -->\s*<div class=\"partner-item\" title=\"Datto\">\s*<svg.*?>.*?</svg>\s*</div>"
content = re.sub(datto_block, "", content, flags=re.DOTALL)

# Replace Acronis logo block
acronis_block = r"<!-- Acronis -->\s*<div class=\"partner-item\" title=\"Acronis\">\s*<svg.*?>.*?</svg>\s*</div>"
content = re.sub(acronis_block, "", content, flags=re.DOTALL)

# Replace SentinelOne logo block
sentinelone_block = r"<!-- SentinelOne -->\s*<div class=\"partner-item\" title=\"SentinelOne\">\s*<svg.*?>.*?</svg>\s*</div>"
content = re.sub(sentinelone_block, "", content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Applied fixes to {filepath}")

