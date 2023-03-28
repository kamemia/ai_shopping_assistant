import csv
import random
from nltk.tokenize import word_tokenize

def load_data():
    products = []
    with open('data/fashion.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip the header row
        for row in reader:
            products.append(tuple(row))
    return products

def process_input(user_input, products):
    # Tokenize the user input
    tokens = word_tokenize(user_input.lower())

    # Check if the user wants to compare prices of a product
    if 'compare' in tokens and 'price' in tokens:
        # Extract the product name
        product_name = None
        for i, token in enumerate(tokens):
            if token in ['of', 'for']:
                product_name = ' '.join(tokens[i+1:])
                break

        # Find the product in the data
        if product_name:
            matches = []
            for product in products:
                if product_name.lower() in product[0].lower():
                    matches.append(product)

            if len(matches) > 0:
                # Sort the matches by price
                matches.sort(key=lambda x: float(x[2].replace('$', '')))

                # Print the cheapest match
                cheapest = matches[0]
                return f"The cheapest {product_name.title()} on Amazon is {cheapest[0]} at {cheapest[2]}"

    # If we haven't returned anything yet, return a default message
    return "I'm sorry, I don't understand. Can you please rephrase your request?"

def main():
    # Load the product data
    products = load_data()

    # Greet the user
    print("Hi! I'm a shopping assistant. How can I help you today?")

    # Start the chat loop
    while True:
        # Get user input
        user_input = input("> ")

        # Process user input
        response = process_input(user_input, products)

        # Print the chatbot's response
        print(response)

if __name__ == '__main__':
    main()
