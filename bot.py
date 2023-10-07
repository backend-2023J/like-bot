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
from likedb import LikeDB

db = LikeDB('data.json')

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

    data = db.data

    if text=="👍":
        db.add_like()
    if text == "👎":
        db.add_dislike()

    like = data['like']
    dislike = data['dislike']

    msg = f"Like: {like}\nDislike: {dislike}"
    bot.sendMessage(chat_id,msg)

updater = Updater(token = TOKEN)
updater.dispatcher.add_handler(CommandHandler("start",start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()