import os

filepath = "/data/msp-site/ai-governance-ontario.html"

replacements = [
    (
        "<h3>IT fires every week</h3>\n        <p>Staff can't work. You're troubleshooting instead of running your business. Every problem is a surprise.</p>",
        "<h3>Staff using ChatGPT with client data</h3>\n        <p>Employees paste contracts, financials, and client notes into public AI tools every day. You didn't authorize it. You don't know how much has already left the building.</p>"
    ),
    (
        "<h3>Unpredictable IT bills</h3>\n        <p>Surprise PIPEDA compliance fines and massive consultant invoices for Enterprise AI roadmaps.</p>",
        "<h3>Your cyber insurer is asking about AI</h3>\n        <p>Renewal forms now ask which AI tools your team uses and what policies are in place. Businesses that can't answer face higher premiums — or denied claims.</p>"
    ),
    (
        "<h3>One ransomware attack away</h3>\n        <p>No monitoring, no backups tested, no incident plan. Your cyber insurer is asking questions you can't answer.</p>",
        "<h3>A client asked about your AI policy</h3>\n        <p>You didn't have a good answer. The businesses that get ahead of this question will win the clients who ask it.</p>"
    ),
    (
        "<li>Unlimited helpdesk — 15-min response guarantee</li>\n            <li>24/7 monitoring and proactive maintenance</li>\n            <li>Cybersecurity — endpoint protection included</li>\n            <li>Microsoft 365 management and support</li>\n            <li>Automated backups with tested recovery</li>\n            <li>Monthly IT health report</li>",
        "<li>AI Acceptable Use Policy — created and maintained</li>\n            <li>Quarterly shadow AI audit</li>\n            <li>Microsoft 365 and Copilot AI configuration</li>\n            <li>Insurer-ready compliance documentation</li>\n            <li>1 active automation maintained</li>\n            <li>Monthly 30-minute review call</li>"
    )
]

if os.path.exists(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
        else:
            # Let's try flexible matching for spacing
            print(f"Warning: Exact string not found:\n{old[:50]}...")
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
else:
    print(f"File not found: {filepath}")

