#!/usr/bin/env python3
import os, http.server, socketserver

os.chdir('/app/data/orgs/org_ntrust/frontend/revenue-dashboard/dist/')
PORT = 55128

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,directory="/app/data/orgs/org_ntrust/frontend/revenue-dashboard/dist/",**kwargs)

socketserver.TCPServer(("", PORT), Handler).serve_forever()