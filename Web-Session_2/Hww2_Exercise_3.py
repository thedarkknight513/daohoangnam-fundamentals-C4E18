# delete by ID

import mlab
from models.service import Service
mlab.connect()

document_1 = Service.objects.get(id='5b2fb4460cc1751dace83d5a')
document_1.delete()