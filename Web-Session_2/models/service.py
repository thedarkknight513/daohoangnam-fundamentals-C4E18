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

# class Customer(Document):
#     name = StringField()
#     gender = IntField()
#     email = StringField()
#     phone_number = StringField()
#     job = StringField()
#     company = StringField()
#     contracted = BooleanField()


# Do thong tin sau khi design khuon
