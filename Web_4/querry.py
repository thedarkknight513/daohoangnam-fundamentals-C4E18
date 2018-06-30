from models.service import Service
from models.service import User
import mlab

mlab.connect()

# all_service = Service.objects()  #kieu du lieu: list
# first_service = all_service[0]
# print(first_service)
# print(first_service.to_mongo())  # nhin ro object. kieu du lieu: dictionary
# print(first_service["name"]) 
# print(first_service.name)
# print(first_service.address)

id_to_find = "5b2fad860cc1751f041b06eb"

# to read
# hera1 = Service.objects(id = id_to_find)

# hera2 = Service.objects().get(id = id_to_find)
service = Service.objects().with_id(id_to_find)


#print
# print(hera1)
# print(hera2.to_mongo()) #to_mongo: Nhin het field
# print(hera3.to_mongo())

#Delete
# hera3.delete()

# Check whether document exist
# if service is not None:
#     # hera3.delete()
#     # print(service.name)
#     #to update
#     print(service.yob)
#     service.update(set__yob = 2005)
#     service.reload()
#     print(service.yob)
# else:
#     print("Service not found")

id_user = "5b374d500cc1752dccb66d60"
# user = User.objects().get(full_name = "Nathan Drake").to_mongo()
user = User.objects(full_name = "Nathan Drake").get().to_mongo()
password = user["pass_word"]

print(password)