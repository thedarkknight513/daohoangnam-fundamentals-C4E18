#Find by ID

import mlab
from models.service import Service
mlab.connect()

document_1 = Service.objects.get(id='5b2fad8c0cc1751600df7a6c')
print(document_1.to_mongo())



