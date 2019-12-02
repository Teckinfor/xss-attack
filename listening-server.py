import http.server
import socketserver

PORT = 12_000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print(httpd.get_request())
    httpd.handle_request()
