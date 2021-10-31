#!/usr/bin/env python

import sys
import os

for entry in sys.stdin:
    entry = entry.strip()
    line_word,counter=entry.split('\t',1)
    map_word,fname=line_word.split(' ',1)
    map_counter=map_word+' '+counter
    print('%s\t%s' % (fname, map_counter))
