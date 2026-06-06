import sys

file_path = "/data/msp-site/ai-governance-southern-ontario.html"

# Due to regional mismatches on the Southern Ontario page (unlike the exact city structure files) 
# we'll run loose targeted replacements.
changes = {
    "AI Governance for Southern Ontario": "AI Governance & Automation for Professional Services Businesses in Southern Ontario",
    "Trueline IT gives your Southern Ontario business a documented AI policy, safe tools, and verifiable compliance — starting at $1,500/mo.": "Trueline IT gives your Southern Ontario business a documented AI policy, safe tools, and ongoing compliance management — for a flat monthly fee.",
    '<strong style="color: #1a2744;">Over 68% of knowledge workers actively use Shadow AI tools at work</strong>, circumventing IT policies and leaking confidential data. — Microsoft / LinkedIn 2026': '<strong style="color: #1a2744;">76% of employees admit to using unauthorized AI tools at work.</strong> Most of their managers don\'t know. — IBM Institute for Business Value, 2025',
    '<div class="offer-badge">For Southern Ontario</div>': '<div class="offer-badge">The Trueline IT Service</div>',
    '>For Southern Ontario<': '>The Trueline IT Service<',
    "Every plan includes a documented AI Acceptable Use Policy, shadow AI audit, and ongoing compliance management. Automation builds included from Growth tier.": "Every plan includes a documented AI Acceptable Use Policy, shadow AI audit, and ongoing compliance management. Automation builds included from Growth tier.", # keeping as is unless needed
    
    # Map the unique FAQ phrasing found on Southern Ontario -> City Standard replacement string answers
    "What is an AI Acceptable Use Policy and why do Southern Ontario businesses need it?": "What is a Shadow AI Audit?",
    "Most organizations either blindly ban AI (which employees circumvent) or run completely blind (massive liability). An AUP officially dictates what data can be supplied to which categorized models. Small professional service environments need this explicit liability protection more than larger, more heavily resourced enterprises.": "It's a structured review of every AI tool your team is using, how it handles your data, and whether your current setup creates regulatory or insurance exposure. We deliver it as a written report with a risk score and a recommended action plan. It's included as part of the onboarding process for every new client.",

    "My team is already using ChatGPT or Copilot secretly. What should we do?": "My team is already using ChatGPT or Copilot secretly. What should we do?",
    "First, assume confidentiality is breached. Start by mapping organizational processes to find out who is doing the heavy lifting using these platforms, run a Shadow AI audit, and formally transition them onto a safe, private instance model to resecure the liability loop.": "Even better. We audit what you already have, identify what's creating risk, configure what's safe, and shut down what isn't. You keep the tools your team loves — just without the liability.",

    "How fast does Trueline IT respond to network issues?": "How fast does Trueline IT respond to issues?",
    "For critical compliance or data security situations, we respond in 15 minutes. For standard requests, you get an answer by the next business day. You are always talking to someone locally.": "For AI policy questions, compliance queries, and automation support we respond within one business day. For urgent issues we respond within 15 minutes during business hours. You will always hear back from a real person who knows your business.",

    "Does Trueline IT force Southern Ontario businesses into restrictive long-term contracts?": "Does Trueline IT force businesses into restrictive long-term contracts?",
    "Never. We work on a strict month-to-month basis. If we aren't delivering the AI protection and continuous automation edge you need, you have complete freedom to leave.": "Month-to-month. We earn your business every month. If you're not happy, you can cancel with 30 days notice — no penalties, no drama.",

    "Do you configure private LLM networks and API models for us?": "Do you configure private LLM networks and API models for us?",
    "Yes, this is core to our service. We establish enterprise-grade, localized model architectures for smaller businesses that want to ensure external models never ingest their prompts or proprietary context windows.": "Yes. We assess which AI tools are safe for your business, set up usage policies, configure permissions in M365, and automate workflows using AI — all included depending on your plan.",

    "Are all your fees completely flat? No extra hours?": "Are all your fees completely flat?",
    "Entirely flat month-to-month. No break-fix extra fees, no onboarding spikes, and absolutely no hourly billing surprises on AI compliance initiatives.": "You pay a fixed monthly fee — not per user. It doesn't matter if you add two people or ten. Your bill is the same every month. No surprise invoices, no per-seat charges, no break-fix fees.",
    
    "Tell us a bit about your business and we'll be in touch within one business day.": "Book a 30-minute call. We will assess your AI exposure, answer your questions, and tell you exactly what needs to be done — no sales pitch, no obligation.",
}

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

for old_text, new_text in changes.items():
    if old_text in content:
        content = content.replace(old_text, new_text)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

