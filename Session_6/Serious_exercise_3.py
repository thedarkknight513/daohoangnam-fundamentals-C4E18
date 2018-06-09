from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client= MongoClient(mongo_uri)
db = client.get_default_database()
posts = db["posts"]

# collection = db.posts

new_content  = {
    "title": "Suy ngẫm :-?",
    "author": "Đào Hoàng Nam C4E18",
    "content": " Nếu không cố gắng bạn sẽ không biết mình vô dụng đến mức nào"
}  

posts.insert_one(new_content)

