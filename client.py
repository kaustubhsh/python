#!/usr/bin/env python2

import  socket

rec_ip="127.0.0.1"
rec_port=9090   
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  sending  messag to target 

while  True:
	data=raw_input("type your command  :  ")
       
	s.sendto(data,(rec_ip,rec_port))
	print  s.recvfrom(100)
	
