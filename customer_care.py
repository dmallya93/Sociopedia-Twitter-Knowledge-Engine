import nltk
import time
import math
import os
import re

def qweet_extraction(tweet,features):
 if 'U' in features or re.search("RT",tweet):
   return True
 else :
   return False
  
 

def question_extraction():
 fl = open("Parsed.csv","r")
 x=[]
 w51h = ["why","when","where","what","how","What","When","Where","Why","How"]
 tweet = ''
 counter = 0
 try :
  for line in fl:
    x=line.split("\t")
    tweet = x[0].split(" ")
    for word in w51h:
      if word in tweet and re.search("\?+",x[0])  :
          if qweet_extraction(x[0],x[1]):
           print x[0] 
           counter =  counter + 1
 except Exception,e:
  print str(e)
 print counter
 


question_extraction()
   
