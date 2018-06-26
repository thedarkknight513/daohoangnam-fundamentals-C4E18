import mongoengine

host = "ds117691.mlab.com"
port = 17691
db_name = "c4e18-customer"
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