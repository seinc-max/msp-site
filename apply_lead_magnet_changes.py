import re

files_changes = {
    "/data/msp-site/ai-automation-roi-guide.html": [
        ("The Complete IT Cost Guide for Ontario", "The Sovereign Automation ROI Guide for Ontario"),
        ("understand the real cost of IT — and find the optimal balance.", "understand the real ROI of automated infrastructure — and eliminate data liability."),
        ("Calculate Your True IT Cost", "Calculate Your True Automation ROI"),
        ("2\nWe build your IT plan", "2\nWe map your Sovereign Architecture"),
        ("We build your IT plan", "We map your Sovereign Architecture"), # Also try without the number in case it's in an element
        ("IT Cost Questions for Ontario Business Owners", "Automation ROI Questions for Ontario Business Owners"),
        ("What is the average IT budget for a 20-person Ontario business?", "What is the financial leakage of manual administration for a 20-person Ontario business?")
    ],
    "/data/msp-site/ai-exposure-score.html": [
        ("IT Health Diagnostic", "Corporate Risk Diagnostic"),
        ("How Does Your IT Stack Up?", "How Does Your Data Security Stack Up?"),
        ("Every day without proactive IT increases risk of catastrophic failure.", "Every day without proactive data governance increases your regulatory exposure."),
        ("2\nWe build your IT plan", "2\nWe map your Sovereign Architecture"),
        ("We build your IT plan", "We map your Sovereign Architecture"), # Fallback without newline
        ("What if we already have some IT in place?", "What if we already have basic AI guardrails in place?"),
        ("Critical issues get a technician on it within 15 minutes.", "Critical architectural pathway or data routing anomalies receive immediate engineering remediation within 15 minutes during business hours.")
    ]
}

for file_path, changes in files_changes.items():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        
        for find_str, replace_str in changes:
            if find_str in content:
                content = content.replace(find_str, replace_str)
                print(f"[{file_path.split('/')[-1]}] Replaced: '{find_str}'")
            elif find_str == "2\nWe build your IT plan":
                # Try finding across HTML elements if literal string isn't there
                pattern = r"2\s*</div>\s*<h3>We build your IT plan"
                match = re.search(pattern, content)
                if match:
                    content = re.sub(pattern, "2</div>\n        <h3>We map your Sovereign Architecture", content)
                    print(f"[{file_path.split('/')[-1]}] Replaced using regex for step 2")

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"--> Updated {file_path}")
        else:
            print(f"--> No changes made to {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print("Done.")
