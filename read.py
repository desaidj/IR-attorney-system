with open('/home/dell/searchengine/cran.all.1400') as f:
    lines = ""
    for l in f.readlines():
        lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
    lines = lines.lstrip("\n").split("\n")
    
# print n lines
n = 5
for l in lines[:n]:
   print(l)
"""
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
        
13
185
52
14
876
15
879
486
142
184
875
37




print(doc_set["2"]) 

"""
