import pandas as pd
import numpy as np

# load the fashion dataset
df = pd.read_csv("data/amazon.csv")

# preprocess the dataset
# df['price'] = df['price'].apply(lambda x: float(x.replace(',', '').replace('$', '')) if isinstance(x, str) else np.nan)
# df = df.dropna(subset=['price'])
# df = df.reset_index(drop=True)

# define catchphrases
catchphrases = {
    "sunglasses": ["sunglasses", "sneakers", "boots", "sandals"],
    "lego": ["lego", "blouses", "sweatshirts", "hoodies"],
    "bottoms": ["pants", "jeans", "shorts", "skirts"],
    "accessories": ["hats", "bags", "sunglasses", "watches"]
}

# define greetings
greetings = ["hi", "hello", "hey"]

def get_product_category(user_input):
    """
    Takes in user input and returns the corresponding product category based on the catchphrases defined.
    """
    for category, phrases in catchphrases.items():
        for phrase in phrases:
            if phrase in user_input.lower():
                return category
    return None

def get_product(product_name):
    """
    Takes in the name of a product and returns the product with the closest match from the fashion dataset.
    """
    df['product_name'] = df['product_name'].astype(str)
    distances = np.array([np.linalg.norm(np.array(list(map(ord, product_name))) - np.array(list(map(ord, name))))
                          for name in df['product_name']])
    closest_idx = distances.argmin()
    return df.loc[closest_idx, 'product_name'], df.loc[closest_idx, 'product_price'], df.loc[closest_idx, 'product_url']

def chat():
    """
    Initiates the chatbot and handles user input.
    """
    print("Hello! I'm a shopping assistant. How can I help you today?")
    while True:
        user_input = input().lower()
        if user_input in greetings:
            print("Hi there! How can I assist you today?")
        else:
            category = get_product_category(user_input)
            if category:
                print(f"Sure, I can help you find {category}. What specific product are you looking for?")
                product_name = input().lower()
                product, price, url = get_product(product_name)
                print(f"I found {product} for ${price:.2f}. You can purchase it here: {url}")
            else:
                print("I'm sorry, I didn't understand your request. Please try again.")
        
if __name__ == '__main__':
    chat()