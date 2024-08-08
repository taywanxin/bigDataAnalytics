#!/usr/bin/env python3
import sys

def main():
    lines = []
    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t', 1)
        count = int(count)
        lines.append((word, count))

    lines = sorted(lines, key=lambda x: x[1], reverse=True)

    # Display only the top 10 word counts
    top_10_lines = lines[:10]

    for word, count in top_10_lines:
        print('%s\t%s' % (word, count))

if __name__ == "__main__":
    main()
