import sys

def apply_fixes(file_path, is_roi):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # CHANGE 1
    content = content.replace(
        '<li>Microsoft 365 &amp; Google Workspace management</li>\n <li>Every client gets a documented AI acceptable use policy on day one</li>\n <li>Proactive monitoring — we catch problems before you do</li>\n <li>Shadow AI audits — full visibility into workforce tools</li>\n <li>A real person who knows your business</li>',
        '<li>Shadow AI audit — full visibility into what tools your team is using</li>\n <li>M365 and Google Workspace AI configuration — ring-fenced, compliant, safe</li>\n <li>Insurer-ready compliance documentation — updated annually</li>\n <li>Monthly 30-minute review call</li>\n <li>A flat monthly fee — no per-seat billing, ever</li>'
    )
    # in case indentation was different
    content = content.replace(
        '<li>Microsoft 365 &amp; Google Workspace management</li>\n        <li>Every client gets a documented AI acceptable use policy on day one</li>\n        <li>Proactive monitoring — we catch problems before you do</li>\n        <li>Shadow AI audits — full visibility into workforce tools</li>\n        <li>A real person who knows your business</li>',
        '<li>Shadow AI audit — full visibility into what tools your team is using</li>\n        <li>M365 and Google Workspace AI configuration — ring-fenced, compliant, safe</li>\n        <li>Insurer-ready compliance documentation — updated annually</li>\n        <li>Monthly 30-minute review call</li>\n        <li>A flat monthly fee — no per-seat billing, ever</li>'
    )
    
    # CHANGE 2
    content = content.replace('<li>Priority Helpdesk</li>', '<li>Priority support</li>')

    # CHANGE 3 & 4
    content = content.replace('<p class="offer-price-note">Everything in Basic, plus:</p>', '<p class="offer-price-note">For businesses with 30–75 employees.</p>')
    content = content.replace('<p class="offer-price-note">Everything in Professional, plus:</p>', '<p class="offer-price-note">For businesses with 75–150 employees.</p>')

    # CHANGE 8
    content = content.replace('Flat per-user pricing', 'Flat monthly fee — no per-seat billing')

    if is_roi:
        # CHANGE 9
        content = content.replace(
            'Staffing. Software licensing. Hardware. Maintenance. Compliance. Disaster recovery. Security. Each line item adds up fast. This section breaks down typical Ontario IT budgets by company size and shows where money is wasted vs. invested wisely.',
            'Big 4 consulting fees. Lawyer-drafted policies with no implementation. Per-seat software you don\'t control. Each adds up fast. This section breaks down what AI governance really costs in Ontario and shows where money is wasted vs. invested wisely.'
        )
        # CHANGE 10
        content = content.replace(
            'Proactive prevents emergencies. Reactive fixes them at premium cost. One server failure costs $8,000-$15,000 CAD per day. Proactive monitoring prevents that scenario entirely.',
            'Governance prevents AI data leaks. Without it, one employee mistake can trigger a PIPEDA violation or a denied insurance claim. A documented AI policy and shadow audit prevent that scenario entirely.'
        )
    else:
        # CHANGE 11
        content = content.replace(
            'Base licensing: $100-$300/user/month depending on plan. Setup, security hardening, training, compliance: $1,500-$5,000 one-time. Included in Trueline IT managed plans.',
            'Microsoft Copilot base licensing is paid directly to Microsoft. Trueline IT handles the governance layer — safe configuration, acceptable use policy, permission hardening, and compliance — included in your flat monthly fee.'
        )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

apply_fixes("/data/msp-site/ai-automation-roi-guide.html", True)
apply_fixes("/data/msp-site/safe-copilot-deployment.html", False)
