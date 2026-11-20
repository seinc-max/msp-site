#!/usr/bin/env python3
"""Source for assets/2026-pipeda-compliance-guide.pdf (ReportLab).

Created 2026-11-20 (release m). The original Oct 15 PDF was made with ReportLab but its
script was never saved; this file reproduces its layout (letter, 0.75in side / 0.7in top and
bottom margins, Times 10.5/14 body, navy #1a2744, orange #f97316) and is now the source of truth.
Edit CONTENT below, then run:  python3 scripts/pdf/build-pipeda-guide.py
(needs: pip install reportlab)
"""
import os
from reportlab import rl_config
rl_config.invariant = 1  # reproducible bytes
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph

NAVY, ORANGE, MUTED = HexColor('#1a2744'), HexColor('#f97316'), HexColor('#5a6a8a')
S = {
    'brand': ParagraphStyle('brand', fontName='Times-Bold', fontSize=14, leading=12, textColor=ORANGE, spaceAfter=2),
    'title': ParagraphStyle('title', fontName='Times-Bold', fontSize=18, leading=22, textColor=NAVY, spaceAfter=6),
    'sub':   ParagraphStyle('sub', fontName='Times-Italic', fontSize=11, leading=14, textColor=MUTED, spaceAfter=8),
    'h':     ParagraphStyle('h', fontName='Times-Bold', fontSize=13, leading=12, textColor=NAVY, spaceBefore=12, spaceAfter=6),
    'body':  ParagraphStyle('body', fontName='Times-Roman', fontSize=10.5, leading=14, textColor=NAVY, spaceAfter=8),
    'foot':  ParagraphStyle('foot', fontName='Times-Roman', fontSize=8.5, leading=11, textColor=MUTED),
}
CONTENT = [
    ('brand', 'TRUELINE IT'),
    ('title', '2026 PIPEDA Compliance Guide'),
    ('sub', 'Is your business actually PIPEDA compliant?'),
    ('body', 'Trueline IT  |  Published 2026'),
    ('h', 'Executive summary'),
    ('body', 'If your business collects customer data in its commercial work — names, emails, phone numbers, IP addresses, purchase history, or financial data — the Personal Information Protection and Electronic Documents Act (PIPEDA) likely applies to you.'),
    ('body', 'This guide explains what PIPEDA requires, walks through the 10 core principles, identifies the most common compliance gaps we see, and lays out a practical, ten-step path to compliance.'),
    ('h', 'What PIPEDA is, and who it applies to'),
    ('body', "PIPEDA is Canada's federal privacy law governing how for-profit organizations collect, use, and disclose personal information. Personal information includes any data that identifies an individual or could reasonably identify them. It does not apply to information held purely for personal, family, or household purposes, but the personal information you handle in your commercial work usually is."),
    ('h', 'The 10 core PIPEDA principles'),
    ('body', '<b>1. Accountability.</b> Designate a privacy officer and document your privacy practices. You must be able to demonstrate compliance.'),
    ('body', '<b>2. Identifying purposes.</b> Be clear about why you collect data before you collect it. Vague or undisclosed purposes violate PIPEDA.'),
    ('body', "<b>3. Consent.</b> Obtain explicit, informed consent from individuals before collecting or using their data. Pre-ticked boxes don't count."),
    ('body', '<b>4. Limiting collection.</b> Collect only the personal information you actually need for the stated purpose. Don\'t collect "just in case."'),
    ('body', '<b>5. Limiting use.</b> Use data only for the purposes disclosed at collection. Any new use requires fresh consent.'),
    ('body', '<b>6. Accuracy.</b> Keep personal information accurate, complete, and up-to-date. Stale data is a compliance violation.'),
    ('body', '<b>7. Safeguarding.</b> Apply technical, physical, and organizational measures to protect data: encryption, access controls, and breach protocols.'),
    ('body', '<b>8. Openness.</b> Make privacy practices transparent and accessible. Your policy must be easy to find and understand.'),
    ('body', '<b>9. Individual access.</b> Allow individuals to access their personal information and request corrections where inaccurate.'),
    ('body', '<b>10. Challenging compliance.</b> Provide a process to file privacy complaints and challenge your compliance. You need a mechanism to handle disputes.'),
    ('h', 'Where businesses fall short'),
    ('body', 'In our 2026 assessment of 20 businesses across legal, accounting, financial, and healthcare sectors, we found the same gaps recurring:'),
    ('body', "<b>No documented privacy policy.</b> Without one, you can't show a policy that holds up to scrutiny."),
    ('body', '<b>Inadequate consent.</b> Data is collected without clear, documented consent mechanisms.'),
    ('body', '<b>Unencrypted data.</b> Customer databases, shared passwords, and missing role-based access controls leave data exposed.'),
    ('body', '<b>Indefinite retention.</b> Data is held forever without a documented justification or deletion schedule.'),
    ('body', '<b>No breach protocol.</b> Most firms lack procedures for detecting, investigating, and reporting breaches, which is itself a legal requirement.'),
    ('body', "<b>No staff training.</b> Employees aren't trained on privacy obligations or how to handle sensitive data securely."),
    ('h', '10 steps to PIPEDA compliance'),
    ('body', '1. Conduct a privacy audit. Map every type of personal data you collect, where it lives, who accesses it, and how long you keep it.'),
    ('body', '2. Document your privacy practices. Publish a clear, plain-language privacy policy, easy to find on your website.'),
    ('body', '3. Implement consent processes. Obtain explicit, informed consent for all data collection and honor opt-outs immediately.'),
    ('body', '4. Encrypt sensitive data in transit (HTTPS) and at rest, including customer databases and backups.'),
    ('body', '5. Limit access with role-based access controls and multi-factor authentication, and log who touches what data.'),
    ('body', '6. Create a data retention schedule. Define how long each data type is kept, then securely delete it on expiry.'),
    ('body', '7. Establish a breach response plan: detection, investigation, documentation, and reporting.'),
    ('body', '8. Train your team. Annual privacy training so staff can identify and handle sensitive data correctly.'),
    ('body', '9. Appoint a privacy officer, someone accountable for oversight, complaints, and audits.'),
    ('body', '10. Review annually. Audit compliance at least once a year and update as the business evolves.'),
    ('h', "What happens if you don't comply"),
    ('body', "The Privacy Commissioner of Canada takes violations seriously. Non-compliance can lead to formal complaints, investigations, reputational damage, and liability for breaches. The Commissioner makes findings and recommendations; binding orders come from the Federal Court. In B.C. and Alberta, the privacy commissioner can issue binding orders, and Quebec's Commission d'accès à l'information can order fixes and impose penalties. Privacy regulators and the Canadian Centre for Cyber Security publish guidance that courts and insurers increasingly weigh."),
    ('h', 'How Trueline IT helps'),
    ('body', "Compliance doesn't have to be overwhelming. We help you assess current practices, build documented PIPEDA-aligned policies, implement encryption and access controls, define retention schedules, create breach-response procedures, and train staff, then keep it current with annual audits."),
    ('body', 'Trueline AI governance retainers are <b>$2,500/month, no setup fee</b>, covering your AI acceptable use policy, shadow AI audit, M365 configuration, and insurer-ready compliance documentation. No per-seat billing.'),
    ('foot', '© 2026 Trueline IT — 1250 Brant Street, Suite 400, Burlington, ON L7P 1X8<br/>hello@truelineit.com  |  (647) 360-5774  |  truelineit.com'),
]

def build(path):
    doc = SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=50.4, bottomMargin=50.4,
                            title='2026 PIPEDA Compliance Guide', author='Trueline IT')
    doc.build([Paragraph(t, S[s]) for s, t in CONTENT])

if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(root, 'assets', '2026-pipeda-compliance-guide.pdf')
    build(out); print('wrote', out)
