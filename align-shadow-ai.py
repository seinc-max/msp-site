import re

def apply_fixes(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        content = content.replace(
            '<a href="#contact" class="nav-cta">Book a Discovery Call</a>',
            '<a href="#contact" class="nav-cta">Book My Free Discovery Call</a>'
        )

        content = content.replace(
            'Cybersecurity Built for Southern Ontario SMBs',
            'Shadow AI Prevention for Southern Ontario Professional Services'
        )

        content = content.replace(
            'In our 2026 assessment of 20 Southern Ontario businesses, 85% had zero encryption on sensitive files. 92% had unpatched critical vulnerabilities. One ransomware attack costs $50,000–$200,000 CAD to recover. Trueline IT delivers threat detection, PIPEDA compliance, incident response, and staff training as standard. No add-ons. No shortcuts.',
            'In May 2026, Canada\'s Privacy Commissioner ruled that ChatGPT violated PIPEDA. Most professional services businesses have employees using public AI tools with client data every day — with no policy and no oversight. Trueline IT delivers a documented AI Acceptable Use Policy, shadow AI audit, and ongoing compliance management as standard. No add-ons. No shortcuts.'
        )

        content = content.replace(
            'Built for 10–50 employee businesses',
            'For legal, accounting, and financial businesses'
        )

        content = content.replace(
            'Flat per-user pricing',
            'Flat monthly fee — no per-seat billing'
        )

        content = content.replace(
            '15-minute response',
            '30-day AI governance deployment'
        )

        content = content.replace(
            'The Southern Ontario Cybersecurity Reality',
            'Sound familiar?'
        )

        content = content.replace(
            '85% of Southern Ontario Businesses Have Zero File Encryption.',
            'The call you\'re dreading has already happened at another business.'
        )

        content = content.replace(
            'Based on our 2026 security assessment across Guelph, Hamilton, Burlington, and the surrounding region, we found consistent gaps. Encryption is missing. Patches are outdated. Staff are untrained. Compliance is aspirational, not documented.',
            'Most professional services businesses have no AI policy, no visibility into what tools their team is using, and no idea how much client data has already left the building. Here\'s what managing partners tell us every week.'
        )

        content = content.replace(
            '<h3>"Everything breaks at the worst time."</h3>\n <p>A server goes down on Friday afternoon. Your point-of-sale freezes mid-transaction. Your team can\'t get online. You\'re scrambling — and losing money every minute.</p>',
            '<h3>"My team is using ChatGPT with client data and I found out by accident."</h3>\n <p>Employees paste contracts, financials, and client notes into public AI tools every day. You didn\'t authorize it. You don\'t know how much has already left the building.</p>'
        )

        content = content.replace(
            '<h3>"I never know what IT is going to cost."</h3>\n <p>Random invoices. Emergency callout fees. Hardware you didn\'t expect. IT feels like a bill that arrives with no warning and no explanation.</p>',
            '<h3>"My cyber insurer sent a renewal form asking about AI governance. I don\'t have answers."</h3>\n <p>Insurers are now asking which AI tools your team uses, what policies are in place, and who is responsible. Businesses that can\'t answer are seeing premiums rise — or claims denied.</p>'
        )

        content = content.replace(
            '<h3>"I don\'t know if we\'re actually secure."</h3>\n <p>You\'ve heard the horror stories — ransomware, phishing, stolen data. You don\'t know if it could happen to you, and honestly, you don\'t know who to ask.</p>',
            '<h3>"A client asked me directly: what is your AI data handling policy?"</h3>\n <p>You didn\'t have a good answer. Neither does most of your competition — yet. The businesses that get ahead of this question will win the clients who ask it.</p>'
        )

        content = content.replace(
            '<div class="offer-badge">Cybersecurity Included</div>',
            '<div class="offer-badge">The Trueline IT Service</div>'
        )

        content = content.replace(
            'Complete Cybersecurity. One Flat Rate. PIPEDA Included.',
            'AI governance and automation — handled. One flat monthly fee.'
        )

        content = content.replace(
            'Threat detection 24/7. Encryption by default. Patch management automated. PIPEDA audits quarterly. Incident response playbook ready. Staff training included. One flat rate per user per month.',
            'No per-seat billing. No surprise invoices. Every plan includes a documented AI Acceptable Use Policy, shadow AI audit, and ongoing compliance management. Automation builds included from Growth tier.'
        )

        content = content.replace(
            '<li>Microsoft 365 &amp; Google Workspace management</li>',
            '<li>M365 and Google Workspace AI configuration — ring-fenced, compliant, safe</li>'
        )

        content = content.replace(
            '<li>Proactive monitoring — we catch problems before you do</li>',
            '<li>Insurer-ready compliance documentation — updated annually</li>'
        )

        content = content.replace(
            '<li>A real person who knows your business</li>',
            '<li>A flat monthly fee — no per-seat billing, ever</li>'
        )

        content = content.replace(
            'Your Employees Are Leaking<br>Confidential Data to Public AI.',
            'Your team is using AI with client data.<br>One mistake can cost you everything.'
        )

        content = content.replace(
            '<p class="offer-card-label">Compliance</p>',
            '<p class="offer-card-label">Foundation</p>'
        )

        content = content.replace(
            '<p class="offer-price-note">Everything included. No hidden fees.</p>',
            '<p class="offer-price-note">For businesses with 15–30 employees.</p>'
        )
        content = content.replace(
            '<h3>$1,500<span> / mo</span></h3>',
            '<h3>$1,500<span> / mo</span></h3>\n <p class="offer-price-note">For businesses with 15–30 employees.</p>'
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Applied fixes to {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

apply_fixes("/data/msp-site/shadow-ai-prevention-ontario.html")
