import pandas as pd
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram import Chat

# Load dataset
products_df = pd.read_csv('data/amazon.csv')

# Define chatbot function
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm an AI Shopping chatbot. What can I help you with today?")

def handle_message(update, context):
    
    user_input = update.message.text

    if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Have a beautiful day!")
        return

    if user_input.lower() == "list":
        products_str = products_df.to_string(index=False)
        context.bot.send_message(chat_id=update.effective_chat.id, text=products_str)
        return

    product = products_df[products_df['product_name'].str.contains(user_input, case=False)]
    if len(product) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I couldn't find any products with that name.")
    else:
        min_price = product['product_price'].min()
        url = product['product_url'].iloc[0]
        response_str = f"The cheapest price for {user_input} is {min_price}.\nYou can purchase it using this link {url}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=response_str)

# Create an updater object
updater = Updater(token='6252407074:AAEAHrjMOS9X27icJmrwX-m3NdoEc_BWm6M', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Add handlers for commands and messages
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(filters.text, handle_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C
updater.idle()
