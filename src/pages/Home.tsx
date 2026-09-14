import React from 'react';

const Home: React.FC = () => {
  return (
    <section className="page-section hero-section" aria-labelledby="hero-heading">
      <div className="container">
        <h1 id="hero-heading">Enterprise-Grade AI Security & Compliance</h1>
        <p className="lead-text">Protect your infrastructure with nTrust's zero-trust architecture, automated compliance auditing, and proactive threat intelligence.</p>
        <div className="cta-group">
          <a href="/services" className="btn btn-primary">View Our Services</a>
          <a href="/contact" className="btn btn-secondary">Request a Demo</a>
        </div>
      </div>
    </section>
  );
};

export default Home;
