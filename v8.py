import pandas as pd

# Load the dataset
df = pd.read_csv('data/dummy.csv')

# Function to find the cheapest price of a product
def find_cheapest_price(product_name):
    # Filter the dataset for the given product name
    product_df = df[df['product_name'] == product_name]
    
    # If no results are found, return None
    if len(product_df) == 0:
        return None
    
    # Find the row with the cheapest price
    cheapest_row = product_df.iloc[product_df['Price'].idxmin()]
    
    # Extract the price and return it
    cheapest_price = cheapest_row['Product_price']
    return cheapest_price

# Greeting message
print("Hi! I'm your shopping assistant. How can I help you today?")

# Chat loop
while True:
    # Get user input
    user_input = input("> ").lower()
    
    # Check if the user wants to quit
    if user_input in ['quit', 'exit', 'bye', 'goodbye']:
        print("Goodbye!")
        break
    
    # Check if the user is asking for a product price
    if 'price of' in user_input:
        # Extract the product name from the user input
        product_name = user_input.replace('price of', '').strip()
        
        # Find the cheapest price of the product
        cheapest_price = find_cheapest_price(product_name)
        
        # If the product is not found, inform the user
        if cheapest_price is None:
            print("Sorry, I couldn't find any results for that product.")
        else:
            # Otherwise, print the cheapest price
            print("The cheapest price for {} is ${}.".format(product_name, cheapest_price))
        
    else:
        # If the user input is not recognized, ask them to try again
        print("Sorry, I didn't understand that. Could you please try again?")
