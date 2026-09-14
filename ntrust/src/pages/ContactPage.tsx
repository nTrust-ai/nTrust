import React, { useState } from 'react';

/**
 * ContactForm Component
 * 
 * Implements PROD-SPINE CTA Alignment Standard v1.0:
 * - Mailto-free (routes intent through form)
 * - Resolvable target (/contact)
 */

export const ContactForm: React.FC = () => {
  const [status, setStatus] = useState<'idle' | 'sending' | 'success' | 'error'>('idle');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus('sending');
    // Simulate form submission
    setTimeout(() => {
      setStatus('success');
    }, 1500);
  };

  return (
    <section id="contact" className="contact-page">
      <div className="container">
        <h1>Contact nTrust.ai</h1>
        <p>For security inquiries, partnerships, or service requests.</p>
        
        {status === 'success' ? (
          <div className="alert alert-success">
            Thank you for your message. Our team will respond within 24 hours.
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="contact-form">
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input type="text" id="name" name="name" required />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input type="email" id="email" name="email" required />
            </div>
            <div className="form-group">
              <label htmlFor="message">Message</label>
              <textarea id="message" name="message" rows={5} required />
            </div>
            <button type="submit" disabled={status === 'sending'}>
              {status === 'sending' ? 'Sending...' : 'Send Message'}
            </button>
          </form>
        )}
      </div>
    </section>
  );
};

export default ContactForm;