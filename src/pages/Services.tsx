import React from 'react';

const Services: React.FC = () => {
  const services = [
    { title: 'NIST AI RMF Compliance', desc: 'Automated audit trails and risk modeling aligned with NIST standards.' },
    { title: 'Zero-Trust Architecture', desc: 'End-to-end security hardening for cloud-native environments.' },
    { title: 'Threat Intelligence', desc: 'Real-time monitoring and proactive vulnerability assessments.' },
  ];

  return (
    <section className="page-section services-section" aria-labelledby="services-heading">
      <div className="container">
        <h2 id="services-heading">Our Services</h2>
        <div className="services-grid">
          {services.map((svc, i) => (
            <article key={i} className="service-card">
              <h3>{svc.title}</h3>
              <p>{svc.desc}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Services;
