#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        words = line.split()
        for word in words:
            print('%s\t%s' % (word, 1))
