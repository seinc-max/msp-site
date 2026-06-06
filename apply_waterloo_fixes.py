import sys

file_path = "/data/msp-site/ai-governance-waterloo.html"

changes = [
    (
        "AI Governance for Waterloo",
        "AI Governance & Automation for Professional Services Businesses in Waterloo"
    ),
    (
        "Trueline IT gives your Waterloo business a documented AI policy, safe tools, and verifiable compliance — for a flat monthly fee.",
        "Trueline IT gives your Waterloo business a documented AI policy, safe tools, and ongoing compliance management — for a flat monthly fee."
    ),
    (
        '<strong style="color: #1a2744;">68% of Ontario professional service employees</strong> use unapproved AI tools for work tasks every week, exposing client data without oversight.',
        '<strong style="color: #1a2744;">76% of employees admit to using unauthorized AI tools at work.</strong> Most of their managers don\'t know. — IBM Institute for Business Value, 2025'
    ),
    (
        "For Waterloo",
        "The Trueline IT Service"
    ),
    (
        "Average deployment time",
        "To full AI governance"
    ),
    (
        "From kickoff to full AI Acceptable Use Policy",
        "From discovery call to documented AI policy, shadow audit, and M365 configuration"
    ),
    (
        "Data Privacy",
        "AI policy coverage"
    ),
    (
        "Zero client data used to train public AI models",
        "Every client gets a documented AI acceptable use policy on day one"
    ),
    (
        "We partner with professional service businesses (legal, accounting, financial, consulting) and select manufacturing operations that handle sensitive intellectual property and client data.",
        "We specialise in professional services businesses with 15 to 150 employees — legal, accounting, financial advisory, healthcare, and consulting. If you handle confidential client data and have no internal IT department, you're exactly who we built this for."
    ),
    (
        "It means zero surprise invoices. Whether we are conducting your quarterly shadow AI audit, updating your policies for new regulations, or rolling out Microsoft Copilot, your monthly fee covers it. No per-hour overages.",
        "You pay a fixed monthly fee — not per user. It doesn't matter if you add two people or ten. Your bill is the same every month. No surprise invoices, no per-seat charges, no break-fix fees."
    ),
    (
        "Perfect. We audit them. If they are safe and enterprise-grade, we document them in your Acceptable Use Policy. If they are publicly training on your data, we migrate you to private alternatives.",
        "Even better. We audit what you already have, identify what's creating risk, configure what's safe, and shut down what isn't. You keep the tools your team loves — just without the liability."
    ),
    (
        "We are based locally in Southern Ontario and guarantee a 15-minute response time for critical issues. You get direct access to our team—no overseas call centres, no endless ticketing loops.",
        "For AI policy questions, compliance queries, and automation support we respond within one business day. For urgent issues we respond within 15 minutes during business hours. You will always hear back from a real person who knows your business."
    ),
    (
        "No long-term lock-ins. Our agreements are month-to-month. If we aren't delivering clear ROI and keeping your data safe, you can walk away at any time.",
        "Month-to-month. We earn your business every month. If you're not happy, you can cancel with 30 days notice — no penalties, no drama."
    ),
    (
        "Yes, this is our core focus. We establish private, enterprise-grade instances of these tools ensuring that your employee inputs and client data are never used to train public models.",
        "Yes. We assess which AI tools are safe for your business, set up usage policies, configure permissions in M365, and automate workflows using AI — all included depending on your plan."
    ),
    (
        "Our assessment acts as an x-ray of your network. We find exactly what AI tools your staff are using behind your back, categorize the data leakage risk, and provide a roadmap to secure it.",
        "It's a structured review of every AI tool your team is using, how it handles your data, and whether your current setup creates regulatory or insurance exposure. We deliver it as a written report with a risk score and a recommended action plan. It's included as part of the onboarding process for every new client."
    ),
    (
        "Ready to stop worrying about IT?",
        "Find out exactly where your business is exposed."
    ),
    (
        "Tell us a bit about your business and we'll be in touch within one business day.",
        "Book a 30-minute call. We will assess your AI exposure, answer your questions, and tell you exactly what needs to be done — no sales pitch, no obligation."
    )
]

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

missing = 0
for i, (old_text, new_text) in enumerate(changes, 1):
    if old_text in content:
        content = content.replace(old_text, new_text)
        print(f"Change {i}: SUCCESS")
    else:
        print(f"Change {i}: FAILED - Could not find text: {old_text[:50]}...")
        missing += 1

if missing == 0:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("All changes applied successfully. File saved.")
else:
    print(f"Failed to find {missing} strings. Did not save changes just in case.")

