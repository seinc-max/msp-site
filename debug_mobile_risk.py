import re

with open('/opt/data/msp-site/risk-assessment.html', 'r') as f:
    html = f.read()

# Apply the same JS refactor to the generic risk assessment page
js_fix = """
<script>
    const steps = [
        document.getElementById('step-1'),
        document.getElementById('step-2'),
        document.getElementById('step-3'),
        document.getElementById('step-4')
    ];
    const progressBar = document.getElementById('progress-bar');
    const form = document.getElementById('risk-assessment-form');

    document.addEventListener("DOMContentLoaded", () => {
        steps.forEach(s => s.classList.remove('active'));
        steps[0].classList.add('active');
        steps[0].style.display = 'block';
    });

    function handleSelection(stepNumber, isSafe, labelElement) {
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

        setTimeout(() => {
            currentStep.classList.remove('active');
            setTimeout(() => {
                currentStep.style.display = 'none';
                if(stepNumber < 4) {
                    steps[stepNumber].style.display = 'block';
                    void steps[stepNumber].offsetWidth;
                    steps[stepNumber].classList.add('active');
                    if(progressBar) progressBar.style.width = ((stepNumber + 1) * 25) + '%';
                    
                    if (window.innerWidth < 640) {
                        const topPos = document.getElementById('form-container').getBoundingClientRect().top + window.scrollY - 100;
                        window.scrollTo({top: topPos, behavior: 'smooth'});
                    }
                }
            }, 50);
        }, 400);
    }

    form?.addEventListener('submit', async function(e) {
        e.preventDefault();
        const btn = document.getElementById('submit-btn');
        const btnText = document.getElementById('btn-text');
        
        const q1 = form.querySelector('input[name="q1"]:checked')?.value || '';
        const q2 = form.querySelector('input[name="q2"]:checked')?.value || '';
        const q3 = form.querySelector('input[name="q3"]:checked')?.value || '';
        const email = document.getElementById('work-email').value;
        const businessSize = document.getElementById('business-size').value;
        
        btn.disabled = true;
        btnText.innerText = 'Calculating Liability...';
        btn.style.opacity = '0.8';

        const payload = {
            fields: [
                { name: 'email', value: email },
                { name: 'company_size', value: businessSize },
                { name: 'ai_policy_status', value: q1 },
                { name: 'shadow_ai_usage', value: q2 },
                { name: 'client_data_consent', value: q3 },
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
                alert('Connection issue submitting your audit. Please try again.');
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
html = re.sub(r'<script>\s*const steps = \[.*?</script>', js_fix, html, flags=re.DOTALL)

with open('/opt/data/msp-site/risk-assessment.html', 'w') as f:
    f.write(html)

print("Rewrote mobile JS logic for main risk page.")
