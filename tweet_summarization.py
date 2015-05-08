import os
import nltk
import time
import math
import networkx as nx
import re
import pylab
import sys
from nltk.corpus import stopwords as sw

g=nx.Graph()
word_count = {}
all_words = []
stpwords = sw.words('english') + ['?','\n','!','rt']

def retWordList(tweet):
 global all_words
 global stpwords
 word_list = []
 
 tweet_words = tweet.split(" ")
 for word in tweet_words:
   if (re.search("http",word) or word in stpwords) or word.startswith("@"):
    word_list=word_list+[]
   else:
    word_list = word_list + [word.lower()]
 all_words = all_words + word_list
 return word_list
 
 
def buildGraph(word_list):
 global g
 a=""
 b=""
 for i in range(len(word_list)):
  if i!=len(word_list)-1:
   try : 
    a=word_list[i+1].encode("ascii","ignore")
    b=word_list[i].encode("ascii","ignore")
   except Exception,e:
     print str(e)
   
   g.add_edge(a,b)
   #word_count[word_list[i]] = word_count[word_list[i]]+1



def test(rt):
 
 global g
 weight = nx.get_node_attributes(g,"weight")
 #print "from test :" , weight
 print rt
 weights=weight.values()
 node_words=weight.keys()
 
 parent_node = rt
 question_string = rt 
 neighbours_weights=dict()
 prev=""
 for i in range(20):
  neighbours_weights={}
  x=nx.neighbors(g,parent_node)
  print x
  print prev
  try :
   if i!=0:
     x.remove(prev)
   for node in x:
    neighbours_weights[node] = weight[node]
   prev=parent_node
   parent_node = max(neighbours_weights)
   print "Parent node is : ", parent_node
   question_string = question_string + " " + parent_node
   
  except Exception,e:
    print str(e)
  
 print question_string  
 try :
  nx.write_gexf(g,"Customer_questions",prettyprint=True)
 except Exception,e:
   print str(e)
 
 

def initializeNodeWeights(fdist,rt):
 global g
 weight = {}
 for key in g.nodes():
   try :
    weight[key] = fdist[key]-(nx.shortest_path_length(g,source=rt,target=key)*math.log(fdist[key]))
   except Exception,e:
    print ""
 #print weight
 nx.set_node_attributes(g,"weight",weight)
 test(rt)
 




def giveTweets():
 global g
 i=0
 fl = open("questions_file.txt","r")
 fdist=object()
 for line in fl :
   i=i+1
   buildGraph(retWordList(line)) 
 fdist = nltk.FreqDist(all_words)
 initializeNodeWeights(fdist,sys.argv[2])
    
 #nx.draw(g) 
 #pylab.show()
 
 


os.system("python care_new.py " + sys.argv[1] + " > questions_file.txt")
giveTweets()     
