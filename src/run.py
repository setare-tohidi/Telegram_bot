from loguru import logger
from src.utils.io import write_json
from telebot import types
from src.constants import keyboards
from src.utils import bot
from src.utils.filters import IsAdmin
from src.bot import bot
import emoji
 



class Bot:
    def __init__(self, telebot):
        self.bot=telebot
        
        # Add costume filters:
        self.bot.add_costume_filter(IsAdmin())
        
        # register handlers
        self.handlers()
        
        # run bot
        logger.info('Bot is running...')
        self.bot.infinity_polling()
        
    
    def handlers(self):
        @self.bot.message_handler(is_admin=True)
        def admin_of_group(message):
            self.send_message(message.chat.id, "You are admin of this group")
        
        @self.bot.message_handler(func=lambda: True)
        def echo(message):
            self.send_message(
                message.chat.id, message.text,
                reply_markup=keyboards.main
                )
            
    def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        
        """
        Send message to telegram bot
        """
        if emojize:
            text=emoji.emojize(text)
        
        self.bot.send_message(chat_id, text, reply_markup=reply_markup)
            
            
if __name__=='__main__':
    logger.info('Bot started')
    inconnu_bot=Bot(telebot=bot)
    inconnu_bot.run()
    
    