import sys
import glob

# We will just brute-force the 22 specific delta changes across ALL 6 city pages (since these changes represent the final diff provided by claude).

changes = [
    # 1. Hero Eyebrow (Regex or partial replacement per city)
    (">AI Governance for [^<]+<", ">AI Governance & Automation for Professional Services Businesses in <CITY><"),
    # 2. Hero Sub
    ("verifiable compliance — for a flat monthly fee.", "ongoing compliance management — for a flat monthly fee."),
    # 3. Offer Badge
    ('>For [a-zA-Z-\s]+<', '>The Trueline IT Service<'),
    # 4. Offer Title
    ("AI Governance at One Flat Monthly Rate", "AI governance and automation — handled. One flat monthly fee."),
    # 5. Offer Sub
    ("No hourly consulting fees. No endless enterprise deployments. Just a rapid 30-day rollout of safe AI tools and policies to protect your liability.", "No per-seat billing. No surprise invoices. Every plan includes a documented AI Acceptable Use Policy, shadow AI audit, and ongoing compliance management. Automation builds included from Growth tier."),
    # 6. Step 1 Description
    ("A 30-minute chat to understand your business, your current setup, and where we can help most.", "A 30-minute call to understand your business, your AI exposure, and which tier fits your situation. No sales pitch — just a diagnosis."),
    # 7. Stats title
    ("What Trueline IT Delivers for [a-zA-Z-\s]+", "Numbers we stand behind."),
    # 8. Stat 1 label
    ("Average deployment time", "To full AI governance"),
    # 9. Stat 1 desc
    ("From kickoff to full AI Acceptable Use Policy", "From discovery call to documented AI policy, shadow audit, and M365 configuration"),
    # 10. Stat 2 label
    ("Data Privacy", "AI policy coverage"),
    # 11. Stat 2 desc
    ("Zero client data used to train public AI models", "Every client gets a documented AI acceptable use policy on day one"),
    # 12. Stat 4 label
    ("Per business, per month", "Flat fee"),
    # 13. FAQ 1
    ("We partner with professional service businesses (legal, accounting, financial, consulting) and select manufacturing operations that handle sensitive intellectual property and client data.", "We specialise in professional services businesses with 15 to 150 employees — legal, accounting, financial advisory, healthcare, and consulting. If you handle confidential client data and have no internal IT department, you're exactly who we built this for."),
    # 14. FAQ 2
    ("It means zero surprise invoices. Whether we are conducting your quarterly shadow AI audit, updating your policies for new regulations, or rolling out Microsoft Copilot, your monthly fee covers it. No per-hour overages.", "You pay a fixed monthly fee — not per user. It doesn't matter if you add two people or ten. Your bill is the same every month. No surprise invoices, no per-seat charges, no break-fix fees."),
    # 15. FAQ 3
    ("Perfect. We audit them. If they are safe and enterprise-grade, we document them in your Acceptable Use Policy. If they are publicly training on your data, we migrate you to private alternatives.", "Even better. We audit what you already have, identify what's creating risk, configure what's safe, and shut down what isn't. You keep the tools your team loves — just without the liability."),
    # 16. FAQ 4
    ("We are based locally in Southern Ontario and guarantee a 15-minute response time for critical issues. You get direct access to our team—no overseas call centres, no endless ticketing loops.", "For AI policy questions, compliance queries, and automation support we respond within one business day. For urgent issues we respond within 15 minutes during business hours. You will always hear back from a real person who knows your business."),
    # 17. FAQ 5
    ("No long-term lock-ins. Our agreements are month-to-month. If we aren't delivering clear ROI and keeping your data safe, you can walk away at any time.", "Month-to-month. We earn your business every month. If you're not happy, you can cancel with 30 days notice — no penalties, no drama."),
    # 18. FAQ 6
    ("Yes, this is our core focus. We establish private, enterprise-grade instances of these tools ensuring that your employee inputs and client data are never used to train public models.", "Yes. We assess which AI tools are safe for your business, set up usage policies, configure permissions in M365, and automate workflows using AI — all included depending on your plan."),
    # 19. FAQ 7
    ("Our assessment acts as an x-ray of your network. We find exactly what AI tools your staff are using behind your back, categorize the data leakage risk, and provide a roadmap to secure it.", "It's a structured review of every AI tool your team is using, how it handles your data, and whether your current setup creates regulatory or insurance exposure. We deliver it as a written report with a risk score and a recommended action plan. It's included as part of the onboarding process for every new client."),
    # 20. Contact Label
    ("Get in touch", "Start here"),
    # 21. Contact Title
    ("Ready to stop worrying about IT?", "Find out exactly where your business is exposed."),
    # 22. Footer
    ('<a href="/about">About</a>', '<a href="/about.html">About</a>'),
    ('<a href="/privacy">Privacy</a>', '<a href="/privacy.html">Privacy</a>'),
    ('<a href="/terms">Terms</a>', '<a href="/terms.html">Terms</a>')
]

import re

files = glob.glob("/data/msp-site/ai-governance-*.html")

for filepath in files:
    city_name = filepath.split("ai-governance-")[1].replace(".html", "").replace("-", " ").title()
    # Correct capitalization for KW
    if city_name == "Kitchener Waterloo":
        city_name = "Kitchener-Waterloo"
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Pre-changes (Since some have already been applied, some haven't. We just aggressively ensure the target state)
    for old, new in changes:
        if "<CITY>" in new:
            new_target = new.replace("<CITY>", city_name)
            # Find the dynamic old string based on city
            old_dynamic = old.replace("[^<]+", city_name)
            if re.search(old, content):
                 content = re.sub(old, new_target, content)
        elif "[a-zA-Z-\s]+" in old:
             if re.search(old, content):
                  content = re.sub(old, new, content)
        else:
             content = content.replace(old, new)
             
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Applied final deltas to {city_name}.")

