import re

with open('/opt/data/msp-site/safe-copilot-deployment.html', 'r') as f:
    html = f.read()

# Let's completely rework the inline JS animation/height logic which is notoriously buggy on mobile Safari.
# Instead of inline styles, we'll ensure the CSS handles the display toggling reliably.

css_fix = """
    <style>
        .audit-step { 
            display: none; 
            opacity: 0;
            transition: opacity 0.3s ease-in-out;
        }
        .audit-step.active { 
            display: block; 
            opacity: 1;
            animation: fadeIn 0.4s ease forwards;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .epc-card { border: 1.5px solid var(--border); transition: all 0.2s; }
        .epc-card:hover { border-color: var(--blue-light); box-shadow: 0 10px 40px -15px rgba(37,99,235,0.15); transform: translateY(-3px); }
        
        /* Mobile Specific Fixes */
        .radio-label {
            display: flex;
            align-items: flex-start;
            padding: 1.25rem;
            border-radius: 0.75rem;
            border: 1.5px solid var(--border);
            cursor: pointer;
            width: 100%;
            background: #fff;
            transition: all 0.2s ease;
        }
        @media (max-width: 640px) {
            .radio-label { padding: 1rem; }
            .radio-text-main { font-size: 0.95rem !important; }
            /* Ensure the container doesn't force a minimum height that breaks scrolling */
            #form-container { min-height: auto !important; padding-bottom: 2rem !important; }
        }
    </style>
"""

# Replace the existing style block in the <head>
html = re.sub(r'<style>\s*\.audit-step \{.*?</style>', css_fix, html, flags=re.DOTALL)

# Refactor the JS to use classList instead of fragile inline style.display manipulation
js_fix = """
<script>
    const steps = [
        document.getElementById('step-1'),
        document.getElementById('step-2'),
        document.getElementById('step-3')
    ];
    const progressBar = document.getElementById('progress-bar');
    const form = document.getElementById('risk-assessment-form');

    // Make sure Step 1 starts active immediately on load
    document.addEventListener("DOMContentLoaded", () => {
        steps.forEach(s => s.classList.remove('active'));
        steps[0].classList.add('active');
        steps[0].style.display = 'block';
    });

    function handleSelection(stepNumber, isSafe, labelElement) {
        // Reset all labels in current step
        const currentStep = steps[stepNumber - 1];
        const allLabels = currentStep.querySelectorAll('label');
        allLabels.forEach(l => {
            l.style.borderColor = 'var(--border)';
            l.style.background = '#fff';
            const ind = l.querySelector('.indicator');
            if(ind) {
                ind.innerHTML = '';
                ind.style.borderColor = '#cbd5e1';
            }
        });

        // Apply UI Feedback
        const indicator = labelElement.querySelector('.indicator');
        if (isSafe) {
            labelElement.style.borderColor = 'var(--blue)';
            labelElement.style.background = 'var(--sky)';
            if(indicator) {
                indicator.innerHTML = '<svg class="w-3 h-3 text-blue-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>';
                indicator.style.borderColor = 'var(--blue)';
            }
        } else {
            labelElement.style.borderColor = '#ef4444';
            labelElement.style.backgroundColor = '#fef2f2';
            if(indicator) {
                indicator.innerHTML = '<svg class="w-3 h-3 text-red-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>';
                indicator.style.borderColor = '#ef4444';
            }
        }

        // Advance to next step reliably using class toggles
        setTimeout(() => {
            currentStep.classList.remove('active');
            setTimeout(() => {
                currentStep.style.display = 'none';
                if(stepNumber < 3) {
                    steps[stepNumber].style.display = 'block';
                    // Force a reflow
                    void steps[stepNumber].offsetWidth;
                    steps[stepNumber].classList.add('active');
                    if(progressBar) progressBar.style.width = ((stepNumber + 1) * 33.3) + '%';
                    
                    // On mobile, scroll slightly if the next question is hidden
                    if (window.innerWidth < 640) {
                        const topPos = document.getElementById('form-container').getBoundingClientRect().top + window.scrollY - 100;
                        window.scrollTo({top: topPos, behavior: 'smooth'});
                    }
                }
            }, 50); // tiny delay to allow display:none to register
        }, 400);
    }

    form?.addEventListener('submit', async function(e) {
        e.preventDefault();
        const btn = document.getElementById('submit-btn');
        const btnText = document.getElementById('btn-text');
        
        const q1 = form.querySelector('input[name="q1"]:checked')?.value || '';
        const q2 = form.querySelector('input[name="q2"]:checked')?.value || '';
        const email = document.getElementById('work-email').value;
        const businessSize = document.getElementById('business-size').value;
        
        btn.disabled = true;
        btnText.innerText = 'Analyzing Tenant...';
        btn.style.opacity = '0.8';

        const payload = {
            fields: [
                { name: 'email', value: email },
                { name: 'company_size', value: businessSize },
                { name: 'copilot_label_audit', value: q1 },
                { name: 'copilot_folder_security', value: q2 },
                { name: 'hubspot_owner_id', value: '89556230' }
            ]
        };

        try {
            const res = await fetch('https://api.hsforms.com/submissions/v3/integration/submit/343087614/e66cbddb-8b74-4166-ab13-6ea81df11466', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            
            if (res.ok) {
                document.getElementById('form-container').style.display = 'none';
                const sCont = document.getElementById('success-container');
                sCont.style.display = 'block';
                sCont.classList.add('active');
                if(progressBar) {
                    progressBar.style.width = '100%';
                    progressBar.style.background = '#10b981';
                }
            } else {
                btn.disabled = false;
                btnText.innerText = 'Book My Free Discovery Call →';
                btn.style.opacity = '1';
                alert('Connection issue. Please try again.');
            }
        } catch (err) {
            btn.disabled = false;
            btnText.innerText = 'Book My Free Discovery Call →';
            btn.style.opacity = '1';
            alert('Network error. Please try again.');
        }
    });

    form?.addEventListener('keydown', function(event) {
        if(event.key === 'Enter') { event.preventDefault(); }
    });
</script>
"""

# Replace the old script block
html = re.sub(r'<script>\s*const steps = \[.*?</script>', js_fix, html, flags=re.DOTALL)

with open('/opt/data/msp-site/safe-copilot-deployment.html', 'w') as f:
    f.write(html)

print("Rewrote mobile JS logic.")
