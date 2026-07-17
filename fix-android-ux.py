import re

with open('/opt/data/msp-site/risk-assessment.html', 'r') as f:
    html = f.read()

# Completely rewrite the JS to be universally safe across Android (Chrome/Samsung Internet) and iOS
fallback_js = """
<script>
    const form = document.getElementById('risk-assessment-form');
    const steps = [
        document.getElementById('step-1'),
        document.getElementById('step-2'),
        document.getElementById('step-3'),
        document.getElementById('step-4')
    ];
    const progressBar = document.getElementById('progress-bar');
    
    // Explicitly hide everything except step 1 on load
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
        // Hide all steps
        for(let i = 0; i < steps.length; i++) {
            steps[i].style.display = 'none';
            steps[i].style.opacity = '0';
            steps[i].classList.remove('active');
        }
        
        // Show next step
        const nextStep = steps[nextIndex];
        if (nextStep) {
            nextStep.style.display = 'block';
            nextStep.classList.add('active');
            
            // Force reflow for animation
            void nextStep.offsetWidth;
            nextStep.style.opacity = '1';
            
            // Update Progress Bar
            if (progressBar) {
                progressBar.style.width = ((nextIndex + 1) * 25) + '%';
            }
            
            // Auto-scroll for mobile (check screen width)
            if (window.innerWidth <= 768) {
                const formEl = document.getElementById('form-container');
                if (formEl) {
                    const y = formEl.getBoundingClientRect().top + window.pageYOffset - 80;
                    window.scrollTo({top: y, behavior: 'smooth'});
                }
            }
        }
    }

    // Attach click listeners to all radios using event delegation
    // This is much safer on mobile browsers than inline onchange="" calls
    if (form) {
        form.addEventListener('change', function(e) {
            if(e.target && e.target.type === 'radio') {
                const radio = e.target;
                const wrapper = radio.closest('label');
                const indicator = wrapper ? wrapper.querySelector('.indicator') : null;
                const stepElement = radio.closest('.audit-step');
                const stepId = stepElement ? stepElement.id : '';
                
                // Determine current step index
                let currentIndex = 0;
                if(stepId === 'step-1') currentIndex = 0;
                else if(stepId === 'step-2') currentIndex = 1;
                else if(stepId === 'step-3') currentIndex = 2;
                else if(stepId === 'step-4') currentIndex = 3;

                // Reset siblings
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

                // Style active selection
                const isSafe = radio.value.includes('No - Blocked') || radio.value.includes('Yes - Updated') || radio.value.includes('Yes - Explicit');
                
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

                // Advance slightly delayed
                if (currentIndex < 3) {
                    setTimeout(() => {
                        advanceToStep(currentIndex + 1);
                    }, 400);
                }
            }
        });

        // Submit logic
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            const btn = document.getElementById('submit-btn');
            const btnText = document.getElementById('btn-text');
            
            const q1 = form.querySelector('input[name="q1"]:checked') ? form.querySelector('input[name="q1"]:checked').value : '';
            const q2 = form.querySelector('input[name="q2"]:checked') ? form.querySelector('input[name="q2"]:checked').value : '';
            const q3 = form.querySelector('input[name="q3"]:checked') ? form.querySelector('input[name="q3"]:checked').value : '';
            const emailEl = document.getElementById('work-email');
            const sizeEl = document.getElementById('business-size');
            
            btn.disabled = true;
            if(btnText) btnText.innerText = 'Calculating Liability...';
            btn.style.opacity = '0.8';

            const payload = {
                fields: [
                    { name: 'email', value: emailEl ? emailEl.value : '' },
                    { name: 'company_size', value: sizeEl ? sizeEl.value : '' },
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
                    if(sCont) sCont.style.display = 'block';
                    if(progressBar) {
                        progressBar.style.width = '100%';
                        progressBar.style.background = '#10b981';
                    }
                } else {
                    btn.disabled = false;
                    if(btnText) btnText.innerText = 'Book My Free Discovery Call →';
                    btn.style.opacity = '1';
                    alert('Connection issue. Please try again.');
                }
            } catch (err) {
                btn.disabled = false;
                if(btnText) btnText.innerText = 'Book My Free Discovery Call →';
                btn.style.opacity = '1';
                alert('Network error. Please try again.');
            }
        });

        // Prevent enter submit
        form.addEventListener('keydown', function(event) {
            if(event.key === 'Enter') { event.preventDefault(); }
        });
    }
</script>
"""

# Strip out inline onchange handlers that Android hates
html = re.sub(r'onchange="handleSelection\([^\)]+\)"', '', html)

# Replace the previous script block entirely
html = re.sub(r'<script>\s*const steps = \[.*?</script>', fallback_js, html, flags=re.DOTALL)

with open('/opt/data/msp-site/risk-assessment.html', 'w') as f:
    f.write(html)
print("Applied Android/Samsung browser universal JS rewrite (risk-assessment).")
