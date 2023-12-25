import decorator
import services.exersice_service as exersice_service
import services.result_service as result_service
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton 

@decorator.message_text_and_keyboard
def show_results(Message,bot):
    keyboard = InlineKeyboardMarkup()
    message_text = Message.data
    chat_id = Message.from_user.id
    if message_text.find("exersice")>0:
        exersice_id = message_text.split("exersice/")[1]
        return show_by_exersice(chat_id,exersice_id),keyboard
    else:
        text = "А у тебя еще нет упражнений"
        exersices = exersice_service.find_all_user_Exersice(chat_id)
        if(len(exersices)>0):
            text = "Выбери упражнение по которому хочешь посмотреть результаты"
            for i in exersices:
                keyboard.add(InlineKeyboardButton(text=i.name,callback_data=f"show_results/exersice/{i.id}"))
        return text,keyboard

def show_by_exersice(chat_id, exersice_id):
    text = "Ты еще не выполнял это упражнение"
    results = result_service.find_exersice_results(chat_id,exersice_id)
    if len(results)>0:
        text = f"Вот результаты упражнения {results[0].exersice.name}:\n"
        n = 1
        for i in results:
            text = text +f"{n}. Повторений: {i.set}, вес :{i.weight}, дата: {i.date}.\n"
    return text