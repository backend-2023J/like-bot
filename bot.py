from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    CallbackContext, 
    Updater, 
    CommandHandler, 
    MessageHandler,
    Filters
    )
import json
import os

TOKEN = os.environ["TOKEN"]

def start(update:Update,context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    
    like = KeyboardButton(text="👍")
    dislike = KeyboardButton(text='👎')

    keyboard = ReplyKeyboardMarkup([[like, dislike]], resize_keyboard=True)

    bot.sendMessage(chat_id,"Welcome to Bot!", reply_markup=keyboard)

def echo(update:Update,context:CallbackContext):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id

    with open('data.json', 'r') as f:
        data = json.loads(f.read())

    like = data['like']
    dislike = data['dislike']

    if text=="👍":
        like += 1
    if text == "👎":
        dislike += 1
    data['like'] = like
    data['dislike'] = dislike

    json_data = json.dumps(data, indent=4)

    with open('data.json', 'w') as f:
        f.write(json_data)

    msg = f"Like: {like}\nDislike: {dislike}"
    bot.sendMessage(chat_id,msg)

updater = Updater(token = TOKEN)
updater.dispatcher.add_handler(CommandHandler("start",start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()