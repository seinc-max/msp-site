import os
import re

files_to_update = [
    "managed-it-services-burlington.html",
    "managed-it-services-hamilton.html",
    "managed-it-services-guelph.html",
    "managed-it-services-waterloo.html",
    "managed-it-services-cambridge.html",
    "managed-it-services-kitchener-waterloo.html"
]

cwd = '/data/msp-site'

for filename in files_to_update:
    filepath = os.path.join(cwd, filename)
    with open(filepath, 'r') as f:
        content = f.read()

    # FIX 11: How it works block section label
    content = re.sub(
        r'(<section[^>]*id="process"[^>]*>.*?<div class="container">.*?<div class="section-label">)(.*?)(</div>)',
        r'\1How it works\3',
        content, count=1, flags=re.DOTALL
    )

    # FIX 12: How it works title
    content = re.sub(
        r'(<section[^>]*id="process"[^>]*>.*?<h2 class="section-title">)(.*?)(</h2>)',
        r'\1From exposure to protected in 30 days.\3',
        content, count=1, flags=re.DOTALL
    )

    # FIX 13: How it works sub
    content = re.sub(
        r'(<section[^>]*id="process"[^>]*>.*?<p class="section-sub">)(.*?)(</p>)',
        r'\1We\'ve removed every barrier. Most businesses have their AI governance foundation in place within 30 days.\3',
        content, count=1, flags=re.DOTALL
    )

    # FIX 14 & 15: Step 2 title & description
    process_match = re.search(r'(<div class="process-steps">)(.*?)(</div>\s*</section>)', content, re.DOTALL)
    if process_match:
        process_html = process_match.group(2)
        
        # Step 2 replacement
        process_html = re.sub(
            r'(<div class="step-num">2</div>.*?<h3>)(.*?)(</h3>.*?<p>)(.*?)(</p>)',
            r'\1We run your AI Risk Audit\3We identify every AI tool in use, assess your data exposure, and build your AI Acceptable Use Policy. Delivered in plain English — ready for your insurer, your regulator, and your clients.\5',
            process_html, count=1, flags=re.DOTALL
        )
        
        # FIX 16 & 17: Step 3 title & description
        process_html = re.sub(
            r'(<div class="step-num">3</div>.*?<h3>)(.*?)(</h3>.*?<p>)(.*?)(</p>)',
            r'\1We manage it ongoing\3Policy updates as regulations change. New automations built on schedule. Monthly reporting. You get back to running your business with one answer ready: we have this handled.\5',
            process_html, count=1, flags=re.DOTALL
        )
        
        content = content[:process_match.start(2)] + process_html + content[process_match.end(2):]

    # FIX 18: Stats section label
    content = re.sub(
        r'(<section[^>]*id="stats"[^>]*>.*?<div class="container">.*?<div class="section-label">)(.*?)(</div>)',
        r'\1By the numbers\3',
        content, count=1, flags=re.DOTALL
    )

    # FIX 19: Stats section title
    content = re.sub(
        r'(<section[^>]*id="stats"[^>]*>.*?<h2 class="section-title">)(.*?)(</h2>)',
        r'\1Numbers we stand behind.\3',
        content, count=1, flags=re.DOTALL
    )

    # FIX 20: Stats section sub
    content = re.sub(
        r'(<section[^>]*id="stats"[^>]*>.*?<p class="section-sub">)(.*?)(</p>)',
        r'\1We hold ourselves to numbers, not promises.\3',
        content, count=1, flags=re.DOTALL
    )

    # FIX 21: Stat 4
    content = re.sub(
        r'<div class="stat-number">0</div>\s*<div class="stat-label">Long-term contracts</div>\s*<div class="stat-desc">.*?</div>',
        '<div class="stat-number">1 price</div>\n        <div class="stat-label">Per business, per month</div>\n        <div class="stat-desc">No per-seat billing. One predictable monthly fee regardless of headcount growth</div>',
        content, count=1, flags=re.DOTALL
    )
    content = re.sub( # Catch alternative wording
        r'<div class="stat-number">0</div>\s*<div class="stat-label">Contracts</div>\s*<div class="stat-desc">.*?</div>',
        '<div class="stat-number">1 price</div>\n        <div class="stat-label">Per business, per month</div>\n        <div class="stat-desc">No per-seat billing. One predictable monthly fee regardless of headcount growth</div>',
        content, count=1, flags=re.DOTALL
    )

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"[+] Applied fixes 11-21 on {filename}")

