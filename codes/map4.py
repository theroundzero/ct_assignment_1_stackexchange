import sys
import os
from math import log10,sqrt

Df=10.0

for entries in sys.stdin:
    wordfreq,nNode = entries.strip().split('\t',1)
    t,d,N=nNode.split(' ',2)
    t=float(t)
    N=float(N)
    d=float(d)
    tf_idf= (t/d)*log10(Df/N)
    print('%s\t%s' % (wordfreq,tf_idf))
