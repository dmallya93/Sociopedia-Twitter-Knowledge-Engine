from flask import Flask
from flask import request
from flask import Markup
from flask import render_template
#import searcher_module as sm
import os
import ontology as onto
#import process as pr


app = Flask(__name__)


@app.route('/')
def second_func():   
    #onto.documentsPath("moto_bulk") 
    return render_template('index.html') 


@app.route('/tester.html',methods=['GET','POST'])
#@app.route('/amcharts/amcharts.js',,methods=['GET','POST'])
def kau_world():
    l=''
    if request.method=='POST':
      l= request.form['search']
      print request.form['search']
      #pr.getInfo(request.form['name'],request.form['email']);
      onto.createGraphJsonMultiLevel(onto.parseResultsToEntities(onto.getObjects("moto_bulk",l))) 
      os.system("firefox secondindex.html")   
    return "Kaushik"


app.run(debug=True)
