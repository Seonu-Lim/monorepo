import http.server
import socketserver
import os

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve files from the 'client' directory
        if self.path == '/':
            self.path = '/client/index.html'
        elif self.path.startswith('/client/'):
            # The path is already correct, do nothing
            pass
        else:
            # Prepend '/client' to all other paths
            self.path = f'/client{self.path}'
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Change to the directory containing your 'client' folder
os.chdir('..')  # Assuming this script is in a subdirectory

# Set up the server
PORT = 3000
Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Open http://localhost:{PORT} in your browser")
    httpd.serve_forever()