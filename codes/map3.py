import sys
import os

for entries in sys.stdin:
    wordfile,corpus_counter = entries.strip().split('\t',1)
    word,filename=wordfile.split(' ',1)
    mapcounter=filename+' '+corpus_counter+' '+str(1)
    print('%s\t%s' % (word,mapcounter))
