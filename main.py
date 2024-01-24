from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            with open('index.html', 'r') as file:
                content = file.read()
                self.wfile.write(content.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/update':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            with open('index.html', 'w') as file:
                file.write(post_data.decode('utf-8'))
                
            self.send_response(200)
            self.end_headers()
            print(f'Server updated!')
        else:
            self.send_response(404)
            self.end_headers()

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyServer)
    print(f'Server started at port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
