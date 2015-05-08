import networkx as nx
import re
from networkx.readwrite import json_graph


def getJson(g):
 t=json_graph.node_link_data(g) 
 x = str(t)
 x=re.sub("\'","\"",x)
 x=re.sub("links","edges",x)
 x=re.sub("\"directed\"(.)*True,","",x)
 x=re.sub("\"graph\"(.)*\[\],","",x)
 x=re.sub("\], \"multigraph\"(.)*False","",x)

 nodes_array = g.nodes()

 for i in range(len(nodes_array)):
  x=x.replace("\"source\": "+str(i),"\"source\": \""+nodes_array[i] + "\"")
  x=x.replace("\"target\": "+str(i),"\"target\": \""+nodes_array[i] + "\"")
 x=x.replace("}}","}]}")
 return x
