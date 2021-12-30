import urllib3
import socket

http = urllib3.PoolManager()
request = http.request('GET', 'https://en.wikipedia.org/wiki/Potentiometer')
print(socket.getaddrinfo('https://en.wikipedia.org/wiki/Potentiometer'))