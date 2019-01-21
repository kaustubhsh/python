#!/usr/bin/env python2

import  socket
import  os

rec_ip="127.0.0.1"
rec_port=9090 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((rec_ip,rec_port))            # proving  a way to connect 

while  3  >  2	 :
	data=s.recvfrom(100) 
	#  checking  for command 
	check=os.system(data[0]) 

	if  check ==  0 :
		print  "success"
		s.sendto("sahi command",data[1])
	else :
		s.sendto(data[0]+" not found",data[1])



		
	
