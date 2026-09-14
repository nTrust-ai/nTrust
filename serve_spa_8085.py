#!/usr/bin/env python3
"""SPA static server for nTrust.ai React MVP (port 8085, TASK-B78E52). Binds 0.0.0.0."""
import http.server, functools, os, sys
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8085
DIR = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
class SpaHandler(http.server.SimpleHTTPRequestHandler):
    # directory supplied via functools.partial only (duplicate kwarg => TypeError, blank-render RCA)
    def send_head(self):
        if os.path.isfile(self.translate_path(self.path)):
            return super().send_head()
        self.path = "/index.html"
        return super().send_head()
    def log_message(self, fmt, *args):
        sys.stderr.write("[ntrust-spa:8085] %s - %s\n" % (self.address_string(), fmt % args))
if __name__ == "__main__":
    http.server.ThreadingHTTPServer(("0.0.0.0", PORT), functools.partial(SpaHandler, directory=DIR)).serve_forever()
