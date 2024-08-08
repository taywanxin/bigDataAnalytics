#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        sentiments = line.split()
        for sentiment in sentiments:
            print('%s\t%s' % (sentiment, 1))
