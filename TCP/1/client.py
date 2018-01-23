#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
VAR = raw_input('Enter number: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(VAR)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data: ", data
