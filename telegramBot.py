import logging
import telegram

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from dotenv import dotenv_values
config = dotenv_values()

MY_TELEGRAM_CHAT_ID = '736836709'

bot = telegram.Bot(config["telegram_bot_token"])

def sendMeme(meme):
    try:
        print(meme)    
        bot.send_message(chat_id=MY_TELEGRAM_CHAT_ID, text=meme['name'])
        # for send .gif and H.264/MPEG-4 AVC video without sound
        if '.gif' in meme['file'] or '.mp4' in meme['file']:
            bot.send_animation(chat_id=MY_TELEGRAM_CHAT_ID, animation=open(meme['file'], 'rb'))
        else:
            # Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), 
            # pass an HTTP URL as a String for Telegram to get a photo from the Internet, or 
            # upload a new photo using multipart/form-data. Lastly you can pass an existing
            bot.send_photo(chat_id=MY_TELEGRAM_CHAT_ID, photo=open(meme['file'], 'rb'))
    except Exception as e: 
        print("error sending meme through telegram")
        print(e)