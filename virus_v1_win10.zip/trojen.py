import os
import time
import http.server
import socket
import socketserver
import os

(os.system('ipconfig /displaydns > dns_logs.txt'))
os.system('ipconfig /flushdns')

PORT = 8010

os.chdir('C:\ESD')

Handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your Browser", IP)
    httpd.serve_forever()

time.sleep(100)