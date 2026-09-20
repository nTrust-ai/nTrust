from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import threading

os.chdir('/app/data/prod/www')

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='/app/data/prod/www', **kwargs)

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8085), Handler)
    print("✅ React MVP served on 0.0.0.0:8085")
    server.serve_forever()
