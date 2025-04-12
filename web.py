## PROGRAM:
from http.server import HTTPServer,BaseHTTPRequestHandler
content="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>30th table</title>
</head>
<body>
    <h2>Table of 10</h2>
    <p>10 x 1 = 10</p>
    <p>10 x 2 = 20</p>
    <p>10 x 3 = 30</p>
    <p>10 x 4 = 40</p>
    <p>10 x 5 = 50</p>
    <p>10 x 6 = 60</p>
    <p>10 x 7 = 70</p>
    <p>10 x 8 = 80</p>
    <p>10 x 9 = 90</p>
    <p>10 x 10 = 10</p>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8000)
httpd=HTTPServer(server_address,myhandler)
print("My webserver is running...")
httpd.serve_forever()