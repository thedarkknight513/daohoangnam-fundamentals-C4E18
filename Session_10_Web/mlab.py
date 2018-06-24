import mongoengine

# mongodb://dhnam1993:dhnam1993@ds217351.mlab.com:17351/muadongkhonglanh-c4e18

host = "ds217351.mlab.com"
port = 17351
db_name = "muadongkhonglanh-c4e18"
user_name = "dhnam1993"
password = "dhnam1993"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())