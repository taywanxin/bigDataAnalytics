#!/usr/bin/env python3
import dask.dataframe as dd
import sys

def extract_review_body(input_file, output_file):
    # Specify columns to keep
    columns_to_keep = ['review_body']
    # Read the dataset using Dask
    df = dd.read_csv(input_file, usecols=columns_to_keep, sep='\t', assume_missing=True)
    # Drop rows with NaN values in 'review_body'
    df = df.dropna(subset=['review_body'])
    # Save the cleaned review_body to a new file
    df.to_csv(output_file, index=False, header=False, sep='\t', single_file=True)
    print(f"Saved cleaned data to {output_file}")

if __name__ == "__main__":
    input_file = sys.argv[1] 
    output_file = sys.argv[2]
    extract_review_body(input_file, output_file)
