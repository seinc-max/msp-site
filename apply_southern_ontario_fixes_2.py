import sys
import re

file_path = "/data/msp-site/ai-governance-southern-ontario.html"

# We must still find and replace the rest of the text mapping from the original list 
# Average deployment time -> To full AI governance
# From kickoff to full AI Acceptable Use Policy -> From discovery call to documented AI policy, shadow audit, and M365 configuration
# Data Privacy -> AI policy coverage
# Zero client data used to train public AI models -> Every client gets a documented AI acceptable use policy on day one

changes_2 = [
    ("Average response time", "To full AI governance"),
    ("Average onboarding", "From discovery call to documented AI policy, shadow audit, and M365 configuration"),
    ("Compliance Focus", "AI policy coverage"),
    ("Automated backups &amp; disaster recovery", "Every client gets a documented AI acceptable use policy on day one"),
    ("We partner with Southern Ontario professional services (legal, accounting, financial). If you handle confidential client IP and have strict privacy requirements, our frameworks are designed for you.", "We specialise in professional services businesses with 15 to 150 employees — legal, accounting, financial advisory, healthcare, and consulting. If you handle confidential client data and have no internal IT department, you're exactly who we built this for."),
    ("Ready to secure your Southern Ontario business?", "Find out exactly where your business is exposed.")
]

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

for old_text, new_text in changes_2:
    if old_text in content:
        content = content.replace(old_text, new_text)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

