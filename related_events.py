import os
import nltk
import time
import math

def list_tweets(lst,dataset_name):
 x=''
 apostrophe_list = []
 for items in lst :
    x=items.replace("#","")
    x=items.replace(" ","")
    x=x+'\'s'
    apostrophe_list = apostrophe_list + [x] 
 print apostrophe_list

 fl = open(dataset_name,"r")
 y=[]
 for line in fl :
  y=line.split(",")
  print y[-3] 
