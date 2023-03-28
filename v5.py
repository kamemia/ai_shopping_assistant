import random
import pandas as pd

# load dataset
df = pd.read_csv('data/fashion.csv')

# define catchphrases for different products
catchphrases = {
    'sunglasses': ['sunglasses', 'sneaker', 'boot'],
    'dress': ['dress', 'gown', 'robe'],
    'shirt': ['shirt', 'blouse', 'top'],
    'pants': ['pants', 'jeans', 'trousers'],
    'jacket': ['jacket', 'coat', 'blazer']
}

# define greeting messages
greetings = ['hi', 'hello', 'hey', 'greetings', 'howdy']

# define farewell messages
farewells = ['bye', 'goodbye', 'see you later', 'have a nice day']

# define function to compare prices
def compare_prices(product, df):
    # filter dataframe for product category
    product_df = df[df['amazon_category_and_sub_category'].str.contains(product)]

    # check if there are any matching products
    if len(product_df) == 0:
        return "Sorry, we couldn't find any products matching that name."

    # convert price column to float data type
    product_df['price'] = product_df['price'].astype(float)

    # get product with the lowest price
    min_product = product_df.loc[product_df['price'].idxmin()]

    # format and return result
    result = f"The {product} with the lowest price is {min_product['product_name']} at ${min_product['price']:.2f}."
    return result

# define function to handle user input
def handle_input(user_input):
    # convert user input to lowercase
    user_input = user_input.lower()

    # check if input is a greeting
    if user_input in greetings:
        return random.choice(greetings).capitalize()

    # check if input is a farewell
    if user_input in farewells:
        return random.choice(farewells).capitalize()

    # check if input is a catchphrase for a product
    for product, catchphrase_list in catchphrases.items():
        for catchphrase in catchphrase_list:
            if catchphrase in user_input:
                return compare_prices(product, df)

    # if input doesn't match any of the above, return default response
    return "I'm sorry, I didn't understand what you're looking for. Please try again with a different search term."

# define function to run the chatbot
def run_chatbot():
    print("Welcome to the shopping chatbot! What are you looking to buy today?")

    while True:
        # get user input
        user_input = input("You: ")

        # handle input and get response
        response = handle_input(user_input)

        # print response
        print("Bot:", response)

        # check if user wants to exit
        if response in farewells:
            break

# run chatbot
run_chatbot()
