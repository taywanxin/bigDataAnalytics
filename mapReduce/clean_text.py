#!/usr/bin/env python3
import re
import string
import time
import sys

def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = set(line.strip() for line in file)
    return stopwords

stop_words = load_stopwords('stopwords-en.txt')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)  # Remove content inside angle brackets
    text = re.sub(r'\[.*?\]', '', text)  # Remove content inside square brackets
    text = re.sub(r'\w*\d\w*', '', text)  # Remove words containing numbers
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)  # Remove punctuation
    text = re.sub('[‘’“”…]', '', text)  # Remove specific typographic quotation marks
    text = re.sub('\n', '', text)  # Remove newline characters
    words = text.split()
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    return ' '.join(words)

def main(input_file, output_file):
    start_time = time.time()
    line_count = 0
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            cleaned_line = clean_text(line.strip())
            outfile.write(cleaned_line + '\n')
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
