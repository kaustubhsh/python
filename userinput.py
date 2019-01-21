#!/usr/bin/env  python2

#  import  is a keyword to import any python library 
import   time
import  math        #  theano  --supercomputing --DL
import  os    #  to understand and user  Base Operating system  features / commands 

#  all data will be converted into string  
x=raw_input("plz enter  a number :   ")


print  "processing..................()()()()()"

voice='echo  processing   |    festival  --tts'
#   here system is a function under os library  to run any command 
os.system(voice)

time.sleep(3)   #  here 5  is second 	
print  type(x)
sum=int(x)  +  100
#  voice output is being generated 
voice_output='echo  '+str(sum)  +  '   |   festival  --tts'

print  sum
os.system("echo  your output is  "+str(sum)+ ' | festival --tts')

