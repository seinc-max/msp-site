import os

path = "/data/msp-site/ai-governance-guelph.html"
schema_block = """<script type="application/ld+json">
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
</head>"""

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# guelph had some legacy FAQPage schema, we need to override the block before </head>
# actually it's easier to just append this specifically to the final </head> even if it puts two FAQPages, but better to clear the old one or just append. 
# Based on the user instruction: Paste this ENTIRE block immediately BEFORE that </head> line
parts = content.rsplit("</head>", 1)
content = parts[0] + schema_block + parts[1]

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Forced Guelph")
