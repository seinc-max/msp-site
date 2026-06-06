import os

files = [
    "index.html",
    "about.html",
    "privacy.html",
    "terms.html",
    "audit-confirmed.html",
    "ai-governance-burlington.html",
    "ai-governance-hamilton.html",
    "ai-governance-guelph.html",
    "ai-governance-waterloo.html",
    "ai-governance-cambridge.html",
    "ai-governance-kitchener-waterloo.html",
    "ai-automation-roi-guide.html",
    "ai-exposure-score.html",
    "safe-copilot-deployment.html",
    "shadow-ai-prevention-ontario.html",
    "ai-governance-ontario.html"
]

base_dir = "/data/msp-site"

fix_a_old = "Your dedicated IT team — without the cost of hiring one. Flat-rate support, no surprises, starting at $99/user/mo."
fix_a_new = "Trueline IT helps Southern Ontario professional services businesses govern AI risk and automate operations — documented AI policy, shadow AI audit, and ongoing compliance management for a flat monthly fee."

fix_b_old = "Unlimited helpdesk, proactive monitoring, backups, and cybersecurity — flat rate per user per month."
fix_b_new = "AI governance, shadow AI audits, Copilot compliance, and secure automation — flat monthly fee per business."

fix_c_old = "Flat-rate AI governance, Copilot compliance, and secure automation forsecurity — flat rate per user per month."
fix_c_new = "Flat-rate AI governance, Copilot compliance, and secure automation for professional services — flat monthly fee per business."

fix_d_old = '"unitText": "per user per month"'
fix_d_new = '"unitText": "per business per month"'

for file_name in files:
    file_path = os.path.join(base_dir, file_name)
    if not os.path.exists(file_path):
        print(f"Skipping {file_name}: not found")
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    content = content.replace(fix_a_old, fix_a_new)
    content = content.replace(fix_b_old, fix_b_new)
    content = content.replace(fix_c_old, fix_c_new)
    content = content.replace(fix_d_old, fix_d_new)

    if content != original_content:
        print(f"Updated {file_name}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Done")
