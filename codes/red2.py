
from operator import itemgetter
import sys

cur_word = None
prev_fname = None
cur_count = 0
word = None
N=0
df={}
entry_word=[]


for entry in sys.stdin:
    entry_word.append(entry.strip())
    fname,wordcounter = entry.split('\t', 1)
    word,counter = wordcounter.split(' ', 1)
    counter=int(counter)
    if prev_fname == fname:
        N=N+counter
    else:
       if prev_fname != None:
            df[prev_fname]=N
       N=0
       prev_fname = fname
df[prev_fname]=N


for entry in entry_word:
    fname,wordcounter = entry.split('\t', 1)
    word,counter = wordcounter.split(' ', 1) 
    for data in df:
        if fname == data:
           word_freq=word+' '+fname
           count_corpus=counter+' '+str(df[data])
           print('%s\t%s' % (word_freq,count_corpus))
