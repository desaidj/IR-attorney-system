from glob import glob
import operator
import os
from os.path import exists
import traceback
from math import sqrt
from math import log


CURRENT_DIRECTORY = os.getcwd()
INPUT_FOLDER = path = os.path.join(CURRENT_DIRECTORY,'generated_corpus')
OUTPUT_FOLDER_PATH = path = os.path.join(CURRENT_DIRECTORY,'doc_score')
DOC_NAME ={} # mapping doc name and ids

def main():
    try:
        if exists(CURRENT_DIRECTORY+"/newREl.txt"):
            os.remove(CURRENT_DIRECTORY+"/newREl.txt")
        unprocessed_query = open(CURRENT_DIRECTORY+"/cranqrel",'r').read()
        query_file = open(CURRENT_DIRECTORY+"/newREl.txt",'a')
        
        with open(CURRENT_DIRECTORY+'/cranqrel') as f:
            lines = ""
            for l in f.readlines():
                summary = l.split()[0].strip() + ' Q0 ' + l.split()[1].strip() + ' ' + '1' #l.split()[2].strip() #' 1 ' #Q0 CACM-
                query_file.write(summary + "\n")
        
                '''lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
            lines = lines.lstrip("\n").split("\n")
        doc_id = ""
        summary = ""
        
        for l in lines:
            print(l)
            summary = l.split()[0].strip() + ' Q0 CACM-' + l.strip()[2:7]
            query_file.write(summary + "\n")'''
        
        
    except Exception as e:
        print(traceback.format_exc())

main()





#x = '1 184 2'
#x = '2 Q0 CACM-1410 1'

#print(x.split()[0])

#print(x[:-1])










