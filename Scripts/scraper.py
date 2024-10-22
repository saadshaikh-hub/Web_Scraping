# scripts/scraper.py

import os  # Import os to handle directories
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape book data from Books to Scrape
def scrape_book_data(url):
    # Create the absolute path for the data directory
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')
    
    # Create data directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print("Data directory created at:", data_dir)

    # Send a GET request to the webpage
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        print(f"Successfully accessed {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return

    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Lists to store scraped data
    book_titles = []
    prices = []
    ratings = []

    # Find book data
    books = soup.find_all('article', class_='product_pod')
    
    if not books:
        print("No books found on the page.")
        return

    for book in books:
        # Scrape book title
        title = book.find('h3').find('a')['title']
        book_titles.append(title)

        # Scrape book price
        price = book.find('p', class_='price_color').text
        prices.append(price)

        # Scrape book rating
        rating = book.find('p', class_='star-rating')['class'][1]
        ratings.append(rating)

    # Create a pandas DataFrame to store the data
    data = pd.DataFrame({
        'Book Title': book_titles,
        'Price': prices,
        'Rating': ratings
    })

    # Define the CSV file path
    csv_file_path = os.path.join(data_dir, 'raw_data.csv')

    # Save the data to a CSV file in the data folder
    try:
        data.to_csv(csv_file_path, index=False)
        print(f"Data scraped and saved successfully to '{csv_file_path}'.")
    except Exception as e:
        print(f"Error saving CSV file: {e}")
        return

    return data

# Example usage
if __name__ == "__main__":
    # URL of the Books to Scrape catalog page
    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    scrape_book_data(url)
