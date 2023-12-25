import services.user_service as service
import decorator

name ="test"
age ="test"
weight="test"

@decorator.message_text_decorator
def new_user_registration(Message,bot):
    text = "Привет, ты видно новенький, давай зарегаем. Как зовут?"
    bot.register_next_step_handler(Message,set_age,bot)
    return text

@decorator.message_text_decorator
def set_age(Message,bot):
        global name
        name = Message.text
        text = "Сколько тебе лет?"
        bot.register_next_step_handler(Message,set_weight,bot)
        return text

@decorator.message_text_decorator
def set_weight(Message,bot):
        global age
        age = Message.text
        text = "Сколько весишь?"
        bot.register_next_step_handler(Message,test,bot)
        return text

@decorator.message_text_decorator
def test(Message,bot):
        global weight
        weight = Message.text
        chat_id = Message.from_user.id
        user = service.add(chat_id,name,age,weight)
        text = f"Мы тебя зарегали =). Имя: {user.name},возраст: {user.age}, вес: {user.weight}."
        return text