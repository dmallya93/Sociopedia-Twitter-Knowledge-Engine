import os
import nltk
import time
import math
import matplotlib.pyplot as plt
import numpy


def trajectory(k) :
 circle = object()
 x=numpy.linspace(0,5,10)
 y=numpy.linspace(5,-5,10)
 col = ''
 for i in range(10):
   for j in range(10): 
    if j==i:
       col = 'r'
    else:
       col='w'    
    circle = plt.Circle((x[j],y[j]), radius=0.2, fc=col,ec='white')  
    rect = plt.Rectangle((4.5,-6), 4, 1+k, facecolor="red",ec='white') #x,y     
    plt.gca().add_patch(circle)
    plt.gca().add_patch(rect)
    plt.axis([-10,10,-10,10])
    plt.pause(0.001)
 

trajectory(1)
trajectory(2)
trajectory(3)
 
