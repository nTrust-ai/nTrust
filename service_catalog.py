#!/usr/bin/env python3
"""nTrust.ai Service Catalog Server - Port 9090 Restoration"""
from flask import Flask, jsonify
import time

app = Flask(__name__)
start_time = time.time()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'uptime': time.time() - start_time}), 200

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def catalog():
    return jsonify({
        'service': 'nTrust.ai Service Catalog',
        'version': '2.0',
        'products': [
            {'id': 'PROD-DCCCF5', 'name': 'nTrust Shield', 'status': 'active'},
            {'id': 'PROD-SUN001', 'name': 'SUN-Token NFC Security', 'status': 'active'}
        ],
        'message': 'Sanitized public-facing catalog - Phase 3 Revenue Operations Active'
    }), 200

@app.route('/api/products', methods=['GET'])
def list_products():
    return jsonify({'products': [
        {'id': 'PROD-DCCCF5', 'name': 'nTrust Shield'},
        {'id': 'PROD-SUN001', 'name': 'SUN-Token NFC Security'}
    ]}), 200

if __name__ == '__main__':
    # HOST MUST BE 0.0.0.0 for external access
    app.run(host='0.0.0.0', port=9090, debug=False)