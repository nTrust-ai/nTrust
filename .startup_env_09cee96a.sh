#!/bin/sh
sh -c 'apt-get update -qq && apt-get install -y -qq --no-install-recommends curl git ca-certificates >/dev/null 2>&1; exec sleep infinity'