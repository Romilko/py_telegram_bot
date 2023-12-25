import services.user_service as service
import decorator

@decorator.message_text_decorator
def show_user_info(Message,bot):
    chat_id = Message.from_user.id
    user = service.find_by_id(chat_id)
    text =  f"Тебя зовут {user.name}, возраст {user.age}, вес {user.weight}."
    return text