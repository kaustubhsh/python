#!/usr/bin/env python2

import  commands,time

print  "plz wait we are really working hard to get RAM and CPU info"
#  delay for 2 seconds 
time.sleep(2)
ram=commands.getoutput('free -m')
final_memory=ram.split()[7]
print  "MY system RAM is "+final_memory+" MB"
cpu=commands.getoutput('lscpu   |    grep  -i model  |   tail -1')
print  "CPU status of this Machine is ",cpu

print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2"
print "@@                                           @@2"
print "@@                                           @@2"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2"
execfile('menu.py')

