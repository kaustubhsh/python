#!/usr/bin/env python2

import  socket

rec_ip="127.0.0.1"
rec_port=9090   #  port >6000  are generally free to use 

#  calling  UDP  protocol 
#             socket.AF_INET--->ipv4         , socket.SOCK_DGRAM--->  UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  sending  messag to target 

while  True:
	data=raw_input("type your message :  ")
        #  it will send data to receiver as well as create own socket (own ip and any random port)
	s.sendto(data,(rec_ip,rec_port))
	#  this is for receiving from  sender 
	print  s.recvfrom(10)



