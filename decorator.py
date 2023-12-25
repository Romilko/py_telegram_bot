import services.bot_messagee_service as bot_service

def message_text_decorator(func):
    def wrapper(*args,**kwargs):
        chat_id = args[0].from_user.id
        bot = args[1]
        last_bot_message = bot_service.get_last_message(chat_id)
        if last_bot_message != None:
                try:
                    bot.delete_message(chat_id,last_bot_message.message_id)
                except:
                    None
        text = func(*args,**kwargs)
        bot_message = bot.send_message(chat_id,text)
        bot_service.set_last_message(chat_id,bot_message.message_id)
    return wrapper

def message_text_and_keyboard(func):
    def wrapper(*args,**kwargs):
        chat_id = args[0].from_user.id
        bot = args[1]
        last_bot_message = bot_service.get_last_message(chat_id)
        if last_bot_message != None:
                try:
                    bot.delete_message(chat_id,last_bot_message.message_id)
                except:
                    None
        text,keyboard = func(*args,**kwargs)
        bot_message = bot.send_message(chat_id,text,reply_markup = keyboard)
        bot_service.set_last_message(chat_id,bot_message.message_id)
    return wrapper