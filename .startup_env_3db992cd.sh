#!/bin/sh
echo "<h1>nTrust Pilot Env v1.0</h1><p>90-Day Free Pilot Environment Active & Validated.</p>" > /tmp/index.html && python3 -m http.server 8000 --directory /tmp