import React from 'react';

const Contact: React.FC = () => {
  return (
    <section className="page-section contact-section" aria-labelledby="contact-heading">
      <div className="container">
        <h2 id="contact-heading">Contact Us</h2>
        <form className="contact-form" aria-label="Contact form">
          <div className="form-group">
            <label htmlFor="name">Full Name</label>
            <input type="text" id="name" name="name" required />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email Address</label>
            <input type="email" id="email" name="email" required />
          </div>
          <div className="form-group">
            <label htmlFor="message">Message</label>
            <textarea id="message" name="message" rows={5} required></textarea>
          </div>
          <button type="submit" className="btn btn-primary">Send Message</button>
        </form>
      </div>
    </section>
  );
};

export default Contact;
