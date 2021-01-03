import requests
import nltk
import os
import tempfile
import numpy as np
import pandas as pd
import re
import sumy
import sys
import networkx as nx
from flask import Flask, render_template, request
from io import StringIO

from whoosh.fields import Schema, TEXT, ID
from whoosh import index
from whoosh import qparser
from whoosh.qparser import QueryParser
from whoosh.query import FuzzyTerm
import  glob
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
      
      schema = Schema(title=TEXT(stored=True), content=TEXT(stored = True))
      ix = index.create_in("/home/dell/searchengine/indexdir", schema)
      
      writer = ix.writer(limitmb = 1000)
      '''if len(sys.argv) != 2:
         print("Usage: python3 inverted_index.py <file name>")
         sys.exit(1)'''
      files = ("/home/dell/searchengine/movies.txt")
      record_id = '0'
      with open(files) as filess:
         for line in filess:
            filecontent = line
            record_id += '1'
            writer.add_document(title = record_id , content = filecontent )
      writer.commit()
      
      with ix.searcher() as searcher:
         org = qparser.OrGroup.factory(0.5)
         query = QueryParser("content", ix.schema, termclass=FuzzyTerm, group=org).parse(query_to_search)
         resultstemp = searcher.search(query, terms=True)
         #print(results[0:])
         results = {}
         for hit in resultstemp:
            results[hit["title"]] = hit["content"]
        
   return render_template('index.html', errors=errors, results=results)


