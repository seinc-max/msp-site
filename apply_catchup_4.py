import os

filepath = "/data/msp-site/blog/20-southern-ontario-shadow-ai-audits-2026.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

old1 = "<p>With flat-rate AI Compliance at $1,500/month, they would have paid $18,000 per year. But that proactive monitoring and DLP execution would have caught the unauthorized Copilot access three weeks earlier—before a server leak. M365 permission hardening would have shielded the HR director's payroll files from general staff query prompts. The liability would have been negated.</p>"
new1 = "<p>With flat-rate AI governance at $1,500/month, they would have paid $18,000 per year. But the shadow AI audit would have caught the unauthorized Copilot access months earlier — before any client data was exposed. M365 permission hardening would have shielded the HR director's payroll files from general staff query prompts. The liability would have been negated.</p>"

content = content.replace(old1, new1)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Applied files to {filepath}")
