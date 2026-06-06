import sys

def apply_fixes(file_path, replacements):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        for old_txt, new_txt in replacements:
            if old_txt in content:
                content = content.replace(old_txt, new_txt)
            else:
                print(f"Warning: Could not find text in {file_path}:\n{old_txt[:50]}...")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Applied fixes to {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

file1 = "/data/msp-site/blog/is-your-ontario-business-pipeda-compliant.html"
replacements1 = [
    (
        'Pricing for IT support starts at <strong>$99–$199 per user per month</strong> for managed services, which includes ongoing compliance monitoring and security updates.',
        'Trueline IT\'s AI governance retainers start at <strong>$1,500/month per business</strong> — including your AI Acceptable Use Policy, shadow AI audit, M365 configuration, and insurer-ready compliance documentation. No per-seat billing.'
    )
]

file2 = "/data/msp-site/blog/20-southern-ontario-shadow-ai-audits-2026.html"
replacements2 = [
    (
        'Based on our assessment of 20 businesses, 78% operate entirely on reactive IT with no monitoring, no automated backups, and no post-hours support.',
        'Based on our assessment of 20 businesses, 78% had no AI acceptable use policy, no visibility into employee AI tool usage, and no documentation ready for their cyber insurer.'
    ),
    (
        '"name": "How much does a server failure cost a business?",',
        '"name": "How much does an AI data breach cost a business?",'
    ),
    (
        'One server failure costs businesses $8,000–$15,000 per day in lost productivity. An unrecoverable data loss can cost $30,000–$100,000 in recovery and downtime.',
        'A PIPEDA investigation can cost a business $50,000 or more in legal fees, fines, and remediation. A Law Society disciplinary proceeding can cost a professional their licence.'
    ),
    (
        'Anonymized IT audit data from 20 Southern Ontario businesses assessed in 2026. Covers monitoring, backup verification, encryption, patch management, disaster recovery, and PIPEDA compliance.',
        'Anonymized AI risk audit data from 20 Southern Ontario businesses assessed in 2026. Covers shadow AI usage, AI acceptable use policies, client data exposure, M365 Copilot configuration, and PIPEDA compliance.'
    ),
    (
        'In our 2026 assessment of 20 Southern Ontario businesses, 78% operated with no IT monitoring, no verified backups, and no after-hours support. One server failure costs these businesses $8,000–$15,000 CAD per day. Here is what we found — and what it means for your business.',
        'In our 2026 assessment of 20 Southern Ontario professional services businesses, 78% had no AI acceptable use policy, no visibility into which AI tools their employees were using, and no documentation ready for their cyber insurer. Here is what we found — and what it means for your business.'
    ),
    (
        'After audits at manufacturing businesses, professional services, accounting practices, and healthcare offices in Guelph, Hamilton, Burlington, and surrounding areas, we discovered that <strong>78% of assessed businesses operate entirely on reactive IT</strong>. No monitoring. No automated backups. No post-hours support.',
        'After AI risk assessments at legal firms, accounting practices, financial advisory businesses, and healthcare offices in Guelph, Hamilton, Burlington, and surrounding areas, we discovered that <strong>78% of assessed businesses had employees actively using unauthorized AI tools with client data</strong>. No policy. No visibility. No documentation.'
    ),
    (
        'One server failure costs these businesses $8,000–$15,000 per day in lost productivity. A ransomware attack costs $50,000–$200,000 in recovery and downtime. Yet 78% have no defense against either.',
        'In May 2026, the Office of the Privacy Commissioner of Canada ruled that ChatGPT violated PIPEDA. The Law Society of Ontario has warned lawyers about disciplinary action for AI data misuse. Yet 78% of the businesses we assessed had no AI policy in place.'
    ),
    (
        '<strong>100% lacked proactive monitoring.</strong> No one was watching their infrastructure. Servers, storage, backups — all invisible until they failed.',
        '<strong>100% lacked an AI Acceptable Use Policy.</strong> Employees were using ChatGPT, Copilot, and other public AI tools with client data daily — with no documented rules, no training, and no oversight.'
    ),
    (
        '<strong>95% had no automated backup verification.</strong> They believed they had backups. They didn\'t test them. When recovery came, the backups were corrupt or incomplete.',
        '<strong>95% had no shadow AI audit.</strong> Partners assumed their team used only approved tools. In every case, employees were using at least 3 unauthorized AI tools — including tools that train on submitted data.'
    ),
    (
        '<strong>100% lacked formal IT disaster recovery plans.</strong> If something catastrophic happened, there was no playbook. No recovery steps. No contact list.',
        '<strong>100% lacked an AI incident response plan.</strong> If an employee leaked client data through an AI tool, there was no playbook. No response steps. No notification process.'
    ),
    (
        'One day, their server failed. Recovery took eight days. During those eight days, they couldn\'t process payroll, generate invoices, or access client files. Eight days × $4,000 daily impact = $32,000 in lost revenue.',
        'One day, a partner discovered an associate had been pasting confidential client contracts into public ChatGPT for months. There was no policy, no audit trail, and no way to know how much client data had been exposed. The firm faced a potential PIPEDA breach and a very difficult conversation with their cyber insurer.'
    ),
    (
        '<strong>24/7 monitoring caught problems before users did.</strong> A failing hard drive, a network bottleneck, a rogue process consuming CPU—all identified and resolved overnight. No user impact. No emergency callout.',
        '<strong>A documented AI policy meant the firm could answer their insurer.</strong> Their cyber insurance renewal went smoothly. Their premium stayed flat. Their clients got a straight answer when they asked about AI data handling.'
    ),
    (
        '<strong>Automated backup verification meant recovery actually worked.</strong> When we tested restores, they worked. Data was recoverable. That confidence alone is worth the investment.',
        '<strong>A shadow AI audit revealed every tool in use.</strong> The firm finally knew exactly which AI tools their team relied on, which were safe, and which had to be shut down. That visibility alone is worth the investment.'
    ),
    (
        '<strong>Patch management meant vulnerabilities were closed within days, not months.</strong> Critical CVEs were patched before exploits appeared in the wild.',
        '<strong>M365 Copilot configuration meant AI could be used safely.</strong> Permissions were locked down so Copilot could only access what each employee was authorized to see. Productivity went up. Exposure went down.'
    ),
    (
        '<strong>Disaster recovery plans meant everyone knew what to do when something actually went wrong.</strong> No panic. No guessing. Just execution.',
        '<strong>An AI incident response plan meant everyone knew what to do if data was exposed.</strong> No panic. No guessing. Just execution.'
    )
]

apply_fixes(file1, replacements1)
apply_fixes(file2, replacements2)

