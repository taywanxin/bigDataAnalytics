import pandas as pd
import re
import string
from collections import Counter
import time  

import warnings
warnings.filterwarnings("ignore")

# Function to read stopwords from file
def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = set(line.strip() for line in file)
    return stopwords

# Load stopwords
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
    return words

def word_count_analysis(df):
    # Initialize an empty list to hold all words
    all_words = []

    # Append text from each record into the list
    for text in df['cleaned_text']:
        all_words.extend(text)

    # Use Counter to count the occurrences of each word
    word_counts = Counter(all_words)

    # Sort word counts by frequency (descending)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Export the sorted word counts to a text file
    print("Exporting word counts to text file...")
    with open('word_counts_list.txt', 'w') as f:
        for word, count in sorted_word_counts:
            f.write(f'{word:<15} {count}\n')

    print("Word count analysis completed. Word counts saved to 'word_counts_list.txt'.")

def main():
    print("Starting main process...")
    start_time = time.time()  # Start the counter
    
    # Load the TSV file into a DataFrame
    print("Loading the TSV file into a DataFrame...")
    columns_to_keep = ['review_body']  # Specify columns if needed
    df = pd.read_csv('extracted_files/amazon_reviews_us_Wireless_v1_00.tsv', 
                     usecols=columns_to_keep, sep='\t', on_bad_lines='skip')
    
    print(f"Initial DataFrame shape: {df.shape}")

    # Remove rows where review_body is NaN
    df = df.dropna(subset=['review_body'])
    print(f"DataFrame shape after dropping NaN values: {df.shape}")

    # Initialize empty lists to store results
    cleaned_texts = []

    # Process each row and display processing index
    for i, row in df.iterrows():
        if i % 100 == 0:
            print(f"Processing row {i}")
        cleaned_text = clean_text(row['review_body'])
        cleaned_texts.append(cleaned_text)

    # Add results to the DataFrame
    print("Adding results to the DataFrame...")
    df['cleaned_text'] = cleaned_texts

    # Perform word count analysis
    word_count_analysis(df)
    
    end_time = time.time()  # End the counter
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"Task completed in {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
