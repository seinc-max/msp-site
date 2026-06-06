import sys
import glob

# Ensure Numbers we stand behind was applied instead of the "What trueline IT Delivers for X". 
import re

files = glob.glob("/data/msp-site/ai-governance-*.html")

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Stat 2 label
    content = content.replace("Per business, per month", "Flat fee")
    # Stat 1 label
    content = content.replace("Average deployment time", "To full AI governance")
    content = content.replace("From kickoff to full AI Acceptable Use Policy", "From discovery call to documented AI policy, shadow audit, and M365 configuration")
    content = content.replace("Data Privacy", "AI policy coverage")
    content = content.replace("Zero client data used to train public AI models", "Every client gets a documented AI acceptable use policy on day one")
    content = re.sub(r'What Trueline IT Delivers for [a-zA-Z-\s]+', 'Numbers we stand behind.', content)
    content = content.replace("Get in touch", "Start here")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

