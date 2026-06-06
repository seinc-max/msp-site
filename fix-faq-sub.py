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

    # The FAQ title got malformed in the last regex pass
    content = content.replace('<h2 class="section-titleYou\\\'ve probably got questions.</h2>', '<h2 class="section-title text-center">You\'ve probably got questions.</h2>')
    content = content.replace('You\\\'ve probably got questions.', 'You\'ve probably got questions.')
    content = content.replace('We\\\'ve removed every barrier.', 'We\'ve removed every barrier.')

    # Ensure FAQ answers match the 7 index.html questions correctly as specified in prompt
    # First, let's just wipe out the `faq-list` entirely and inject the correct 7
    # Note: earlier pass left existing answers. We must replace the whole faq-list to match exactly
    
    faq_replacement = """    <div class="faq-list">
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
        r'<div class="faq-list">.*?</div>\s*</div>\s*</section>',
        faq_replacement + '\n  </div>\n</section>',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    with open(filepath, 'w') as f:
        f.write(content)

