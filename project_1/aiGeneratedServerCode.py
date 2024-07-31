from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b'<!DOCTYPE html><html><head><title>My Web Server</title></head><body><h1>My Web Server</h1><p>This server is running on port 8000</p></body></html>')

def start_web_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyServer)
    print('Starting web server...')
    httpd.serve_forever()

if __name__ == '__main__':
    start_web_server()
