import sys
import re

file_path = "/data/msp-site/health-score.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Title, Meta Description, Keywords
content = re.sub(r'<title>.*?</title>', '<title>AI Exposure Health Score & Readiness Audit | Trueline IT</title>', content)
content = re.sub(r'<meta name="description" content=".*?" />', '<meta name="description" content="Free AI exposure and automation readiness diagnostic for Ontario professionals. Find out your company\'s Shadow AI risk score in 3 minutes." />', content)
content = re.sub(r'<meta name="keywords" content=".*?" />', '<meta name="keywords" content="AI readiness audit, AI exposure score, shadow AI risk assessment, ChatGPT compliance check, AI automation readiness" />', content)

# 2. Update Open Graph Data
content = re.sub(r'<meta property="og:title" content=".*?" />', '<meta property="og:title" content="Free AI Exposure Health Score | Trueline IT" />', content)
content = re.sub(r'<meta property="og:description" content=".*?" />', '<meta property="og:description" content="Find out your company\'s Shadow AI risk and automation readiness in 3 minutes." />', content)
content = re.sub(r'<meta name="twitter:title" content=".*?" />', '<meta name="twitter:title" content="Free AI Exposure Health Score | Trueline IT" />', content)
content = re.sub(r'<meta name="twitter:description" content=".*?" />', '<meta name="twitter:description" content="Find out your company\'s Shadow AI risk and automation readiness in 3 minutes." />', content)


# 3. Update Hero Section
content = content.replace(
    '<div class="hero-pre">15-minute diagnostic</div>', 
    '<div class="hero-pre">3-minute diagnostic</div>'
)
content = content.replace(
    '<h1>Is Your IT Setup<br>Holding You Back?</h1>', 
    '<h1>Is Shadow AI Already<br>Leaking Your Data?</h1>'
)
content = content.replace(
    '<p class="hero-sub">Most businesses only think about IT when something breaks. But poor security, outdated systems, and unverified backups are silent killers. Take our free 15-question diagnostic to see exactly where your business is exposed—and what you need to fix it.</p>', 
    '<p class="hero-sub">Most businesses only think about AI when an employee asks to buy a tool. But unauthorized usage, unverified data policies, and lack of DLP controls are silent liability engines. Take our free 3-minute diagnostic to see exactly where your business is exposed—and how ready you are for automation.</p>'
)

# 4. Form questions
content = content.replace(
    '<p style="font-weight:700;color:#1a2744;font-size:1.1rem;margin-bottom:20px;">Book a Health Score review call</p>',
    '<p style="font-weight:700;color:#1a2744;font-size:1.1rem;margin-bottom:20px;">Book your AI Risk Audit</p>'
)

# Replace general references to "IT Health Score"
content = content.replace("IT Health Score", "AI Exposure Score")

# Update contact sub
content = content.replace(
    '<p class="contact-sub">Tell us a bit about your business and we\'ll be in touch within one business day.</p>',
    '<p class="contact-sub">Get your personalized AI exposure and automation readiness roadmap.</p>'
)
# Update bottom CTA text
content = content.replace(
    '<p style="font-weight:700;color:#fff;font-size:1.1rem;margin-bottom:20px;">Get your comprehensive Trueline IT Health Score — no sales pitch, just data.</p>',
    '<p style="font-weight:700;color:#fff;font-size:1.1rem;margin-bottom:20px;">Get your comprehensive AI Exposure Score — no sales pitch, just data.</p>'
)


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

