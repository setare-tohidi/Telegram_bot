import telebot
import os

# export inconnu_bot_token=7064417063:AAF82dz9rUlVfd8tA_19mu4qUJ2gJ1wwAIs
bot = telebot.TeleBot(os.environ['inconnu_bot_token']) # You can set parse_mode by default. HTML or MARKDOWN
