from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

html_form = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Safe Demo</title>
<style>
body { 
    background: #121212; 
    color: white; 
    font-family: Arial;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}
.box {
    padding: 25px;
    background: #1e1e1e;
    border-radius: 15px;
    width: 300px;
}
input, button {
    width: 100%;
    padding: 12px;
    margin-top: 10px;
    border-radius: 10px;
}
button {
    background: transparent;
    border: 2px solid cyan;
    color: cyan;
}
button:active {
    transform: scale(0.92);
}
</style>
</head>
<body>
<div class="box">
<h2>Safe Demo Form</h2>
<form method="POST">
<input type="password" name="pass" placeholder="Enter something" required>
<button type="submit">Submit</button>
</form>
</div>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_form.encode())

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length).decode()
        parsed = urllib.parse.parse_qs(data)
        user_input = parsed.get("pass", [""])[0]

        response = f"""
        <html>
        <body style='background:#000;color:white;font-family:Arial;padding:40px;'>
        <h1>You typed:</h1>
        <p style='color:cyan;font-size:22px;'>{user_input}</p>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(response.encode())


PORT = 9000
server = HTTPServer(("0.0.0.0", PORT), Handler)

print(f"SERVER RUNNING → http://localhost:{8000}")
print(f"OR → http://127.0.0.1:{8000}")

server.serve_forever()
