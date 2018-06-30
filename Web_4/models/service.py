from mongoengine import *

#1. Design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    measurement = ListField()
  
class Customer(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone_number = StringField()
    job = StringField()
    company = StringField()
    contracted = BooleanField()

class User(Document):
    user_name = StringField()
    pass_word = StringField()
    email = StringField()
    full_name = StringField()

class Order(Document):
    service_id = StringField()
    user_id = StringField()
    order_time = StringField()
    is_accepted = BooleanField()



# Do thong tin sau khi design khuon
