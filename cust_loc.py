import os
import nltk
import time
import math
import networkx as nx
import pylab
import re
from networkx.readwrite import json_graph

def getLocation(dataset_name):
 fl = open(dataset_name,"r")
 g=nx.DiGraph()
 g.add_node("areas")
 x=[]
 location_name = ''
 locations = []
 f=open("aux.txt","w")
 try :
  for line in fl:
   x=line.split(",")
   location_name = x[8] 
   if len(location_name) > 0 :
    locations=locations + [location_name.strip("\"")]
  
 except Exception,e :
   print str(e)
 fdist = nltk.FreqDist(locations) 
 j=len(fdist.keys()) - 1
 i=0
 location_name = ''
 color = ''
 for areas in fdist.keys():
  i=i+1
  if fdist[areas] > 50 and fdist[areas] < 100:
    color = 'blue' 
  if fdist[areas] > 100 and fdist[areas] < 200:
    color = 'yellow' 
  if fdist[areas] > 200 and fdist[areas] < 1000:
    color = 'green' 
  if fdist[areas] > 1000 :
    color = 'red'
  if i!=j:
   location_name = location_name +  "{\n" + "id:"+"\""+areas+"\",\n" + "color:" + "\""+color+"\"\n},\n" 
 
 location_name = location_name[:-2]
 f.write(location_name)
 f.close()
 print fdist.keys()
 print fdist.values()


getLocation("moto_overall.csv")
 
