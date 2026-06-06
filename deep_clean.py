import os
import re

def clean_file(file_path):
    if not os.path.exists(file_path):
        return
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Clean JSON-LD Schema (Services & Descriptions) across all files
    content = content.replace(
        '"description": "Flat-rate managed IT services for small businesses across Canada. 24/7 helpdesk, security monitoring, backups, and M365 support."',
        '"description": "Flat-rate AI governance and automation for professional services in Ontario. Shadow AI audits, Copilot compliance, and secure workflow automation support."'
    )
    content = content.replace('"serviceType": "Managed IT Services"', '"serviceType": "AI Governance & Automation"')
    content = content.replace('"name": "Managed IT Services"', '"name": "AI Governance"')
    content = content.replace('"name": "Managed IT Support"', '"name": "AI Governance"')

    # 2. Clean specific file content
    if "ai-automation-roi-guide.html" in file_path:
        content = content.replace(
            '"text": "10-person company: $2,500–$4,000/month reactive IT. 50-person company: $8,000–$12,000/month reactive IT. Proactive managed IT typically costs 30-40% less."',
            '"text": "10-person company: $2,500–$4,000/month in manual data entry waste. 50-person company: $8,000–$12,000/month in waste. Proactive AI automation typically recovers 30-40% of administrative overhead."'
        )
        content = content.replace(
            '"text": "One full-time IT hire: $100,000+ salary plus benefits, plus tools, hardware, licensing. One managed IT service provider: $25,000–$45,000/year for 10-20 people, all-inclusive."',
            '"text": "One full-time administrative hire: $60,000+ salary plus benefits. One flat-rate AI automation suite: $30,000/year, replacing 3+ admin roles."'
        )
        content = content.replace(
            '"text": "PIPEDA compliance requires documented security controls, audits, staff training, incident response plans. Budget: $5,000–$15,000 annually for a 20-person business. Managed IT includes this as standard."',
            '"text": "PIPEDA compliance for generative AI requires documented acceptable use policies, Shadow AI audits, and DLP enforcement. Our flat-rate plans include this natively."'
        )
        content = content.replace(
            '"text": "Average Ontario business saves 30-40% on IT costs annually by switching to proactive managed IT. Plus: zero emergency calls, predictable budgeting, faster issue resolution, better compliance."',
            '"text": "Average Ontario business saves 30-40% on administrative overhead annually by switching to proactive AI automation. Plus: zero Shadow AI liability, predictable budgeting, and faster document processing."'
        )
        content = content.replace(
            '<p class="hero-sub">In our 2026 assessment of 20 Southern Ontario businesses, 78% operated with no IT monitoring, no verified backups, and no after-hours support. The average company spent $45,000–$80,000 annually on reactive IT fixes. One full-time IT hire costs $100,000+/year salary alone. Proactive managed IT services cost $25,000–$45,000 annually for the same company — and eliminate 75% of emergency costs. This guide breaks down every IT spending category, shows what you\'re actually paying for, and reveals where Ontario businesses waste money.</p>',
            '<p class="hero-sub">In our 2026 assessment of 20 Southern Ontario businesses, 78% operated with no Shadow AI tracking, no verified Copilot security, and no Acceptable Use Policies. The average company spent $45,000–$80,000 annually on manual internal labor that could be automated. This guide breaks down every administrative spending category, shows what you\'re actually paying for, and reveals where Ontario businesses waste money.</p>'
        )
        content = content.replace(
            '<p class="section-sub">10-person company: $2,500–$4,000/month reactive IT vs. $2,100–$3,700/month proactive managed IT. 50-person company: $8,000–$12,000/month reactive vs. $5,000–$8,000/month proactive. Larger teams amplify the ROI.</p>',
            '<p class="section-sub">10-person company: $2,500–$4,000/month manual waste vs. $1,500/month flat-rate AI automation. 50-person company: $8,000–$12,000/month manual waste vs. $4,000/month flat-rate AI Scale plan. Larger teams amplify the ROI.</p>'
        )
        content = content.replace(
            '<p class="section-sub">Reactive IT (break-fix per incident): $50–$300 per ticket, unpredictable. Proactive managed IT (flat-rate): $99–$199/user/month, predictable budgeting.</p>',
            '<p class="section-sub">Reactive liability (PIPEDA fines): $50,000+, unpredictable. Proactive AI Governance (flat-rate): $1,500–$4,000/month, predictable budgeting.</p>'
        )
        content = content.replace(
            '<p class="faq-answer">Reactive IT (break-fix model): $2,500–$4,000/month. Proactive managed IT (flat-rate): $2,100–$3,700/month. The difference is predictability and fewer emergencies. Most Ontario businesses overspend on reactive models and underspend on prevention.</p>',
            '<p class="faq-answer">Manual administration: $2,500–$4,000/month in wasted labor. Proactive AI Automation (flat-rate): $1,500–$4,000/month. The difference is predictability and margin expansion. Most Ontario businesses overspend on manual labor and underspend on automation.</p>'
        )

    if "ai-exposure-score.html" in file_path or "shadow-ai-prevention-ontario.html" in file_path:
        content = content.replace(
            '<strong style="color: #1a2744;">SMBs without managed IT spend up to 40% more</strong> on technology support costs than those with a dedicated provider. — BizTech',
            '<strong style="color: #1a2744;">76% of employees admit to using unauthorized AI tools at work.</strong> Most of their managers don\'t know. — IBM Institute for Business Value, 2025'
        )
    
    if "ai-exposure-score.html" in file_path:
        content = content.replace(
            '<p class="section-sub">Your score tells you where you stand today. If you\'re in the Critical or Moderate risk zone, don\'t wait. One server failure costs $8,000–$15,000 CAD per day. One ransomware attack costs $50,000–$200,000 CAD. Proactive managed IT prevents both.</p>',
            '<p class="section-sub">Your score tells you where you stand today. If you\'re in the Critical or Moderate risk zone, don\'t wait. One PIPEDA violation costs $50,000–$200,000 CAD. Proactive AI governance prevents it.</p>'
        )
        content = content.replace(
            '<p class="faq-answer">If your score is 0–5 or 6–10, schedule a discovery call. We\'ll review your assessment, identify your top 3 risks, and show you how proactive managed IT fixes them. If your score is 11–15, you\'re in good shape — but we can still optimize.</p>',
            '<p class="faq-answer">If your score is 0–5 or 6–10, schedule a discovery call. We\'ll review your assessment, identify your top Shadow AI risks, and show you how proactive AI Governance fixes them. If your score is 11–15, you\'re in good shape — but we can still optimize.</p>'
        )

    if "ai-governance-ontario.html" in file_path:
        content = content.replace(
            '<p>Hourly break-fix invoices with no warning. You never know what IT is going to cost this month.</p>',
            '<p>Surprise PIPEDA compliance fines and massive consultant invoices for Enterprise AI roadmaps.</p>'
        )

    if "20-southern-ontario-shadow-ai-audits-2026.html" in file_path:
        content = content.replace('"name": "How do I know if my business needs managed IT services?",', '"name": "How do I know if my business needs AI Governance policies?",')
        content = content.replace('"managed IT", "Southern Ontario", "cybersecurity", "PIPEDA", "SMB", "IT audit"', '"AI governance", "Southern Ontario", "Shadow AI", "PIPEDA", "automation", "compliance audit"')
        content = content.replace(
            '<p>So they hire a break-fix vendor. Someone shows up when something breaks. The bill is $150–$200 per hour. The problem gets fixed. Then nothing happens until the next failure.</p>',
            '<p>So they ban ChatGPT. A memo goes out. The problem looks fixed on paper. Then employees just use their personal phones to summarize confidential documents.</p>'
        )
        content = content.replace(
            '<p>They had been running without proper backups or monitoring for three years. Their break-fix vendor charged $175/hour. Total spend on IT: ~$12,000/year.</p>',
            '<p>They had been running without an AI Acceptable Use Policy or DLP controls since LLMs launched. They spent nothing on proactive AI governance.</p>'
        )
        content = content.replace(
            '<p>With managed IT services at $149/user/month (their business size: $44,700/year), they would have paid $24,000 more per year. But that proactive monitoring would have caught the failing hardware three weeks earlier—before failure. The backup verification would have caught the corrupt backups before they mattered. Recovery time would have been minutes, not days.</p>',
            '<p>With flat-rate AI Compliance at $1,500/month, they would have paid $18,000 per year. But that proactive monitoring and DLP execution would have caught the unauthorized Copilot access three weeks earlier—before a server leak. M365 permission hardening would have shielded the HR director\'s payroll files from general staff query prompts. The liability would have been negated.</p>'
        )
        content = content.replace('<td style="padding:12px 16px;border-bottom:1px solid var(--border);font-weight:600;">Break-Fix Vendor</td>', '<td style="padding:12px 16px;border-bottom:1px solid var(--border);font-weight:600;">Traditional IT Vendor</td>')
        content = content.replace('<td style="padding:12px 16px;border-bottom:1px solid var(--border);font-weight:700;color:var(--navy);">Trueline Managed IT</td>', '<td style="padding:12px 16px;border-bottom:1px solid var(--border);font-weight:700;color:var(--navy);">Trueline AI Governance</td>')
        content = content.replace(
            '<div class="related-links" style="margin-top:2rem;padding:1.5rem;background:#f0f4ff;border-radius:8px;"><p style="font-weight:600;color:#1a2744;margin-bottom:0.75rem;">Related resources from Trueline IT:</p><ul style="color:#2563eb;line-height:2;margin-left:1.2rem;"><li><a href="/shadow-ai-prevention-ontario.html">Cybersecurity for Southern Ontario SMBs</a></li><li><a href="/managed-it-services-southern-ontario.html">Managed IT Services Southern Ontario</a></li><li><a href="/ai-automation-roi-guide.html">IT Cost Guide for Ontario Business Owners</a></li><li><a href="/ai-exposure-score.html">Free 15-Minute IT Health Score</a></li></ul></div>',
            '<div class="related-links" style="margin-top:2rem;padding:1.5rem;background:#f0f4ff;border-radius:8px;"><p style="font-weight:600;color:#1a2744;margin-bottom:0.75rem;">Related resources from Trueline IT:</p><ul style="color:#2563eb;line-height:2;margin-left:1.2rem;"><li><a href="/shadow-ai-prevention-ontario">Shadow AI Prevention</a></li><li><a href="/ai-governance-ontario">AI Governance Ontario</a></li><li><a href="/ai-automation-roi-guide">Automation ROI Guide</a></li><li><a href="/ai-exposure-score">AI Exposure Risk Score</a></li></ul></div>'
        )
    
    if "is-your-ontario-business-pipeda-compliant.html" in file_path:
        content = content.replace(
            '<div class="related-links" style="margin-top:2rem;padding:1.5rem;background:#f0f4ff;border-radius:8px;"><p style="font-weight:600;color:#1a2744;margin-bottom:0.75rem;">Related resources from Trueline IT:</p><ul style="color:#2563eb;line-height:2;margin-left:1.2rem;"><li><a href="/shadow-ai-prevention-ontario.html">Cybersecurity for Southern Ontario SMBs</a></li><li><a href="/ai-exposure-score.html">Free 15-Minute IT Health Score</a></li><li><a href="/managed-it-services-guelph.html">Managed IT Services — Guelph</a></li><li><a href="/managed-it-services-hamilton.html">Managed IT Services — Hamilton</a></li></ul></div>',
            '<div class="related-links" style="margin-top:2rem;padding:1.5rem;background:#f0f4ff;border-radius:8px;"><p style="font-weight:600;color:#1a2744;margin-bottom:0.75rem;">Related resources from Trueline IT:</p><ul style="color:#2563eb;line-height:2;margin-left:1.2rem;"><li><a href="/shadow-ai-prevention-ontario">Shadow AI Prevention</a></li><li><a href="/ai-governance-ontario">AI Governance Ontario</a></li><li><a href="/ai-automation-roi-guide">Automation ROI Guide</a></li><li><a href="/ai-exposure-score">AI Exposure Risk Score</a></li></ul></div>'
        )

    # 3. Clean global "no surprise invoices, no per-seat charges, no break-fix fees" references inside ALL FAQ answers
    content = content.replace('no break-fix fees.', 'no enterprise consulting retainers.')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Run on all HTML files
for root, dirs, files in os.walk("/data/msp-site"):
    for file in files:
        if file.endswith(".html"):
            clean_file(os.path.join(root, file))

