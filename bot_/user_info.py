import services.user_service as service
import decorator

sets={}
name ="name"
age ="age"
sets[0]={"name":name,"age":age}

@decorator.message_text_decorator
def new_user_registration(Message,bot):
    text = "Привет, ты видно новенький, давай зарегаем. Как зовут?"
    bot.register_next_step_handler(Message,set_age,bot)
    return text

@decorator.message_text_decorator
def set_age(Message,bot):
        chat_id = Message.from_user.id
        global sets
        name = Message.text
        sets[chat_id]={"name":name}
        text = "Сколько тебе лет?"
        bot.register_next_step_handler(Message,set_weight,bot)
        return text

@decorator.message_text_decorator
def set_weight(Message,bot):
        chat_id = Message.from_user.id
        global sets
        age = Message.text
        sets[chat_id]["age"]=age
        text = "Сколько весишь?"
        bot.register_next_step_handler(Message,test,bot)
        return text

@decorator.message_text_decorator
def test(Message,bot):
        global sets
        chat_id = Message.from_user.id
        name = sets[chat_id]["name"]
        age = sets[chat_id]["age"]
        weight = Message.text
        chat_id = Message.from_user.id
        user = service.add(chat_id,name,age,weight)
        text = f"Мы тебя зарегали =). Имя: {user.name},возраст: {user.age}, вес: {user.weight}."
        return text