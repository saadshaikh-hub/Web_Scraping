# scripts/data_cleaner.py

import pandas as pd
import os

def clean_book_data(raw_file_path, cleaned_file_path):
    # Load the raw data
    try:
        data = pd.read_csv(raw_file_path)
        print(f"Raw data loaded from {raw_file_path}.")
    except FileNotFoundError:
        print(f"File not found: {raw_file_path}")
        return
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Display the first few rows of the raw data
    print("Raw Data Preview:")
    print(data.head())

    # Remove rows with any missing values
    cleaned_data = data.dropna()
    
    # Optionally reset the index
    cleaned_data.reset_index(drop=True, inplace=True)

    # Display the first few rows of the cleaned data
    print("Cleaned Data Preview:")
    print(cleaned_data.head())

    # Save the cleaned data to a new CSV file
    try:
        cleaned_data.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned data saved to {cleaned_file_path}.")
    except Exception as e:
        print(f"Error saving cleaned data: {e}")

# Example usage
if __name__ == "__main__":
    # Define paths for raw and cleaned data files
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')
    raw_file_path = os.path.join(data_dir, 'raw_data.csv')
    cleaned_file_path = os.path.join(data_dir, 'cleaned_data.csv')
    
    # Clean the book data
    clean_book_data(raw_file_path, cleaned_file_path)
