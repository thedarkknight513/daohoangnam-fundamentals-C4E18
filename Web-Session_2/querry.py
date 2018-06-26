from models.service import Service
import mlab

mlab.connect()

all_service = Service.objects()  #kieu du lieu: list
first_service = all_service[0]
print(first_service)
print(first_service.to_mongo())  # nhin ro object. kieu du lieu: dictionary
print(first_service["name"]) 
print(first_service.name)
print(first_service.address)
