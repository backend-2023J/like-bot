from telegram import Update
from telegram.ext import (
    CallbackContext, 
    Updater, 
    CommandHandler, 
    MessageHandler,
    Filters
    )

import os

TOKEN = os.environ["TOKEN"]

def start(update:Update,context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id,"Welcome to Bot!")

def echo(update:Update,context:CallbackContext):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    
    like = 
    dislike = 

    if text=="👍":
        like += 1
    if text == "👎":
        dislike += 1
        
    msg = f"Like: {like}\nDislike: {dislike}"

    bot.sendMessage(chat_id,msg)

updater = Updater(token = TOKEN)
updater.dispatcher.add_handler(CommandHandler("start",start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()