from models.models import Exersice
from models.models import User

def find_all_user_Exersice(chat_id):
    exersice = Exersice().select().join(User).where(User.chat_id == chat_id)
    return exersice

def add_exersice(chat_id, exersice_name):
    exersice = Exersice()
    exersice.user = User().get_or_none(User.chat_id==chat_id)
    exersice.name = exersice_name
    exersice.save()

