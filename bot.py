import telebot
import services.user_service as service
import bot_.user_info as user_info
from models.models import ConnsetToDb
import bot_.bot_info as bot_info
import bot_.show_user_info as show_user_info
import bot_.main_menu as main_menu
import bot_.start_training as start_training
import bot_.show_results as show_results
bot = telebot.TeleBot("6196473654:AAHvg4cwgO8H62EGfqz9i2JaOvG-x0rZnFM")
ConnsetToDb.connect()

@bot.message_handler(content_types=["text"])
def start(Message):
        chat_id = Message.from_user.id
        if service.find_by_id(chat_id)==None:
            user_info.new_user_registration(Message,bot)
        else:
            main_menu.main_menu(Message,bot)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    data = call.data
    if data.startswith("start_training"):
        start_training.start_training(call,bot)
    elif data.startswith("about_bot"):
        bot_info.show_bot_info(call,bot)
    elif data.startswith("about_user"):
        show_user_info.show_user_info(call,bot)
    elif data.startswith("show_results"):
        show_results.show_results(call,bot)

bot.register_next_step_handler_by_chat_id
bot.polling(none_stop=True, interval=0)