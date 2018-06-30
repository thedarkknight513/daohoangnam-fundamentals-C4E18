from models.service import Service
# from models.service import Customer
import mlab
# import mlab2hw

from faker import Faker
from random import randint, choice

mlab.connect()
# mlab2hw.connect()

fake = Faker()

for i in range(50):
    print("Saving service", i + 1, "...")
    description_list_1 = ["Ngoan", "Hien","Le phep"]
    description_list_2 = ["Nau an ngon", "diu dang", "hung du"]
    new_service = Service(
        name = fake.name(),
        yob = randint(1990,2000),
        gender = randint(0,1),
        height = randint(155, 190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([True, False]),
        description = choice(description_list_1) + ", "+ choice(description_list_2),
        # measurment = str(randint(70,100))+", "+ str(randint(70,100)) +", "+str(randint(70,100))
        measurement = [randint(70,100), randint(70,100), randint(70,100)]
        )
    new_service.save()

# for i in range(29):
#     print("Saving",i+1, "...")
#     new_customer = Customer(
#         name = fake.name(),
#         email = fake.safe_email(),
#         phone_number = fake.phone_number(),
#         job = fake.job(),
#         gender = choice([1,0]),
#         company = fake.company(),
#         contracted = choice([True, False])
#     )
#     new_customer.save()
