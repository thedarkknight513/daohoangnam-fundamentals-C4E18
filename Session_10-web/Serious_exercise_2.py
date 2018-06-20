# from flask import Flask

from flask import Flask
app = Flask(__name__)


@app.route('/user/<username>')
def user_name(username):
    # Users = { “quy”: { “name” : “Dinh Cong Quy”, “age” : 20}, “tuananh”: {“name” : “Huynh Tuan Anh”,“age” : 22}}
    user = { "quy": {"name": "Dinh Cong Quy", "age": 20}, "tuananh": {"name": "Huynh Tuan Anh", "age": 22}}

    if username == "quy":
        name = user[username]["name"]
        age = user[username]["age"]
        info = name + " "+ str(age)
    elif username == "tuananh":
        name = user[username]["name"]
        age = user[username]["age"]
        info = name + " "+ str(age)
    else:
        info = "User not found"
    
    return info


if __name__ == '__main__':
  app.run(debug=True)
 