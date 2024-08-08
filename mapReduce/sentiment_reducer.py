#!/usr/bin/env python3
from operator import itemgetter
import sys

current_sentiment = None
current_count = 0
sentiment = None

try:
    for line in sys.stdin:
        line = line.strip()
        print(f"DEBUG: Processing line: {line}", file=sys.stderr) 
        sentiment, count = line.split('\t', 1)

        try:
            count = int(count)
        except ValueError:
            continue

        if current_sentiment == sentiment:
            current_count += count
        else:
            if current_sentiment:
                print('%s\t%s' % (current_sentiment, current_count))
            current_count = count
            current_sentiment = sentiment

    if current_sentiment == sentiment:
        print('%s\t%s' % (current_sentiment, current_count))
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
