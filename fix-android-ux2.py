import re

with open('/opt/data/msp-site/safe-copilot-deployment.html', 'r') as f:
    html = f.read()

fallback_js = """
<script>
    const form = document.getElementById('risk-assessment-form');
    const steps = [
        document.getElementById('step-1'),
        document.getElementById('step-2'),
        document.getElementById('step-3')
    ];
    const progressBar = document.getElementById('progress-bar');
    
    document.addEventListener("DOMContentLoaded", function() {
        for(let i = 0; i < steps.length; i++) {
            if(i === 0) {
                steps[i].style.display = 'block';
                steps[i].style.opacity = '1';
                steps[i].classList.add('active');
            } else {
                steps[i].style.display = 'none';
                steps[i].style.opacity = '0';
                steps[i].classList.remove('active');
            }
        }
    });

    function advanceToStep(nextIndex) {
        for(let i = 0; i < steps.length; i++) {
            steps[i].style.display = 'none';
            steps[i].style.opacity = '0';
            steps[i].classList.remove('active');
        }
        
        const nextStep = steps[nextIndex];
        if (nextStep) {
            nextStep.style.display = 'block';
            nextStep.classList.add('active');
            void nextStep.offsetWidth;
            nextStep.style.opacity = '1';
            
            if (progressBar) {
                progressBar.style.width = ((nextIndex + 1) * 33.3) + '%';
            }
            
            if (window.innerWidth <= 768) {
                const formEl = document.getElementById('form-container');
                if (formEl) {
                    const y = formEl.getBoundingClientRect().top + window.pageYOffset - 80;
                    window.scrollTo({top: y, behavior: 'smooth'});
                }
            }
        }
    }

    if (form) {
        form.addEventListener('change', function(e) {
            if(e.target && e.target.type === 'radio') {
                const radio = e.target;
                const wrapper = radio.closest('label');
                const indicator = wrapper ? wrapper.querySelector('.indicator') : null;
                const stepElement = radio.closest('.audit-step') || radio.closest('div[id^="step-"]');
                const stepId = stepElement ? stepElement.id : '';
                
                let currentIndex = 0;
                if(stepId === 'step-1') currentIndex = 0;
                else if(stepId === 'step-2') currentIndex = 1;
                else if(stepId === 'step-3') currentIndex = 2;

                if (stepElement) {
                    const siblingRadios = stepElement.querySelectorAll('input[type="radio"]');
                    siblingRadios.forEach(r => {
                        const w = r.closest('label');
                        if (w) {
                            w.style.borderColor = 'var(--border)';
                            w.style.background = '#fff';
                            const ind = w.querySelector('.indicator');
                            if (ind) {
                                ind.innerHTML = '';
                                ind.style.borderColor = '#cbd5e1';
                            }
                        }
                    });
                }

                const isSafe = radio.value.includes('No - Audited') || radio.value.includes('Yes - Confident');
                
                if (wrapper) {
                    if (isSafe) {
                        wrapper.style.borderColor = 'var(--blue)';
                        wrapper.style.background = 'var(--sky)';
                        if (indicator) {
                            indicator.innerHTML = '<svg class="w-3 h-3 text-blue-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>';
                            indicator.style.borderColor = 'var(--blue)';
                        }
                    } else {
                        wrapper.style.borderColor = '#ef4444';
                        wrapper.style.backgroundColor = '#fef2f2';
                        if (indicator) {
                            indicator.innerHTML = '<svg class="w-3 h-3 text-red-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>';
                            indicator.style.borderColor = '#ef4444';
                        }
                    }
                }

                if (currentIndex < 2) {
                    setTimeout(() => {
                        advanceToStep(currentIndex + 1);
                    }, 400);
                }
            }
        });

        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            const btn = document.getElementById('submit-btn');
            const btnText = document.getElementById('btn-text');
            
            const q1 = form.querySelector('input[name="q1"]:checked') ? form.querySelector('input[name="q1"]:checked').value : '';
            const q2 = form.querySelector('input[name="q2"]:checked') ? form.querySelector('input[name="q2"]:checked').value : '';
            const emailEl = document.getElementById('work-email');
            const sizeEl = document.getElementById('business-size');
            
            btn.disabled = true;
            if(btnText) btnText.innerText = 'Calculating Liability...';
            btn.style.opacity = '0.8';

            const payload = {
                fields: [
                    { name: 'email', value: emailEl ? emailEl.value : '' },
                    { name: 'company_size', value: sizeEl ? sizeEl.value : '' },
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
                    if(sCont) sCont.style.display = 'block';
                    if(progressBar) {
                        progressBar.style.width = '100%';
                        progressBar.style.background = '#10b981';
                    }
                } else {
                    btn.disabled = false;
                    if(btnText) btnText.innerText = 'Book My Free Discovery Call &rarr;';
                    btn.style.opacity = '1';
                    alert('Connection issue. Please try again.');
                }
            } catch (err) {
                btn.disabled = false;
                if(btnText) btnText.innerText = 'Book My Free Discovery Call &rarr;';
                btn.style.opacity = '1';
                alert('Network error. Please try again.');
            }
        });
    }
</script>
"""

html = re.sub(r'onchange="handleSelection\([^\)]+\)"', '', html)
html = re.sub(r'<script>\s*const steps = \[.*?</script>', fallback_js, html, flags=re.DOTALL)

with open('/opt/data/msp-site/safe-copilot-deployment.html', 'w') as f:
    f.write(html)
print("Applied Android universal rewrite (copilot).")
