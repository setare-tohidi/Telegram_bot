import telebot
import os
from loguru import logger
from src.utils.io import write_json
from telebot import types
from src.constants import keyboards
import emoji
class Bot:
   '''
   Telegram bot to connect two random people  
   '''
   def __init__(self):
      self.bot=telebot.TeleBot(os.environ['inconnu_bot_token'])
      self.echo_all=self.bot.message_handler(func=lambda m: True)(self.echo_all)
      
   def run(self):
      logger.info('Bot is running...')
      self.bot.infinity_polling()
   
   def echo_all(self, message):
      write_json(message.json, 'message.json')
      self.bot.send_message(message.chat.id, message.txt,
                            reply_markup=keyboards.main)
   
   
   
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# bot.reply_to(message, message.text)
 
 
if __name__ == '__main__':
   logger.info('Bot started')
   bot=Bot()
   bot.run()
