import React, { useEffect, useState } from 'react';

// Product Catalog Data Structure aligned with PROD-71C577 requirements
const PRODUCT_CATALOG = [
  {
    id: 'PROD-597152',
    name: 'PrivacyGuard Suite',
    status: 'Active',
    category: 'Compliance'
  },
  {
    id: 'PROD-BFBA88',
    name: 'nTrust.ai Dashboard',
    status: 'Coming Soon',
    category: 'Analytics'
  },
  {
    id: 'PROD-DE7694',
    name: 'TrustGuard',
    status: 'Active',
    category: 'Security'
  }
];

const ProductCatalogSync = () => {
  const [syncedProducts, setSyncedProducts] = useState([]);

  useEffect(() => {
    // Simulate fetch from internal registry
    setSyncedProducts(PRODUCT_CATALOG);
  }, []);

  return (
    <div className="product-catalog-container">
      <h2 className="text-2xl font-bold mb-4 text-gray-900">Our Products</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {syncedProducts.map((product) => (
          <div key={product.id} className="card p-6 border rounded-lg shadow-sm bg-white">
            <div className="flex justify-between items-center mb-2">
              <h3 className="text-xl font-semibold text-primary">{product.name}</h3>
              <span className={`badge ${product.status === 'Active' ? 'bg-green-100 text-green-800' : 'bg-blue-100 text-blue-800'}`}>
                {product.status}
              </span>
            </div>
            <p className="text-gray-600 mb-4">{product.category}</p>
            <button className="btn-primary w-full">
              {product.status === 'Active' ? 'Learn More' : 'Join Waitlist'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProductCatalogSync;