import requests
import nltk
import os
import tempfile
import numpy as np
import pandas as pd
import re
import sumy
import networkx as nx
from flask import Flask, render_template, request
from io import StringIO
import  glob

from whoosh import index
from whoosh.query import FuzzyTerm
from whoosh import qparser
from whoosh.qparser import *
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED, NUMERIC
from whoosh.analysis import StemmingAnalyzer, StandardAnalyzer
from whoosh import index
from nltk.corpus import stopwords
#
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
   errors = []
   results = []
   query_to_search = request.form.get("search_query")
   
   
   if request.method == "POST":
           
      
      if not os.path.exists("/home/dell/searchengine/indexdir"):
         os.mkdir("/home/dell/searchengine/indexdir")
      
      schema = Schema(title=TEXT(stored=True), content=TEXT(analyzer=StandardAnalyzer(stoplist=None), stored = True)) #stoplist = none
      ix = index.create_in("/home/dell/searchengine/indexdir", schema)
      
      writer = ix.writer()
      with open('/home/dell/searchengine/cran.all.1400') as f:
         lines = ""
         for l in f.readlines():
            lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
         lines = lines.lstrip("\n").split("\n")
   # print n lines
   n = 5
   for l in lines[:n]:
      print(l)
      """doc_id = ""
      summary = ""
      
      for l in lines:
         if l.startswith(".I"):
            doc_id = l.split(" ")[1].strip()
         if(l.startswith('.W')):
            summary = l.strip()[3:] + " " 
         writer.add_document(title = doc_id , content = summary )"""
      '''files = getFiles()
      for file in files:
            with open(file , "r") as f:
               filecontent = f.read()
               writer.add_document(title = file , content = filecontent )'''
      writer.commit()
      
      with ix.searcher() as searcher:
         org = qparser.OrGroup.factory(0.5)
         query = QueryParser("content", ix.schema, group=org).parse(query_to_search)
         resultstemp = searcher.search(query, terms=True, limit=45)
         #print(results[0:])
         results = {}
         for hit in resultstemp:
            results[hit["title"]] = hit["content"]

      if resultstemp.has_matched_terms():
         # What terms matched in the results?
         print(resultstemp.matched_terms())

      # What terms matched in each hit?
      for hit in resultstemp:
         print(hit.matched_terms())

   return render_template('index.html', errors=errors, results=results)

def getFiles():
   os.chdir(r'/home/dell/searchengine/datafile')
   myfiles = glob.glob('*.txt')
    
   return myfiles
