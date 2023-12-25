import decorator
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton 
import services.exersice_service as service
import services.result_service as result_service


set =""

@decorator.message_text_and_keyboard
def start_training(Message,bot):
    message_text = Message.data
    chat_id = Message.from_user.id
    exersices = service.find_all_user_Exersice(chat_id)
    text = ""
    keyboard = InlineKeyboardMarkup()
    if message_text.find("add_exersice")>0:
            text = "Введи название упражнения"
            bot.register_next_step_handler_by_chat_id(Message.from_user.id,add_exersice,bot)
    elif message_text.find("result")>0:
            text = "Введи количество повторений."
            bot.register_next_step_handler_by_chat_id(Message.from_user.id,add_set,bot,message_text.split("result/")[1])
    else:
        if len(exersices) == 0:
            text = "А ты еще не добавил свои упражнения, введи название что б продолжить."
            bot.register_next_step_handler_by_chat_id(Message.from_user.id,add_exersice,bot)
        else:
            text = "Выбирай упражнение"
            for i in exersices:
                keyboard.add(InlineKeyboardButton(text=i.name,callback_data=f"start_training/result/{i.id}"))
            keyboard.add(InlineKeyboardButton(text="Добавить упражнение",callback_data="start_training/add_exersice"))
    return text,keyboard

@decorator.message_text_decorator
def add_exersice(Message,bot):
    chat_id = Message.from_user.id
    exersice_name = Message.text
    service.add_exersice(chat_id,exersice_name)
    text = f"Упражнение {exersice_name} успешно добавлено"
    return text

@decorator.message_text_decorator
def add_set(Message,bot,exersice_id):
    global set
    set = Message.text
    chat_id = Message.from_user.id 
    text = "Сколько вес?"
    bot.register_next_step_handler_by_chat_id(chat_id,add_weight,bot,exersice_id)
    return text
    

@decorator.message_text_decorator
def add_weight(Message,bot,exersice_id):
    chat_id = Message.from_user.id 
    text = "Ну ты зверюга."
    result_service.add_result(chat_id,exersice_id,set,Message.text)
    return text
