import telebot
import os
from loguru import logger
from src.utils.io import write_json
from telebot import types


markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
itembtn1 = types.KeyboardButton('connect')
itembtn2 = types.KeyboardButton('settings')
# itembtn3 = types.KeyboardButton('d')
markup.add(itembtn1, itembtn2, itembtn3)
# tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)

# or add KeyboardButton one row at a time:
# markup = types.ReplyKeyboardMarkup()
# itembtna = types.KeyboardButton('a')
# itembtnv = types.KeyboardButton('v')
# itembtnc = types.KeyboardButton('c')
# itembtnd = types.KeyboardButton('d')
# itembtne = types.KeyboardButton('e')
# markup.row(itembtna, itembtnv)
# markup.row(itembtnc, itembtnd, itembtne)
# tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)




# export inconnu_bot_token=7064417063:AAF82dz9rUlVfd8tA_19mu4qUJ2gJ1wwAIs
# bot = telebot.TeleBot(os.environ['inconnu_bot_token']) # You can set parse_mode by default. HTML or MARKDOWN
class Bot:
   def __init__(self):
      self.bot=telebot.TeleBot(os.environ['inconnu_bot_token'])
      self.echo_all=self.bot.message_handler(func=lambda m: True)(self.echo_all)
      
   def run(self):
      logger.info('Bot is running...')
      self.bot.infinity_polling()
   
   def echo_all(self, message):
      write_json(message.json, 'message.json')
      self.bot.send_message(message.chat.id, message.txt,
                            reply_markup=markup)
   
   
   
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# bot.reply_to(message, message.text)
 
 
if __name__ == '__main__':
   logger.info('Bot started')
   bot=Bot()
   bot.run()
