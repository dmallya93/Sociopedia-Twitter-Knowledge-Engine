import os
import nltk
import time
import math

def Parse():
 fl = open("moto_overall.csv","r")
 x=[]
 f=open("moto_overall_tweets.txt","w")
 try :
  for line in fl :
   x=line.split(",")
   f.write(x[-3]+"\n")
  f.close()
 except Exception,e :
  print str(e)
  


def cluster():
 fl = open("Parsed.csv","r")
 x=[]
 pos = []
 fdist = object()
 p=[]
 f1=open("marketer.txt","w")
 f2=open("customer_care.txt","w")
 f3=open("product_management.txt","w")
 for line in fl:
   x=line.split("\t")
   pos = x[1]
   fdist =  nltk.FreqDist(pos)
   p=fdist.keys()
   if p[1]=='^':
     f1.write(x[0]+"\n")
   elif p[1] == 'N':
     f2.write(x[0]+"\n")
   elif p[1] == 'V':
     f3.write(x[0]+"\n")
   else:
      print 'NO class'
    
     

 

#Parse()
#os.system("./runTagger.sh moto_overall_tweets.txt > Parsed.csv")
cluster() 
 
 
