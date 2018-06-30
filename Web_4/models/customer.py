from mongoengine import *
class Customer(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone_number = StringField()
    job = StringField()
    company = StringField()
    contracted = BooleanField()