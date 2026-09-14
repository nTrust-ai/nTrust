#!/bin/sh
apk add --no-cache bash gh jq curl npm > /dev/null 2>&1; chmod +x /workspace/spine_ci_patcher.sh; bash /workspace/spine_ci_patcher.sh