from whoosh.fields import Schema, TEXT, ID
from whoosh import index
from whoosh import qparser
from whoosh.qparser import QueryParser
from whoosh.query import FuzzyTerm
import os, glob
import pandas as pd
#To create an index in a directory, use index.create_in: 




def main():    
    if not os.path.exists("/home/dell/searchengine/indexdir"):
        os.mkdir("/home/dell/searchengine/indexdir")

    """schema = Schema(title=TEXT(stored=True), content=TEXT(stored = True))
    ix = index.create_in("/home/dell/searchengine/indexdir", schema)"""

    """writer = ix.writer()"""
    files_path = ("/home/dell/searchengine/cran.all.1400")
    data = pd.read_csv(files_path)

    print(data.head())
    """ for file in files:
        with open(file , "r") as f:
            filecontent = f.read()
            writer.add_document(title = file , content = filecontent )
    
    with open(files) as filess:
        for line in filess:


    writer.commit()

    
    
    query_to_search =  u"high court"
    with ix.searcher() as searcher:
        org = qparser.OrGroup.factory(0.5)
        query = QueryParser("content", ix.schema, termclass=FuzzyTerm, group=org).parse(query_to_search)
        results = searcher.search(query, terms=True)
        #print(results[0:])
        tempx = []
        for hit in results:
            #print(hit["content"])
            tempx.append(hit["content"])
            print(tempx[0:])
        '''for r in results:
            print (r, r.score)
            # Was this results object created with terms=True?
            if results.has_matched_terms():
               # What terms matched in the results?
               print(results.matched_terms())
        # What terms matched in each hit?
        print ("matched terms")
        for hit in results:
           print(hit.matched_terms())


        print ("more_results")
        first_hit = results[0]
        more_results = first_hit.more_like_this("content")
        print (more_results)     

     
    found = results.scored_length()
    if results.has_exact_length():
        print("Scored", found, "of exactly", len(results), "documents")
    else:
        low = results.estimated_min_length()
        high = results.estimated_length()
    
        print("Scored", found, "of between", low, "and", high, "documents")   ''' 
"""

if __name__ == "__main__":
    main()    