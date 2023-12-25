from models.models import User

def add(chat_id,name,age,weight):
    user = User()
    user.chat_id =chat_id
    user.name=name
    user.age=age
    user.weight=weight
    user.save()
    return user

def find_by_id(id):
    user = User().get_or_none(User.chat_id==id)
    return user