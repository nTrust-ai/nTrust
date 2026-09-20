#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os

os.chdir('/app/data/frontend/dist')
class H(SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    
ThreadingHTTPServer(('0.0.0.0', 8085), H).serve_forever()
