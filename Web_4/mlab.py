import mongoengine

host = "ds121341.mlab.com"
port = 21341
db_name = "c4e18-web4"
user_name = "namdh1993"
password = "namdh1993"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())