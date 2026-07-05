import re

files_changes = {
    "/data/msp-site/about.html": [
        ("Your outsourced IT department — without the overhead.", "Your Sovereign Automation & Governance Partners — without the overhead.")
    ],
    "/data/msp-site/shadow-ai-prevention-ontario.html": [
        ('<p class="offer-card-label">Scale</p>\n          <h3>$4,000<span> / mo</span></h3>', '<p class="offer-card-label">Transform</p>\n          <h3>$4,500<span> / mo</span></h3>'),
        ("1 Custom Automation Build /mo", "1 New Custom Enterprise Pipeline Build per quarter (Safely link apps like Xero, DocuSign, and CRMs with local transit encryption)"),
        ("3 Custom Automation Builds /mo", "Dedicated Private Core Environment (Closed-loop processing for voice, financial ledger, and legal registries)"),
        ("How Cybersecurity Implementation Works", "How Sovereign Infrastructure Implementation Works"),
        ("Cybersecurity Metrics for Southern Ontario Businesses", "Sovereign Infrastructure Metrics for Southern Ontario Businesses"),
        ("Cybersecurity Questions for Southern Ontario Business Owners", "Sovereign Infrastructure Questions for Southern Ontario Business Owners")
    ],
    "/data/msp-site/safe-copilot-deployment.html": [
        ('<p class="offer-card-label">Compliance</p>\n          <h3>$1,500<span> / mo</span></h3>', '<p class="offer-card-label">Foundation</p>\n          <h3>$1,500<span> / mo</span></h3>'),
        ('<p class="offer-card-label">Scale</p>\n          <h3>$4,000<span> / mo</span></h3>', '<p class="offer-card-label">Transform</p>\n          <h3>$4,500<span> / mo</span></h3>'),
        ("1 Custom Automation Build /mo", "1 New Custom Enterprise Pipeline Build per quarter (Safely link apps like Xero, DocuSign, and CRMs with local transit encryption)"),
        ("3 Custom Automation Builds /mo", "Dedicated Private Core Environment (Closed-loop processing for voice, financial ledger, and legal registries)"),
        ("For urgent issues we respond within 15 minutes during business hours.", "Critical architectural pathway or data routing anomalies receive immediate engineering remediation within 15 minutes during business hours.")
    ]
}

def apply_fixes():
    for file_path, changes in files_changes.items():
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            
            for find_str, replace_str in changes:
                if find_str in content:
                    content = content.replace(find_str, replace_str)
                    print(f"[{file_path.split('/')[-1]}] Replaced string successfully")
                else:
                    print(f"[{file_path.split('/')[-1]}] WARNING: String not found: {find_str[:50]}...")

            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"--> Updated {file_path}")
            else:
                print(f"--> No changes made to {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

apply_fixes()
print("Done.")
