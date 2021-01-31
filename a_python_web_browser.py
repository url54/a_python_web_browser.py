# This program was used for an assignemnt, in which we had to test a web socket connection
# using python as our web-browser.  Below this are the instructions for the assignment.  More
# importantly we had to pull out specific information that would show that we actually got the
# HTTP header response.

# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
# http://data.pr4e.org/intro-short.txt .
# Enter the header values in each of the fields below and press "Submit".
# Last-Modified:
# ETag:
# Content-Length:
# Cache-Control:
# Content-Type:


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
