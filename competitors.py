import nltk
import time
import math
import os
import re
import networkx as nx
import pylab
import sys
import related_events
import json
from networkx.readwrite import json_graph

def getCompetitors(filename,central_theme,dataset_name):
 fl = open(filename,"r")
 g=nx.DiGraph()
 x=[]
 POS = []
 tweet_words = []
 i=0
 competitors = []
 entities = []
 overall_entities =  []
 for line in fl:
  entities = []
  x=line.split("\t")
  tweet_words = x[0].split(" ")
  POS=x[1].split(" ")
  k=0
  for items in POS:
    i = POS.index(items)
    if items == '^' and POS[i+1]== '^':
      entities =  entities + [tweet_words[i]+" - " +tweet_words[i+1]]
      k=k+1
    if items == '^' and POS[i-1]=='^':
      print 'joined'
    if items == '^' and (POS[i-1]!='^' and POS[i+1]!='^'):
      entities = entities + [tweet_words[i]]
  print entities
  overall_entities = overall_entities + entities
 fdist = nltk.FreqDist(overall_entities)
 for i in range(len(fdist.keys())):
  print fdist.keys()[i] + " : " + str(fdist.values()[i])


 #comeptitor finding
 for entities in overall_entities :
  if entities.find("-") != -1 :
    competitors = competitors + [entities[0:entities.find("-")]]
  else :
    competitors = competitors + [entities]
 competitors = list(set(competitors))
  
 
 #graph making 
 g.add_node(central_theme)  
 for node in fdist.keys()[:40]:
   g.add_node(node,size=fdist[node])
   g.add_edge(central_theme,node) 
 t=json_graph.tree_data(g,root=central_theme)
 s = json.dumps(t, sort_keys=True, indent=4)
 r='\n'.join([l.rstrip() for l in  s.splitlines()])
 

 l=open("marketer.json","w")
 l.write(r)
 l.close()

 l=open("marketer.json","r")
 l1=open("marketer_rival.json","w")
 p=''
 for line in l:
  p=line.replace("id","name")
  l1.write(p)
 l.close()
 l1.close()

 os.system("cat marketer_rival.json")
 os.remove("marketer.json") 

 
 nx.draw(g)
 pylab.show()

 nx.write_gexf(g,"test.gexf",prettyprint=True)
 #print competitors
 #related_events.list_tweets(competitors,sys.argv[1])
 


def makeParseFile(filename):
 required_name =  filename.replace(".txt","")
 os.system("./runTagger.sh " + filename + " > " + required_name + "_parsed.csv") 
 os.system("rm " + filename)
 return required_name + "_parsed.csv"

def check(dataset_name,central_theme):
 
 fl=  open(dataset_name,"r")
 required_name = dataset_name.replace(".csv","") + "_marketer_tweets.txt"
 f=open(required_name,"w")
 x=[]
 tweet =  ''
 counter = 0
 ind=0
 try : 
  for line in fl :
    x=line.split(",")
    tweet = x[-3]
    if re.search(" vs ",tweet):
     ind = tweet.find(" vs ") 
     f.write(tweet+"\n")
     print tweet[ind-35:ind+35]
     counter = counter + 1
    elif re.search("versus", tweet):
     ind = tweet.find("versus") 
     f.write(tweet+"\n")
     print tweet[ind-35:ind+35]
     #print tweet
     counter = counter + 1
 except Exception,e:
  print str(e) 
 print counter
 f.close()
 parsed_file = makeParseFile(required_name)
 getCompetitors(parsed_file,central_theme,sys.argv[1])
 


check(sys.argv[1],"moto")

   
