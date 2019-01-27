#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re
import nltk

data=search('hello',num=5,lang="eng",tld="co.in",stop=5)
print (type(data))
main_text=""
for i in data:
    source = requests.get(i).text
    soup = BeautifulSoup(source, 'lxml')
    for p in soup.select('p'):
        main_text=main_text+p.text
#print(main_text)
x=re.sub("Loading...|Working...","",main_text)
y=re.sub("\s{2,40}"," ",x)
z=re.sub("[+, *, ., |, (), $,{},~,!,#,%,^,&,-,_,=,:,;,<,>,?,/,',\"]"," ",y)
f=open('/home/kaustubh/scraped.txt','w')
f.write(z)
f.close()

f = open("/home/kaustubh/scraped.txt", "r")
inputfile = f.read()
tokens = nltk.tokenize.word_tokenize(inputfile)
fd = nltk.FreqDist(tokens)
fd.plot(30,cumulative=False)
f.close()