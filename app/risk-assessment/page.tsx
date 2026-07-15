'use client';
import Head from 'next/head';
import { useState } from 'react';

export default function RiskAssessment() {
  const [formData, setFormData] = useState({
    q1: '',
    q2: '',
    q3: '',
    email: '',
    firmSize: '1-14 Employees'
  });
  const [status, setStatus] = useState('idle');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus('submitting');

    const payload = {
      fields: [
        { name: 'email', value: formData.email },
        { name: 'company_size', value: formData.firmSize },
        { name: 'ai_policy_status', value: formData.q1 },
        { name: 'shadow_ai_usage', value: formData.q2 },
        { name: 'client_data_consent', value: formData.q3 },
        { name: 'hubspot_owner_id', value: '89556230' }
      ]
    };

    try {
      const response = await fetch('https://api.hsforms.com/submissions/v3/integration/submit/343087614/e66cbddb-8b74-4166-ab13-6ea81df11466', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (response.ok) setStatus('success');
      else setStatus('error');
    } catch (err) {
      setStatus('error');
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 font-sans">
      <Head>
        <title>2026 AI Privacy Risk Assessment | Trueline IT</title>
        <meta name="description" content="Ontario professional services firms: Calculate your Shadow AI liability under OPC rulings and Law Society guidelines." />
      </Head>

      {/* Hero Section */}
      <div className="bg-slate-900 text-white pb-20 pt-16 px-6">
        <div className="max-w-5xl mx-auto">
          <div className="inline-block px-3 py-1 bg-red-500/20 text-red-300 rounded-full text-sm font-semibold tracking-wide mb-6 border border-red-500/30">
            URGENT FOR ONTARIO FIRMS
          </div>
          <h1 className="text-4xl md:text-6xl font-extrabold mb-6 leading-tight tracking-tight">
            Stop the Bleeding: Find Your <br className="hidden md:block"/> "Shadow AI" Liability Score inside 3 Minutes.
          </h1>
          <p className="text-xl text-slate-300 max-w-3xl mb-8 leading-relaxed">
            The Office of the Privacy Commissioner has explicitly ruled on unauthorized AI use under PIPEDA. The Law Society of Ontario is warning about client privilege. 
            <strong> If you don't have a documented AI Acceptable Use policy, cyber insurers are now treating you as a high-risk liability.</strong>
          </p>
          <div className="flex items-center space-x-4 text-sm text-slate-400 font-medium pb-8">
            <span className="flex items-center"><svg className="w-5 h-5 mr-2 text-blue-400" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd"></path></svg> Based on 2026 OPC Rulings</span>
            <span className="flex items-center"><svg className="w-5 h-5 mr-2 text-blue-400" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd"></path></svg> 100% Confidential</span>
          </div>
        </div>
      </div>

      <main className="max-w-5xl mx-auto px-6 -mt-10 mb-20 relative">
        <div className="bg-white rounded-xl shadow-[0_20px_50px_-12px_rgba(0,0,0,0.1)] border border-gray-200 overflow-hidden flex flex-col md:flex-row">
          
          {/* Form Side */}
          <div className="p-8 md:p-12 w-full md:w-2/3">
            {status === 'success' ? (
              <div className="text-center py-16">
                <svg className="w-20 h-20 text-green-500 mx-auto mb-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                <h2 className="text-3xl font-bold text-slate-900 mb-4">Risk Audit Received</h2>
                <p className="text-lg text-slate-600">We are processing your answers against current PIPEDA and Law Society frameworks. Check your inbox in a few minutes for your comprehensive risk report.</p>
              </div>
            ) : (
              <form id="risk-assessment-form" className="space-y-10" onSubmit={handleSubmit}>
                <div className="pt-2 pb-6 border-b border-gray-100">
                  <h2 className="text-2xl font-bold text-slate-900">Confidential Audit</h2>
                  <p className="text-slate-500 mt-2">Answer honestly. We never share this data.</p>
                </div>

                <div className="space-y-4">
                  <label className="block text-lg font-bold text-slate-800">1. Does your firm currently have a formally documented AI Acceptable Use Policy signed by all employees?</label>
                  <p className="text-sm text-slate-500 mb-2">Insurers look for a paper trail proving you attempted to govern staff.</p>
                  <div className="space-y-3">
                    <label className="flex items-start space-x-3 p-4 rounded-lg border border-gray-200 hover:bg-slate-50 hover:border-blue-300 cursor-pointer transition">
                      <input type="radio" name="q1" value="Yes - Updated" required onChange={(e) => setFormData({...formData, q1: e.target.value})} className="mt-1 form-radio text-blue-600 w-5 h-5" />
                      <span className="font-medium text-slate-700">Yes, active and updated within the last 12 months.</span>
                    </label>
                    <label className="flex items-start space-x-3 p-4 rounded-lg border border-red-200 hover:bg-red-50 cursor-pointer transition">
                      <input type="radio" name="q1" value="No / Drafting" required onChange={(e) => setFormData({...formData, q1: e.target.value})} className="mt-1 form-radio text-red-600 w-5 h-5" />
                      <span className="font-medium text-slate-700">No, or we are drafting one now. (Warning: High Liability)</span>
                    </label>
                  </div>
                </div>

                <div className="space-y-4">
                  <label className="block text-lg font-bold text-slate-800">2. To your knowledge, have employees ever used a free-tier public AI (like ChatGPT, Gemini, or Claude) to summarize documents, draft emails, or analyze spreadsheets?</label>
                  <p className="text-sm text-slate-500 mb-2">Free-tier tools train their models on your inputs, resulting in an automatic breach of confidentiality.</p>
                  <div className="space-y-3">
                    <label className="flex items-start space-x-3 p-4 rounded-lg border border-red-200 hover:bg-red-50 cursor-pointer transition">
                      <input type="radio" name="q2" value="Yes" required onChange={(e) => setFormData({...formData, q2: e.target.value})} className="mt-1 form-radio text-red-600 w-5 h-5" />
                      <span className="font-medium text-slate-700">Yes, I am aware this happens.</span>
                    </label>
                    <label className="flex items-start space-x-3 p-4 rounded-lg border border-orange-200 hover:bg-orange-50 cursor-pointer transition">
                      <input type="radio" name="q2" value="Likely" required onChange={(e) => setFormData({...formData, q2: e.target.value})} className="mt-1 form-radio text-orange-600 w-5 h-5" />
                      <span className="font-medium text-slate-700">I'm not sure, but it is highly likely.</span>
                    </label>
                    <label className="flex items-start space-x-3 p-4 rounded-lg border border-gray-200 hover:bg-slate-50 hover:border-blue-300 cursor-pointer transition">
                      <input type="radio" name="q2" value="No - Blocked" required onChange={(e) => setFormData({...formData, q2: e.target.value})} className="mt-1 form-radio text-blue-600 w-5 h-5" />
                      <span className="font-medium text-slate-700">Absolutely not. We have technical network blocks in place to prevent access.</span>
                    </label>
                  </div>
                </div>

                <div className="space-y-4">
                  <label className="block text-lg font-bold text-slate-800">3. Have you updated your client privacy notices to explicitly disclose the use of AI in your firm's workflows?</label>
                  <p className="text-sm text-slate-500 mb-2">The OPC recently mandated that relying on a generic "we use tech tools" clause does not meet the standard for Meaningful Consent under PIPEDA when deploying generative AI.</p>
                  <div className="space-y-3">
                    <label className="flex items-start space-x-3 p-4 rounded-lg border border-gray-200 hover:bg-slate-50 hover:border-blue-300 cursor-pointer transition">
                      <input type="radio" name="q3" value="Yes - Explicit" required onChange={(e) => setFormData({...formData, q3: e.target.value})} className="mt-1 form-radio text-blue-600 w-5 h-5" />
                      <span className="font-medium text-slate-700">Yes, our engagements explicitly outline AI usage and data-handling limitations.</span>
                    </label>
                    <label className="flex items-start space-x-3 p-4 rounded-lg border border-red-200 hover:bg-red-50 cursor-pointer transition">
                      <input type="radio" name="q3" value="No - Implicit" required onChange={(e) => setFormData({...formData, q3: e.target.value})} className="mt-1 form-radio text-red-600 w-5 h-5" />
                      <span className="font-medium text-slate-700">No, we have not specifically addressed AI in our client agreements yet.</span>
                    </label>
                  </div>
                </div>

                <div className="pt-8 border-t border-gray-200 bg-slate-50 -mx-8 sm:-mx-12 px-8 sm:px-12 pb-8 sm:pb-12 mt-8">
                  <h3 className="text-xl font-bold text-slate-900 mb-2">Request Your Incident Report</h3>
                  <p className="text-sm text-slate-600 mb-6">Enter your details below to generate your score. Your custom report will detail exactly what your cyber insurer and the Law Society will demand from you in 2026.</p>
                  
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Work Email *</label>
                      <input type="email" required value={formData.email} onChange={(e) => setFormData({...formData, email: e.target.value})} className="w-full bg-white border border-gray-300 rounded-lg px-4 py-3 text-slate-900 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" placeholder="managingpartner@firm.ca" />
                    </div>
                    <div>
                      <label className="block text-sm font-bold text-slate-700 mb-2">Firm Size</label>
                      <select value={formData.firmSize} onChange={(e) => setFormData({...formData, firmSize: e.target.value})} className="w-full bg-white border border-gray-300 rounded-lg px-4 py-3 text-slate-900 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        <option value="1-14 Employees">1-14 Employees</option>
                        <option value="15-50 Employees">15-50 Employees</option>
                        <option value="51-150 Employees">51-150 Employees</option>
                      </select>
                    </div>
                  </div>
                  
                  <button 
                    type="submit" 
                    disabled={status === 'submitting'}
                    className="w-full bg-blue-700 hover:bg-blue-800 disabled:bg-slate-400 text-white font-bold py-4 rounded-lg text-lg transition shadow-lg hover:shadow-xl"
                  >
                    {status === 'submitting' ? 'Processing Governance Audit...' : "Generate My Liability Score"}
                  </button>
                  {status === 'error' && <p className="text-red-500 mt-4 text-center font-medium">There was a server issue submitting your audit. Please try again.</p>}
                  <p className="text-xs text-center text-slate-400 mt-4">By generating a score, you consent to Trueline IT securely processing this data to calculate your risk.</p>
                </div>

              </form>
            )}
          </div>

          {/* Social Proof Side */}
          <div className="w-full md:w-1/3 bg-slate-50 border-l border-gray-200 p-8">
            <h3 className="text-sm font-bold uppercase tracking-wider text-slate-400 mb-6">Why Take The Audit?</h3>
            
            <div className="space-y-6">
              <div className="flex">
                <div className="flex-shrink-0 mt-1"><svg className="w-6 h-6 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg></div>
                <div className="ml-4">
                  <h4 className="text-base font-bold text-slate-900">The OPC Ruling</h4>
                  <p className="text-sm text-slate-600 mt-1">In May 2026, the Office of the Privacy Commissioner ruled that unmanaged ChatGPT usage violates PIPEDA and Quebec Law 25 confidentiality laws.</p>
                </div>
              </div>

              <div className="flex">
                <div className="flex-shrink-0 mt-1"><svg className="w-6 h-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg></div>
                <div className="ml-4">
                  <h4 className="text-base font-bold text-slate-900">Insurance Renewals</h4>
                  <p className="text-sm text-slate-600 mt-1">Cyber insurers now explicitly deny coverage to firms lacking a documented AI Acceptable Use Policy in the event of an AI-originating payload breach.</p>
                </div>
              </div>

              <div className="flex">
                <div className="flex-shrink-0 mt-1"><svg className="w-6 h-6 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg></div>
                <div className="ml-4">
                  <h4 className="text-base font-bold text-slate-900">Law Society Warnings</h4>
                  <p className="text-sm text-slate-600 mt-1">The LSO warns that using free-tier public AI tools with client data is an actionable breach of client privilege. You are responsible for your staff's tools.</p>
                </div>
              </div>

            </div>

            <div className="mt-10 p-5 bg-blue-50 border border-blue-100 rounded-lg">
              <p className="text-sm italic text-slate-700">"We thought our staff knew better than to put client PDFs into ChatGPT. The audit Trueline ran proved otherwise. Getting the formalized policy in place saved our cyber renewal."</p>
              <p className="text-xs font-bold text-slate-900 mt-3">— Managing Partner, Toronto Firm</p>
            </div>
          </div>

        </div>
      </main>
    </div>
  );
}
