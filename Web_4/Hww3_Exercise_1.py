# Remove ALL documents in your Service Collection

from models.service import Service
import mlab

mlab.connect()

service = Service.objects()
service.delete()
