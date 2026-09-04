#!/bin/sh
cd /app/data/orgs/org_ntrust/mvp && python3 -m http.server 8085 > /tmp/server1.log 2>&1 & python3 -m http.server 55127 > /tmp/server2.log 2>&1 & echo "Atlas-ComputeWorker started"