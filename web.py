from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.generate_dynamic_html().encode("utf-8"))

    def generate_dynamic_html(self):
        
        path = self.url().path.strip('/')
        query_params = self.query_data()

        if path.startswith("proyecto"):
            try:
                _, project_name = path.split('/')
                author = query_params.get("autor", "desconocido")
                return f"<h1>Proyecto: {project_name} Autor: {author}</h1>"
            except ValueError:
                return "<h1>Error: Formato de URL incorrecto</h1>"
        else:
            return "<h1>Ruta no reconocida</h1>"


if __name__ == "__main__":
    PORT = 8000
    print(f"Starting server on port {PORT}")
    server = HTTPServer(("localhost", PORT), WebRequestHandler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
