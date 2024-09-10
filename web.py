from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
import time

class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

        print("\nRequest Information:")
        print(f"Host: {self.headers['Host']}")
        print(f"User-Agent: {self.headers['User-Agent']}")
        print(f"Path: {self.path}")

    def get_response(self):
        response_html = f"""
        <h1> Hola Web </h1>
        <p> URL Parse Result : {self.url()}         </p>
        <p> Path Original: {self.path}         </p>
        <p> Headers: {self.headers}      </p>
        <p> Query: {self.query_data()}   </p>
        """
        
        print("\nResponse Information:")
        print(f"Content-Type: text/html")
        print(f"Server: {self.version_string()}")
        print(f"Date: {self.date_time_string()}")

        return response_html

if __name__ == "__main__":
    PORT = 8000
    print(f"Starting server on port {PORT}")
    server = HTTPServer(("localhost", PORT), WebRequestHandler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
