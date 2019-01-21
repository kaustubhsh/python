#!/usr/bin python3
import socket
ip="192.168.10.101"
port=9090	# port--> 6000 are generally free to use
# socket contain calling protocol for udp (socket --> function name)

#calling UDP protocol
#socket.AF_INET -->	ipv4, socket.SOCK_DGRAM --> UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# ======================= above this all is common for both sender/receiver 

#receiver side code
#binding ip and port
while 1:
	s.bind((ip,port))  # provding a way to connect
	s.recvfrom(100) # here 100 is a buffer size in character
