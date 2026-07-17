import re

with open('/opt/data/msp-site/ai-consulting-pricing.html', 'r') as f:
    current_html = f.read()

# 1. Restore the JSON-LD FAQ Schema
faq_schema = """
<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://truelineit.com"}]}</script>
<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "FAQPage",
 "mainEntity": [
 {
 "@type": "Question",
 "name": "What size businesses do you work with?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "We specialise in professional services businesses with 15 to 150 employees — legal, accounting, financial advisory, healthcare, and consulting. If you handle confidential client data and have no internal IT department, you're exactly who we built this for."
 }
 },
 {
 "@type": "Question",
 "name": "What does flat rate actually mean?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "You pay a fixed monthly fee — not per user. It doesn't matter if you add two people or ten. Your bill is the same every month. No surprise invoices, no per-seat charges, no enterprise consulting retainers."
 }
 },
 {
 "@type": "Question",
 "name": "What if we already have some AI tools in place?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "Even better. We audit what you already have, identify what's creating risk, configure what's safe, and shut down what isn't. You keep the tools your team loves — just without the liability."
 }
 },
 {
 "@type": "Question",
 "name": "How fast do you respond when something breaks?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "For AI policy questions, compliance queries, and automation support we respond within one business day. For urgent issues we respond within 15 minutes during business hours. You will always hear back from a real person who knows your business."
 }
 },
 {
 "@type": "Question",
 "name": "Is there a contract?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "Month-to-month. We earn your business every month. If you're not happy, you can cancel with 30 days notice — no penalties, no drama."
 }
 },
 {
 "@type": "Question",
 "name": "Do you help with AI tools like ChatGPT and Microsoft Copilot?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "Yes. We assess which AI tools are safe for your business, set up usage policies, configure permissions in M365, and automate workflows using AI — all included depending on your plan."
 }
 },
 {
 "@type": "Question",
 "name": "What is an AI privacy risk assessment?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "It's a structured review of every AI tool your team is using, how it handles your data, and whether your current setup creates regulatory or insurance exposure. We deliver it as a written report with a risk score and a recommended action plan. It's included as part of the onboarding process for every new client."
 }
 }
 ]
}
</script>
"""
current_html = current_html.replace('</head>', faq_schema + '</head>')


# 2. Restore the Social Proof Trust Section
social_proof_html = """
<!-- TRUST SECTION -->
<section style="background: var(--navy); padding: 80px 5%; margin-top: 20px;">
    <div class="max-w-[1000px] mx-auto text-left text-white">
        <h2 style="font-family: 'Fraunces', serif; font-size: 2.2rem; font-weight: 700; color: white; text-align: center; margin-bottom: 15px;">Trueline IT Reviews & Transparency</h2>
        <p style="color: rgba(255,255,255,0.75); font-size: 1.1rem; line-height: 1.6; text-align: center; max-width: 700px; margin: 0 auto 50px;">Before hiring an AI automation agency in Canada, many risk-aware operators search platforms to verify legitimacy. We embrace the scrutiny.</p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div style="background: rgba(255,255,255,0.06); padding: 35px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="color: #34d399; font-size: 1.2rem; letter-spacing: 2px; margin-bottom: 15px;">★★★★★</div>
                <p style="color: white; font-style: italic; line-height: 1.65; margin-bottom: 24px; font-size: 0.95rem;">"Our AI Exposure Sprint uncovered three departments using public ChatGPT for sensitive financial data. Trueline IT locked it down and implemented an internal secure proxy without disrupting our workflow. The guarantee made it a no-brainer."</p>
                <div style="font-weight: 600; font-size: 0.95rem; color: white;">Managing Partner <br><span style="font-weight: 400; color: rgba(255,255,255,0.5);">Accounting Firm</span></div>
            </div>
            
            <div style="background: rgba(255,255,255,0.06); padding: 35px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
                 <div style="color: #34d399; font-size: 1.2rem; letter-spacing: 2px; margin-bottom: 15px;">★★★★★</div>
                <p style="color: white; font-style: italic; line-height: 1.65; margin-bottom: 24px; font-size: 0.95rem;">"They are extremely clear on pricing. We knew exactly how much the AI audit would cost and what our monthly retainer would be before signing anything. No surprise per-user license fees. Finally, an IT partner that operates transparently."</p>
                <div style="font-weight: 600; font-size: 0.95rem; color: white;">COO <br><span style="font-weight: 400; color: rgba(255,255,255,0.5);">Legal Services</span></div>
            </div>
        </div>
    </div>
</section>
"""

# Inject before the Bottom CTA Section
current_html = current_html.replace('<!-- BOTTOM CTA SECTION -->', social_proof_html + '\n<!-- BOTTOM CTA SECTION -->')

with open('/opt/data/msp-site/ai-consulting-pricing.html', 'w') as f:
    f.write(current_html)

print("Restored SEO Schema and Social Proof.")
