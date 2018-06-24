from flask import Flask, render_template
import mlab 
from models.service import Service
# from mongoengine import *
app = Flask(__name__)

#0. Create connection
mlab.connect()

new_service = Service(
    name = "Dat 100",
    dob = 1996,
    gender = 1,
    height = 174,
    phone = "012345887900",
    address = "Tran Duy Hung",
    status = False
)
new_service.save()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template("index.html", all_service = all_service)
    # return render_template("admin.html")


if __name__ == '__main__':
  app.run(debug=True)
 