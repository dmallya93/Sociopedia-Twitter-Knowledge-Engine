import os
import nltk
import pylab
import csv
 
def donut_json_creator(filename):

 fl1=open("./file1.txt","r")
 fl2=open("./file2.txt","r") 
 str1 = fl1.read()
 str2= fl2.read()
 fl = open(filename,"r")
 fl1 = open(filename,"r")  
 x=len(fl1.readlines())
 y=[]
 p=""
 
 counter = 0 
 #print str1
 p=p+str1
 p=p+ "{\n"
 for line in fl:
  counter=counter+1
  y=line.split(",")
  
  p=p+ "\"keyword\": \""+y[0]+"\"," + "\n"
    
  p=p+"\"occurences\": " + y[1] + "\n}" 
  if counter != x:
   p=p+",{\n" 
     

 #print p
 p=p + "],\n" + str2
 fl=open("resultant_file.js","w")
 fl.write(p)
 fl.close()
 print p


donut_json_creator("entries.csv")


 
  
