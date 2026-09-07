#!/usr/bin/env python3
from flask import Flask, jsonify
import time

app = Flask(__name__)
start_time = time.time()


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "uptime": time.time() - start_time})


@app.route("/")
@app.route("/index")
def catalog():
    return jsonify(
        {
            "service": "nTrust.ai Service Catalog",
            "products": [
                {"id": "PROD-DCCCF5", "name": "nTrust Shield"},
                {"id": "PROD-SUN001", "name": "SUN-Token NFC Security"},
            ],
        }
    )


@app.route("/api/products")
def products():
    return jsonify(
        {
            "products": [
                {"id": "PROD-DCCCF5", "name": "nTrust Shield"},
                {"id": "PROD-SUN001", "name": "SUN-Token NFC Security"},
            ]
        }
    )


if __name__ == "__main__":
    # CRITICAL: 0.0.0.0 for external access - DO NOT use localhost
    app.run(host="0.0.0.0", port=9090, debug=False)
