import random
import pandas as pd

# load the dataset
df = pd.read_csv('data/amazon_products.csv')

# define the catchphrases for different products
catchphrases = {
    'television': ['tv', 'television'],
    'smartphone': ['smartphone', 'phone', 'mobile'],
    'laptop': ['laptop', 'notebook'],
    'headphones': ['headphones', 'earphones', 'earbuds']
}

# function to extract the product details based on the catchphrase
def extract_product_details(catchphrase):
    for product, keywords in catchphrases.items():
        for keyword in keywords:
            if keyword in catchphrase.lower():
                # extract the details of the product with the lowest price
                df_product = df[df['product_category'] == product]
                df_product = df_product[df_product['price'] == df_product['price'].min()]
                product_name = df_product['product_title'].iloc[0]
                product_price = df_product['price'].iloc[0]
                return product_name, product_price
    return None, None

# function to generate a greeting
def generate_greeting():
    greetings = ['Hi there!', 'Hello!', 'Hey!']
    return random.choice(greetings)

# main function to handle user input
def respond(user_input):
    if 'hi' in user_input.lower() or 'hello' in user_input.lower() or 'hey' in user_input.lower():
        response = generate_greeting()
    else:
        product_name, product_price = extract_product_details(user_input)
        if product_name:
            response = f"The product with the lowest price for {user_input} is {product_name} which costs {product_price} dollars."
        else:
            response = "I'm sorry, I could not find any products that match your query."
    return response

# example usage
print(generate_greeting())
print(respond("I want to buy a new TV"))