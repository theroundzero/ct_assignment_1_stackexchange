from operator import itemgetter
import sys

cur_word = None
cur_count = 0
entries = None

for entry in sys.stdin:
    entries, counter = entry.strip().split('\t', 1)
    try:
        counter = int(counter)
    except ValueError:
        continue
    if cur_word == entries:
        cur_count += counter
    else:
        if cur_word:
            print('%s\t%s' % (cur_word, cur_count))
        cur_count = counter
        cur_word = entries
if cur_word == entries:
    print('%s\t%s' % (cur_word, cur_count))
