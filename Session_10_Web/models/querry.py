from models.service import Service
import mlab




id_to_find = "5b2f25530cc175087c6052c3"

# hera = Service.objects().get(id = id_to_find)
# hera = Service.objects(id = id_to_find)
# print(hera[0])

service = Service.objects().with_id(id_to_find)
print(hera.to_mongo())


if service is not None:
    # service.delete()
    # print("deleted")
    print(service.yob)
    service.update(set__yob= 2005)
    service.reload() # cap nhat thong tin ve bien o duoi may
    print(service.yob)
else:
    print("service not found")

