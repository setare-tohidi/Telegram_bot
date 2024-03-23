import telebot

class IsAdmin(telebot.custom_filters.SimpleCustomeFilter):
    key='is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id, message.from_user.id).status in ['administrator', 'creator']