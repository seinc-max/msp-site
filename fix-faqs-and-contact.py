import re
import os

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

    # FIX 24: FAQ questions (Proper replacement including creating missing blocks)
    new_faq_html = """    <div class="faq-list">
      <details>
        <summary>What size businesses do you work with?</summary>
        <p class="faq-answer">We partner with professional service businesses (legal, accounting, financial, consulting) and select manufacturing operations that handle sensitive intellectual property and client data.</p>
      </details>
      <details>
        <summary>What does "flat rate" actually mean?</summary>
        <p class="faq-answer">It means zero surprise invoices. Whether we are conducting your quarterly shadow AI audit, updating your policies for new regulations, or rolling out Microsoft Copilot, your monthly fee covers it. No per-hour overages.</p>
      </details>
      <details>
        <summary>What if we already have some AI tools in place?</summary>
        <p class="faq-answer">Perfect. We audit them. If they are safe and enterprise-grade, we document them in your Acceptable Use Policy. If they are publicly training on your data, we migrate you to private alternatives.</p>
      </details>
      <details>
        <summary>How fast do you respond when something breaks?</summary>
        <p class="faq-answer">We are based locally in Southern Ontario and guarantee a 15-minute response time for critical issues. You get direct access to our team—no overseas call centres, no endless ticketing loops.</p>
      </details>
      <details>
        <summary>Is there a contract?</summary>
        <p class="faq-answer">No long-term lock-ins. Our agreements are month-to-month. If we aren't delivering clear ROI and keeping your data safe, you can walk away at any time.</p>
      </details>
      <details>
        <summary>Do you help with AI tools like ChatGPT and Microsoft Copilot?</summary>
        <p class="faq-answer">Yes, this is our core focus. We establish private, enterprise-grade instances of these tools ensuring that your employee inputs and client data are never used to train public models.</p>
      </details>
      <details>
        <summary>What is an AI privacy risk assessment?</summary>
        <p class="faq-answer">Our assessment acts as an x-ray of your network. We find exactly what AI tools your staff are using behind your back, categorize the data leakage risk, and provide a roadmap to secure it.</p>
      </details>
    </div>"""

    content = re.sub(
        r'<div class="faq-list">.*?</div>\s*</section>',
        new_faq_html + '\n  </div>\n</section>',
        content,
        flags=re.DOTALL
    )

    # FIX 25: Contact section label
    content = re.sub(
        r'(<section[^>]*class="contact-section"[^>]*>\s*)<p class="section-label">[^<]*</p>',
        r'\1<p class="section-label">Start here</p>',
        content
    )

    # FIX 26: Contact section title
    content = re.sub(
        r'(<section[^>]*class="contact-section"[^>]*>.*?<p class="section-label">Start here</p>\s*)<h2>[^<]*</h2>',
        r'\1<h2>Find out exactly where your business is exposed.</h2>',
        content, flags=re.DOTALL
    )

    # FIX 27: Contact section sub
    content = re.sub(
        r'(<section[^>]*class="contact-section"[^>]*>.*?<h2>Find out exactly where your business is exposed.</h2>\s*)<p class="contact-sub">[^<]*</p>',
        r'\1<p class="contact-sub">Book a 30-minute call. We will assess your AI exposure, answer your questions, and tell you exactly what needs to be done — no sales pitch, no obligation.</p>',
        content, flags=re.DOTALL
    )
    
    # Clean up the generic "Is your Southern Ontario business protected... Health Score" paragraph below contact-sub
    content = re.sub(
        r'<p style="font-weight:700;color:#fff;font-size:1.1rem;margin-bottom:20px;">[^<]*</p>',
        '',
        content
    )

    with open(filepath, 'w') as f:
        f.write(content)
        print(f"[+] Fixed FAQ & Contact sections in {filename}")

