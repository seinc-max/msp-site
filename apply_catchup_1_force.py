import re

filepath = "/data/msp-site/ai-governance-ontario.html"

# The issue was spacing in the ul li element
old_text = """<li>Unlimited helpdesk — 15-min response guarantee</li>
        <li>24/7 monitoring and proactive maintenance</li>
        <li>Cybersecurity — endpoint protection included</li>
        <li>Microsoft 365 management and support</li>
        <li>Automated backups with tested recovery</li>
        <li>Monthly IT health report</li>"""
        
new_text = """<li>AI Acceptable Use Policy — created and maintained</li>
        <li>Quarterly shadow AI audit</li>
        <li>Microsoft 365 and Copilot AI configuration</li>
        <li>Insurer-ready compliance documentation</li>
        <li>1 active automation maintained</li>
        <li>Monthly 30-minute review call</li>"""

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(old_text, new_text)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Forced replace for pricing features")
