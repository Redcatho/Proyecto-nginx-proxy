import http.server
import socketserver

PORT = 5000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status": "success", "message": "Hola desde la API de Backend de Diego"}')

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Servidor API corriendo en el puerto {PORT}")
    httpd.serve_forever()
