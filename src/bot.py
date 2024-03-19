import telebot
import os
from loguru import logger

# export inconnu_bot_token=7064417063:AAF82dz9rUlVfd8tA_19mu4qUJ2gJ1wwAIs
bot = telebot.TeleBot(os.environ['inconnu_bot_token']) # You can set parse_mode by default. HTML or MARKDOWN



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
 
 
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
 
 
logger.info('Bot started')
bot.infinity_polling()
logger.info("Done!")
 