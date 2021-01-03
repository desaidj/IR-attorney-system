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
from whoosh import scoring
from nltk.corpus import stopwords
from whoosh.analysis import StemmingAnalyzer
from whoosh import fields

#
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
   errors = []
   results = []
   stop_words = frozenset(['and', 'is', 'it', 'an', 'as', 'at', 'have', 'in', 'yet', 'if', 'from', 'for', 'when', 'by', 'to', 'you', 'be', 'we', 'that', 'may', 'not', 'with', 'tbd', 'a', 'on', 'your', 'this', 'of', 'us', 'will', 'can', 'the', 'or', 'are'])
   query_to_search = request.form.get("search_query")
   
   query_to_search = list(str(query_to_search).split(" "))
   query_bag = []
   #stop_words = frozenset(stopwords.words('english'))
   for word in query_to_search:
      if word not in stop_words:
         query_bag.append(word)
   query_to_search = ' '.join(query_bag)
   
   
   if request.method == "POST":
           
      
      if not os.path.exists("/home/dlinux/Desktop/D/searchengine/indexdir"):
         os.mkdir("/home/dlinux/Desktop/D/searchengine/indexdir")
      
      stem_ana = StemmingAnalyzer(stoplist=stop_words)
      schema = Schema(title=TEXT(stored=True), content=TEXT(analyzer=stem_ana, stored = True)) #stoplist = none
      ix = index.create_in("/home/dlinux/Desktop/D/searchengine/indexdir", schema)
      
      writer = ix.writer()
      with open('/home/dlinux/Desktop/D/searchengine/cran.all.1400') as f:
         lines = ""
         for l in f.readlines():
            lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
         lines = lines.lstrip("\n").split("\n")
         # print n lines
      doc_id = ""
      summary = ""

      doc_set = {}
      doc_id = ""
      doc_text = ""
      for l in lines:
         if l.startswith(".I"):
            doc_id = l.split(" ")[1].strip()
         elif l.startswith(".B"):
            doc_set[doc_id] = doc_text.lstrip(" ")
            doc_id = ""
            doc_text = ""
         else:
            doc_text += l.strip()[3:] + " " 
      """
      for l in lines:
         if l.startswith(".I"):
            doc_id = l.split(" ")[1].strip()
         if(l.startswith('.W')):
            summary = l.strip()[3:] + " " 
         writer.add_document(title = doc_id , content = summary )"""

      for key, value in doc_set.items():
         writer.add_document(title = key , content = value )
      
      '''files = getFiles()
      for file in files:
            with open(file , "r") as f:
               filecontent = f.read()
               writer.add_document(title = file , content = filecontent )'''
      writer.commit()
      
      with ix.searcher(weighting=scoring.TF_IDF()) as searcher: #BM25F(B=0.75, K1=1.2)
         org = qparser.OrGroup.factory(0.5)
         query = QueryParser("content", ix.schema, group=org).parse(query_to_search) #termclass=FuzzyTerm ,
         resultstemp = searcher.search(query, terms=True)#, limit=24)
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
   os.chdir(r'/home/dlinux/Desktop/D/searchengine/datafile')
   myfiles = glob.glob('*.txt')
    
   return myfiles
