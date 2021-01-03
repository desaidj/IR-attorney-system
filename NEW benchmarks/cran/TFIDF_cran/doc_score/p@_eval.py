from os.path import exists
import traceback


FILE_NAME = ""

def main():
    global NO_OF_QUERIES,FILE_NAME
    FILE_NAME = raw_input(">\tEnter the file name of the doc_score with proper extension\n")
    if exists(FILE_NAME):
        
        file_rank_list = open (FILE_NAME, 'r')
        tot = 0
        for l in file_rank_list.readlines():
            x =  l.split(" ")[1]
            tot+= float(x)
        print('The P@x is', float(tot/225))
        file_rank_list.flush()
        file_rank_list.close()
    else:
        print "The file does not exist"

main()
