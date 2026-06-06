import sys
import re

file_path = "/data/msp-site/ai-governance-southern-ontario.html"

# We must still find and replace the rest of the text mapping from the original list 

changes_2 = [
    ("Ready to stop worrying about IT?", "Find out exactly where your business is exposed."),
    ("AI Governance for Southern Ontario", "AI Governance & Automation for Professional Services Businesses in Southern Ontario")
]

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

for old_text, new_text in changes_2:
    if old_text in content:
        content = content.replace(old_text, new_text)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

