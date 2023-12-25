import decorator
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton 

@decorator.message_text_and_keyboard
def main_menu(Message,bot):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Тренировка",callback_data="start_training"))
    keyboard.add(InlineKeyboardButton(text="О боте",callback_data="about_bot"))
    keyboard.add(InlineKeyboardButton(text="Мои данные",callback_data="about_user"))
    text = "Главное меню, выбирай:"
    return text, keyboard