import React, { useState, useEffect } from 'react';
// TASK-FD8171 / TASK-6DAC16: Website Alignment & Product Catalog Sync (Board Directive v4.1)

const CATALOG_ITEMS = [
  { id: "PROD-75052F", name: "Enterprise Security Audit", tier: "$15K / $35K / $50K", status: "Available" },
  { id: "PROD-TRUSTGUARD", name: "TrustGuard Compliance Suite", tier: "Subscription", status: "Coming Soon" },
  { id: "PROD-NIST-AI", name: "NIST AI RMF Consulting", tier: "Project-Based", status: "Available" }
];

export default function ProductCatalogSync() {
  const [products, setProducts] = useState([]);
  const [syncStatus, setSyncStatus] = useState('syncing');

  useEffect(() => {
    // Sync with internal product registry
    setProducts(CATALOG_ITEMS);
    setSyncStatus('synced');
  }, []);

  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-xl font-bold mb-4">Product & Service Catalog</h2>
      <p className="mb-4 text-sm text-gray-500">Last synced: {new Date().toLocaleString()}</p>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {products.map((item) => (
          <div key={item.id} className="border p-4 rounded-lg hover:shadow-lg transition">
            <h3 className="font-semibold">{item.name}</h3>
            <p className="text-sm text-gray-600">{item.tier}</p>
            <span className={`inline-block mt-2 px-2 py-1 text-xs rounded-full ${item.status === 'Available' ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'}`}>
              {item.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
