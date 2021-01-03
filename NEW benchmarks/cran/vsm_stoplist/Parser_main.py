import re
from glob import glob
import operator
import os
from os.path import exists
import traceback

CURRENT_DIRECTORY = os.getcwd()
INPUT_FOLDER = path = os.path.join(CURRENT_DIRECTORY,'cacm')
OUTPUT_FOLDER_PATH = path = os.path.join(CURRENT_DIRECTORY,'generated_corpus')



def write_files():
    try:
        LINK_FILENAME=[]
        counter=1
        #
        with open(CURRENT_DIRECTORY+'/cran.all.1400') as f:
            lines = ""
            for l in f.readlines():
                lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
            lines = lines.lstrip("\n").split("\n")
        doc_id = ""
        summary = ""
       
        for l in lines:
            if l.startswith(".I"):
                doc_id = l.split(" ")[1].strip()
            if(l.startswith('.W')):
                summary = l.strip()[3:] + " " 
            
            out_file  = open(OUTPUT_FOLDER_PATH+"/"+doc_id+".txt",'w')
#            tokens=" ".join(file_to_terms[term_file]) #Coverting a list to string with spaces as delimiters
            out_file.write(summary)
            out_file.close()
    except Exception as e:
        print(traceback.format_exc())



def processing_query():
    try:
        if exists(CURRENT_DIRECTORY+"/query.txt"):
            os.remove(CURRENT_DIRECTORY+"/query.txt")
        unprocessed_query = open(CURRENT_DIRECTORY+"/cran.qry",'r').read()
        query_file = open(CURRENT_DIRECTORY+"/query.txt",'a')
        
        with open(CURRENT_DIRECTORY+'/cran.qry') as f:
            lines = ""
            for l in f.readlines():
                lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
            lines = lines.lstrip("\n").split("\n")
        doc_id = ""
        summary = ""
        
        for l in lines:
            if l.startswith(".I"):
                doc_id = l.split(" ")[1].strip()
            if(l.startswith('.W')):
                summary = l.strip()[3:] + " " 
                summary = re.sub(r'[^\w\s]', '', summary) 
                query_file.write(summary.lower() + "\n")
        
        '''while unprocessed_query.find('<DOC>')!=-1:
            unprocessed_query, query = processed_query(unprocessed_query)
            if(unprocessed_query.find('<DOC>')==-1):
                query_file.write(query.lower())
            else:
                query_file.write(query.lower()+"\n")'''
    except Exception as e:
        print(traceback.format_exc())

processing_query()

write_files()
