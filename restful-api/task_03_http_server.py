#!/usr/bin/python3
"""
Simple API using Python's http.server module.
Handles GET requests and serves text or JSON data.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET (self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self_wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "Json",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text-plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

    def run():
        server = HTTPServer(("", 8000), SimpleAPIHandler)
        server.serve_forever()

    if __name__ == '__main__':
        run()
