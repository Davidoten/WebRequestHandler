from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

contenido = {
    '/': """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ana Lee</title>
</head>
<body>
    <h1>Ana Lee</h1>
    <h2>Desarrolladora Web (Música/Diseño/Empresaria)</h2>
    <small>Este texto fue generado por Copilot:</small>
    <h3>¡Hola! Soy Ana Lee, una desarrolladora web que se especializa en la creación de sitios web y aplicaciones web. Me encanta trabajar con tecnologías web modernas y crear experiencias de usuario atractivas y fáciles de usar. También soy una artista y empresaria apasionada, y me encanta combinar mi creatividad y mi pasión por la tecnología para crear soluciones web únicas y efectivas.</h3>
    <h2>Proyectos</h2>
    <h3><a href="/proyecto/1">Web Estática - App de recomendación de libros</a></h3>
    <h3><a href="/proyecto/2">Web App - MeFalta, que película o serie me falta ver</a></h3>
    <h3><a href="/proyecto/3">Web App - Foto22, web para gestión de fotos</a></h3>
    <h2>Experiencia</h2>
    <h3>Desarrolladora Web Freelance</h3>
    <h3>Backend: FastAPI, nodejs, Go</h3>
    <h3>Frontend: JavaScript, htmx, React</h3>
</body>
</html>""",
    '/proyecto/1': """<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Proyecto Web Estática</title>
</head>
<body>
    <h1>Juan</h1>
    <h2>Recomendación de libros</h2>
    <p>El proyecto consiste en el diseño de un sitio que muestra la información de distintos libros. La información se obtiene de una base de datos que se actualiza cada vez que se agrega un nuevo libro. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla aliquam faucibus sapien, nec eleifend libero pulvinar a. Donec suscipit tortor quis velit placerat, et finibus nibh fermentum...</p>
    <h2>Tecnologías</h2>
    <ul>
      <li>HTML5</li>
      <li>CSS</li>
      <li>Redis</li>
    </ul>
</body>
</html>""",
    '/proyecto/2': """<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Proyecto Web App - MeFalta</title>
</head>
<body>
    <h1>Juan</h1>
    <h2>No Falta - ¿Qué película o serie me falta ver?</h2>
    <p>El proyecto MeFalta permite a los usuarios llevar un registro de las películas y series que han visto y las que les falta por ver. La aplicación proporciona recomendaciones personalizadas basadas en el historial de visualización...</p>
    <h2>Tecnologías</h2>
    <ul>
      <li>HTML5</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
</body>
</html>""",
    '/proyecto/3': """<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Proyecto Web App - Foto22</title>
</head>
<body>
    <h1>Juan</h1>
    <h2>Foto22 - Web para gestión de fotos</h2>
    <p>Foto22 es una plataforma en línea para la gestión y organización de fotos. Permite a los usuarios subir, categorizar y compartir sus fotos con facilidad. La aplicación incluye características como la búsqueda de fotos y la creación de álbumes...</p>
    <h2>Tecnologías</h2>
    <ul>
      <li>HTML5</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
</body>
</html>"""
}

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in contenido:
            self.serve_content(self.path)
        else:
            self.serve_404_error()

    def serve_content(self, path):
        content = contenido[path]
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

    def serve_404_error(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        error_message = "<h1>Error 404: Página no encontrada</h1>"
        self.wfile.write(error_message.encode("utf-8"))

if __name__ == "__main__":
    PORT = 8000
    print(f"Starting server on port {PORT}")
    server = HTTPServer(("0.0.0.0", PORT), WebRequestHandler)
    print(f"Server running at http://0.0.0.0:{PORT}")
    server.serve_forever()
