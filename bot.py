from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    CallbackContext, 
    Updater, 
    CommandHandler, 
    MessageHandler,
    Filters
    )
import json

from likedb import LikeDB

db = LikeDB('data.json')

TOKEN = "6388893107:AAHm55DuPheZmctXz5mX5HnSfD9zfgmpNhY"

def start(update:Update,context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    db.add_user(chat_id)
    like = KeyboardButton(text="👍")
    dislike = KeyboardButton(text='👎')

    keyboard = ReplyKeyboardMarkup([[like, dislike]], resize_keyboard=True)

    bot.sendMessage(chat_id,"Welcome to Bot!", reply_markup=keyboard)

def echo(update:Update,context:CallbackContext):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id

    if text=="👍":
        db.add_like(chat_id)
    if text == "👎":
        db.add_dislike(chat_id)

    like = db.get_likes(chat_id)
    dislike = db.get_dislikes(chat_id)

    msg = f"Like: {like}\nDislike: {dislike}"
    bot.sendMessage(chat_id,msg)

updater = Updater(token = TOKEN)
updater.dispatcher.add_handler(CommandHandler("start",start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()