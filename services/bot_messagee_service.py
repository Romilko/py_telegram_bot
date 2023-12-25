from models.models import BotMessage

def set_last_message(chat_id,message_id):
    message = BotMessage().get_or_none(BotMessage.chat_id==chat_id)
    if(message == None):
        message = BotMessage()
    message.chat_id=chat_id
    message.message_id=message_id
    message.save()

def get_last_message(chat_id):
    message = BotMessage().get_or_none(BotMessage.chat_id==chat_id)
    return message