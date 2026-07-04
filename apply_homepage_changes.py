import re

file_path = "/data/msp-site/index.html"

MOD1_FIND = "1 active automation maintained"
MOD1_REPLACE = "1 Active Sovereign Workflow Pipeline (Containerized locally within private Ontario cloud nodes)"

MOD2_FIND = "Up to 3 active automations maintained"
MOD2_REPLACE = "Up to 3 active automated workflows maintained"

MOD3_FIND = "1 new automation build per quarter"
MOD3_REPLACE = "1 New Custom Enterprise Pipeline Build per quarter (Safely link apps like Xero, DocuSign, and CRMs with local transit encryption)"

MOD4_FIND = "Unlimited active automations"
MOD4_REPLACE = "Unlimited Sovereign Automation Infrastructure (Full local hosting & continuous security pathway audits)"

MOD5_FIND = "One active build at a time — no limits on complexity"
MOD5_REPLACE = "Dedicated Private Core Environment (Closed-loop processing for voice, financial ledger, and legal registries)"

mods = [
    (MOD1_FIND, MOD1_REPLACE),
    (MOD2_FIND, MOD2_REPLACE),
    (MOD3_FIND, MOD3_REPLACE),
    (MOD4_FIND, MOD4_REPLACE),
    (MOD5_FIND, MOD5_REPLACE)
]

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    for find_str, replace_str in mods:
        if find_str in content:
            content = content.replace(find_str, replace_str)
            print(f"Replaced string successfully: '{find_str}'")
        else:
            print(f"WARNING: String not found: '{find_str}'")

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes made to {file_path}")
except Exception as e:
    print(f"Error processing {file_path}: {e}")

print("Done.")
