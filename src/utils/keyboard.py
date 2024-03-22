
from telebot import types
from src.utils.keyboard import create_keybaord
import emoji


def create_keybaord(*keys, row_width=2, resize_keyboard=True):
    markup=types.ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=resize_keyboard
    )
    
    keys=map(emoji.emojize, keys)
    buttons=map(types.KeyboardButton, keys)
    markup.add(*buttons)
    return markup
