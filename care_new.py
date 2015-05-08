import nltk
import time
import math
import os
import re
import sys

def qweet_extraction(tweet):
 if re.search("http:",tweet) or re.search("RT",tweet):
   return True
 else :
   return False
  
 

def question_extraction():
 fl = open(sys.argv[1],"r")
 x=[]
 w51h = ["why","when","where","what","how","What","When","Where","Why","How"]
 tweet = ''
 counter = 0
 try :
  for line in fl:
    x=line.split(",")
    tweet = x[-3].split(" ")
    for word in w51h:
      if word in tweet and re.search("\?+",x[-3])  :
          if qweet_extraction(x[-3]):
           print x[-3] 
           counter =  counter + 1
 except Exception,e:
  print str(e)
 print counter
 


question_extraction()

