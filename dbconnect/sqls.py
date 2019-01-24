#!/usr/bin/python2
import cgi
import cgitb
import commands
import mysql.connector 

connection = mysql.connector.connect(host='localhost',database='adhoc',user='root',password='redhat')
cur = connection.cursor()
print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

name = data.getvalue("n1")
print(name)
print "<br/>"

surname = data.getvalue("n2")
print(surname)
print "<br/>"

age = data.getvalue("n3")
print(age)
print "<br/>"

email = data.getvalue("n4")
print(email)
print "<br/>"

cur.execute("INSERT INTO dockers(name,surname,age,email) VALUES(%s,%s,%s,%s)", (name,surname,age,email))
connection.commit()
#fetching  database
cur.execute("select *   from dockers")
print  cur.fetchall()
connection.close()








