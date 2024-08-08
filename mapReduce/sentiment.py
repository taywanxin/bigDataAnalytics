#!/usr/bin/env python3
import sys
from textblob import TextBlob
import time

def analyze_sentiment(text):
    review = TextBlob(text)
    if review.sentiment.polarity < 0:
        return 'Negative'
    elif review.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Positive'

def main(input_file, output_file):
    start_time = time.time() 
    line_count = 0
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            text = line.strip()
            sentiment = analyze_sentiment(text)
            outfile.write(sentiment + '\n')
            line_count += 1
            if line_count % 1000 == 0:
                print(f"Processed {line_count} lines")
    end_time = time.time()
    total_time = end_time - start_time 
    print(f"Total time taken: {total_time:.2f} seconds")

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
