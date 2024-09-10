from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.serve_home_page()
        else:
            self.serve_404_error()

    def serve_home_page(self):
        try:
            with open('home.html', 'r') as file:
                content = file.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        except FileNotFoundError:
            self.serve_404_error()

    def serve_404_error(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        error_message = "<h1>Error 404: Página no encontrada</h1>"
        self.wfile.write(error_message.encode("utf-8"))

if __name__ == "__main__":
    PORT = 8000
    print(f"Starting server on port {PORT}")
    server = HTTPServer(("localhost", PORT), WebRequestHandler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
