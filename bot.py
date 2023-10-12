from telegram import (
    Update,
    KeyboardButton, 
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup
    )
from telegram.ext import (
    CallbackContext, 
    Updater, 
    CommandHandler, 
    MessageHandler,
    Filters,
    CallbackQueryHandler
    )
import json

from likedb import LikeDB

db = LikeDB('data.json')

TOKEN = "6388893107:AAHm55DuPheZmctXz5mX5HnSfD9zfgmpNhY"

def start(update:Update,context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    db.add_user(chat_id)

    bot.sendMessage(chat_id,"Send me image")

def helping(update:Update,context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id

    bot.sendMessage(chat_id,"help")


def image(update:Update,context:CallbackContext):

    file_id = update.message.photo[0]['file_id']

    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id

    print(update.message.message_id)
    like = InlineKeyboardButton(text="👍", callback_data="like")
    dislike = InlineKeyboardButton(text='👎', callback_data="dislike")

    keyboard = InlineKeyboardMarkup([[like, dislike]])
    bot.sendPhoto(chat_id, photo=file_id, reply_markup=keyboard)


def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    print(query.message.message_id)
    data = query.data
    chat_id = query.message.chat.id

    if data=="like":
        db.add_like(chat_id)
    if data == "dislike":
        db.add_dislike(chat_id)

    like = db.get_likes(chat_id)
    dislike = db.get_dislikes(chat_id)

    like = InlineKeyboardButton(text=f"👍 {like}", callback_data="like")
    dislike = InlineKeyboardButton(text=f'👎 {dislike}', callback_data="dislike")
    query.answer(text=f"{data}")

    keyboard = InlineKeyboardMarkup([[like, dislike]])
    query.edit_message_reply_markup(reply_markup=keyboard)
    


updater = Updater(token = TOKEN)
updater.dispatcher.add_handler(CommandHandler("start",start))
updater.dispatcher.add_handler(CommandHandler("help",helping))
updater.dispatcher.add_handler(MessageHandler(Filters.photo,image))
updater.dispatcher.add_handler(CallbackQueryHandler(callback))

updater.start_polling()
updater.idle()