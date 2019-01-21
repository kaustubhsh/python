#!/usr/bin/env  python2

import  webbrowser,time
import  commands
options='''
Press  1  to  check your OS version  :
Press  2  to  login your facebook account   :
Press  3  to check RAM and CPU in your currnet machine   :
Press  4  to search something in google search engine :   :
Press  5  to list out all IP and mac address in your current network zone  :
'''
print  options 
#  to take input from user in python 2
choice=raw_input()


if    int(choice)  ==  1  :
	print  "MY OS is RHEL "

elif  int(choice) ==  3: 
	execfile('cpu_ram_check.py')


elif  int(choice)  ==  4  : 
	data=raw_input("type something to search on google :  ")
	webbrowser.open_new_tab('https://www.google.com/search?q='+data)

else :
	print  "NO valid option given "
	print  "closing programmmm"
	exit()







