import pandas as pd
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Chat
import re

# Load dataset
products_df = pd.read_csv('data/amazon.csv')

# Define chatbot function
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm an AI Shopping chatbot. What can I help you with today?")

def handle_message(update, context):
    user_input = update.message.text.lower()
    
    # Check if the user wants to quit
    if user_input in ['quit', 'exit', 'bye', 'goodbye']:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Have a great day!")
        return
    
    # Check if the user wants to list all products
    if user_input == "list":
        products_str = products_df.to_string(index=False)
        context.bot.send_message(chat_id=update.effective_chat.id, text=products_str)
        return
    
    # Check if the user wants to purchase a product
    if re.search(r'i want to (purchase|buy|shop for) (.+)', user_input):
        product_name = re.search(r'i want to (purchase|buy|shop for) (.+)', user_input).group(2)
        product = products_df[products_df['product_name'].str.contains(product_name, case=False)]
        
        if len(product) == 0:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I couldn't find any products with that name.")
        else:
            min_price = product['product_price'].min()
            url = product['product_url'].iloc[0]
            response_str = f"The cheapest price for {product_name} is {min_price}.\nYou can purchase it using this link {url}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=response_str)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand your request. Please try again.")
        
# Create an updater object
updater = Updater(token='6184481425:AAGaQZwdAgS6Umxeqmsz1hnq9GtJVUNsUK0', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Add handlers for commands and messages
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, handle_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C
updater.idle()
