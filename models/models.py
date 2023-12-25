from peewee import *
import datetime

db = PostgresqlDatabase('postgres', host='localhost', port=5432, user='postgres', password='postgres')

class User(Model):
    chat_id = CharField()
    name = CharField()
    age = CharField()
    weight = CharField()
    def __str__(self):
       return f"Name: {self.name}, chat if: {self.chat_id}."
    class Meta:
      database=db

class Exersice(Model):
   name = CharField()
   user = ForeignKeyField(User)
   def __str__(self):
       return f"Name: {self.name}."
   class Meta:
      database=db

class Results(Model):
   set = CharField()
   weight = CharField()
   date = DateField(default=datetime.datetime.now)
   user = ForeignKeyField(User)
   exersice = ForeignKeyField(Exersice)
   class Meta:
      database=db

class BotMessage(Model):
   chat_id = CharField()
   message_id = CharField()
   class Meta:
      database=db

class ConnsetToDb():
   def connect():
      db.connect()
      # db.drop_tables([User,BotMessage,Exersice,Results])
      db.create_tables([User,BotMessage,Exersice,Results])   
   

