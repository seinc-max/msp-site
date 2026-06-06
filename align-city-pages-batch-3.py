import re

def apply_fixes(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # CHANGE 1
        content = content.replace(
            '<title>IT Support & AI Automation in Ontario | Trueline IT</title>',
            '<title>AI Governance & Automation in Ontario | Trueline IT</title>'
        )

        # CHANGE 2
        content = content.replace(
            'Flat-rate AI governance and IT support for Ontario. 15-min response, secure automation, shadow AI audits, no contracts.',
            'Flat-rate AI governance and automation for Ontario professional services businesses. Documented AI policy, shadow AI audits, Copilot compliance, no contracts.'
        )

        # CHANGE 3
        content = content.replace(
            'Ontario IT Support — Starting at $99/user/mo',
            'AI Governance & Automation for Ontario Professional Services'
        )

        # CHANGE 4
        content = content.replace(
            'Flat-rate IT support.<br><em>No surprise bills.</em><br>15-min response.',
            'Your team is using AI with client data.<br><em>One mistake</em> can cost you everything.'
        )

        # CHANGE 5
        content = content.replace(
            'Your dedicated IT team — without the cost of hiring one. Built for Southern Ontario businesses with 10–50 employees. Unlimited helpdesk, cybersecurity, and 24/7 monitoring.',
            'In May 2026, Canada\'s Privacy Commissioner ruled that ChatGPT violated PIPEDA. The Law Society of Ontario has warned lawyers that using public AI tools with client data risks disciplinary action. Trueline IT gives your business a documented AI policy, safe tools, and ongoing compliance management — for a flat monthly fee.'
        )

        # CHANGE 6
        content = content.replace(
            'Built for 10–50 employee businesses',
            'For legal, accounting, and financial businesses'
        )

        # CHANGE 7
        content = content.replace(
            '15-minute response guarantee',
            '30-day AI governance deployment'
        )

        # CHANGE 8
        content = content.replace(
            'Burlington-based team, serving GTA West',
            'AI Acceptable Use Policy included'
        )

        # CHANGE 9
        content = content.replace(
            'Switch from your current provider in 48 hours',
            'Shadow AI audit on every plan'
        )

        # CHANGE 10
        content = content.replace(
            'See if Trueline IT is right for your business',
            'Find out exactly where your business is exposed'
        )

        # CHANGE 11
        content = content.replace(
            'No sales pitch. Just an honest look at your current IT setup and what better support would cost.',
            'No sales pitch. Just an honest look at your AI exposure and what it takes to fix it.'
        )

        # CHANGE 12
        content = content.replace(
            'Up and running in 48 hours',
            'From exposure to protected in 30 days'
        )

        # CHANGE 13
        content = content.replace(
            '<h3>Book a free 30-min call</h3>\n <p>We review your current setup. No software installed. No commitment required.</p>',
            '<h3>Book a free 30-min call</h3>\n <p>We review your AI exposure. No commitment required.</p>'
        )

        # CHANGE 14
        content = content.replace(
            '<h3>Get your IT audit report</h3>\n <p>We document every risk, gap, and cost — in plain English. $1 admin fee, fully refundable.</p>',
            '<h3>We run your AI Risk Audit</h3>\n <p>We document every AI tool in use and every exposure — in plain English, ready for your insurer and clients.</p>'
        )

        # CHANGE 15
        content = content.replace(
            '<h3>Switch in 48 hours</h3>\n <p>We handle the transition. Your team notices faster support. You notice a predictable bill.</p>',
            '<h3>We manage it ongoing</h3>\n <p>Policy updates as regulations change. Automations built on schedule. You get peace of mind.</p>'
        )

        # CHANGE 16
        content = content.replace(
            'Most Ontario SMBs are one IT failure away from a bad week',
            'The call you\'re dreading has already happened at another business'
        )

        # CHANGE 17
        content = content.replace(
            '<h3>IT fires every week</h3>\n <p>Staff can\'t work. You\'re troubleshooting instead of running your business. Every problem is a surprise.</p>',
            '<h3>Staff using ChatGPT with client data</h3>\n <p>Employees paste contracts, financials, and client notes into public AI tools every day. You didn\'t authorize it. You don\'t know how much has already left the building.</p>'
        )

        # CHANGE 18
        content = content.replace(
            '<h3>Unpredictable IT bills</h3>\n <p>Surprise PIPEDA compliance fines and massive consultant invoices for Enterprise AI roadmaps.</p>',
            '<h3>Your cyber insurer is asking about AI</h3>\n <p>Renewal forms now ask which AI tools your team uses and what policies are in place. Businesses that can\'t answer face higher premiums — or denied claims.</p>'
        )

        # CHANGE 19
        content = content.replace(
            '<h3>One ransomware attack away</h3>\n <p>No monitoring, no backups tested, no incident plan. Your cyber insurer is asking questions you can\'t answer.</p>',
            '<h3>A client asked about your AI policy</h3>\n <p>You didn\'t have a good answer. The businesses that get ahead of this question will win the clients who ask it.</p>'
        )

        # CHANGE 20
        content = content.replace(
            '"We used to spend half our Monday fixing whatever broke over the weekend. Since switching to Trueline IT, we haven\'t had a single Monday fire in four months. Worth every penny."',
            '"We were using ChatGPT for client work without realizing the privacy risk. Trueline flagged it, fixed it, and set up a proper policy in a week. We sleep better now."'
        )

        # CHANGE 21
        content = content.replace(
            '— Operations Manager, 18-person accounting business, Mississauga',
            '— Managing Partner, 18-person accounting business, Mississauga'
        )

        # CHANGE 22
        content = content.replace(
            'One flat rate. Everything included.',
            'One flat monthly fee. Everything included.'
        )

        # CHANGE 23
        content = content.replace(
            '$99<span>/user/mo</span>',
            '$1,500<span>/mo</span>'
        )

        # CHANGE 24
        content = content.replace(
            'Minimum 10 users. No setup fees. No contracts. Cancel anytime.',
            'Per business, not per user. No contracts. Cancel anytime.'
        )

        # CHANGE 25
        content = content.replace(
            '<li>Unlimited helpdesk — 15-min response guarantee</li>\n <li>24/7 monitoring and proactive maintenance</li>\n <li>Cybersecurity — endpoint protection included</li>\n <li>Microsoft 365 management and support</li>\n <li>Automated backups with tested recovery</li>\n <li>Monthly IT health report</li>',
            '<li>AI Acceptable Use Policy — created and maintained</li>\n <li>Quarterly shadow AI audit</li>\n <li>Microsoft 365 and Copilot AI configuration</li>\n <li>Insurer-ready compliance documentation</li>\n <li>1 active automation maintained</li>\n <li>Monthly 30-minute review call</li>'
        )

        # CHANGE 26
        content = content.replace(
            '<h2>Ready to stop paying for IT surprises?</h2>\n <p>Book a free 30-minute call. We\'ll tell you exactly what your IT should cost.</p>',
            '<h2>Ready to find out where you\'re exposed?</h2>\n <p>Book a free 30-minute call. We\'ll assess your AI exposure — no sales pitch, no obligation.</p>'
        )

        # CHANGE 27
        content = content.replace(
            "pageName: 'IT Support Ontario Landing Page'",
            "pageName: 'AI Governance Ontario Landing Page'"
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Applied fixes to {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

apply_fixes("/data/msp-site/ai-governance-ontario.html")
