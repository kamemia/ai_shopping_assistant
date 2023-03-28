import requests
from bs4 import BeautifulSoup

# Define the URLs of the e-commerce websites and the category of products you want to scrape
urls = ["https://www.jumia.co.ke/womens-dresses/",
        "https://www.aliexpress.com/category/205871601/Dress.html"]

# Loop through each website URL
for url in urls:
    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the product elements on the page
    products = soup.find_all('div', {'class': 'product'})

    # Loop through each product and extract relevant information
    for product in products:
        # Extract the product name
        name = product.find('h2', {'class': 'product-name'}).text.strip()

        # Extract the product price
        price = product.find('span', {'class': 'product-price'}).text.strip()

        # Extract the product image URL
        image_url = product.find('img', {'class': 'product-image'}).get('src')

        # Store the data in a database or file
        # For example, you can use a CSV file to store the data
        with open('data/product_data.csv', 'a') as file:
            file.write(f"{name},{price},{image_url},{url}\n")