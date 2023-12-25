from models.models import Results
from models.models import User
from models.models import Exersice


def add_result(chat_id,exersice_id,set,weight):
    result = Results()
    result.user = User().get_or_none(User.chat_id==chat_id)
    result.exersice = Exersice().get_or_none(Exersice.id == exersice_id)
    result.set = set
    result.weight = weight
    result.save()

def find_exersice_results(chat_id,exersice_id):
    results = Results().select().join(Exersice).where(Exersice.id==exersice_id).switch(Results).join(User).where(User.chat_id == chat_id)
    print("hello")
    return results