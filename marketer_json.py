import os
import nltk
import networkx as nx
from networkx.readwrite import json_graph
import pylab
import re

def createTree():
 g=nx.DiGraph()
 g.add_node("Kaushik",size=2000)
 g.add_node("Apoorva",size=1000)
 g.add_node("Chaitanya",size=1000)
 g.add_node("Dilip",size=1000)
 
 g.add_edge("Kaushik","Apoorva") 
 g.add_edge("Kaushik","Dilip") 
 g.add_edge("Kaushik","Chaitanya") 

 t=json_graph.tree_data(g,root="Kaushik")
 x=str(t)
 x=re.sub(x,'id','name')
 print x
 

 nx.draw(g)
 pylab.show()

createTree()


