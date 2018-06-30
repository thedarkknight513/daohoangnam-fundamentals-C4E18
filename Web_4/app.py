from flask import Flask, render_template, redirect, url_for, request
from flask import *
import mlab
import mlab2hw
from models.service import Service 
from models.customer import Customer
from models.service import User
from models.service import Order
from mongoengine import *
from datetime import datetime

app = Flask(__name__)
app.secret_key ="a super super secret key"
mlab.connect()
mlab2hw.connect()

# Day object/document len database

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/search")
def search1():
   
    # day thong tin service len day. lay thong tin tu database
    # all_service = Service.objects(gender = gender) #lay ra document trong Service thoa man tieu chi
        all_service = Service.objects() #lay ra document trong Service thoa man tieu chi
        return render_template("search.html", all_service = all_service)
    
@app.route("/search/detail/<service_id>", methods = ["GET", "POST"])
def search_detail(service_id):
    if "loggedin" in session:
        service_detail = Service.objects().with_id(service_id)
        return render_template("search_detail.html", service_detail = service_detail)
    else:
        return redirect(url_for("log_in"))

@app.route("/search/<gender>")
def search2(gender):
    # day thong tin service len day. lay thong tin tu database
    # all_service = Service.objects(gender = gender, yob__lte =1998,address__icontains="Hanoi") #lay ra document trong Service thoa man tieu chi
    all_service = Service.objects(gender = gender) #lay ra document trong Service thoa man tieu chi
    return render_template("search.html", all_service = all_service)

@app.route("/customer")
def customer():
    all_customer = Customer.objects()
    return render_template("customer.html", all_customer = all_customer)
    # return all_customer[1]

@app.route("/customer2")
def customer_2():
    all_customer = Customer.objects(contracted = False)
    ten_customer = all_customer[0:10]
    return render_template("customer.html",ten_customer = ten_customer)

@app.route("/admin")
def admin():
    all_service = Service.objects()
    return render_template("admin.html", all_service = all_service)

@app.route("/admin/delete/<service_id>")
def delete(service_id):
    # return render_template("delete.html")
    service_to_delete = Service.objects().with_id(service_id) 
    if service_to_delete is None:
        return "Service not found"
    else:
        service_to_delete.delete()
        # return "deleted" + service_id
        return redirect(url_for("admin"))

@app.route("/admin/new_service", methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new_service.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]
        gender = form["gender"]
        if gender == "Nam":
            new_service_gender = 1
        else:
            new_service_gender = 0

        new_service = Service(
            name = name,
            yob = yob,
            phone = phone,
            gender = new_service_gender
        )
        new_service.save()

        return redirect(url_for("admin"))

@app.route("/admin/update/<service_id>", methods = ["GET", "POST"])
def update(service_id):
    service_update = Service.objects().with_id(service_id)
    name_default = service_update.name
    yob_default = service_update.yob
    phone_default = service_update.phone

    if request.method == "GET":
        return render_template("update.html", name_default = name_default, yob_default = yob_default, phone_default = phone_default)
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]
        service_update.update(set__name = name)
        service_update.update(set__yob = yob)
        service_update.update(set__phone = phone)
        service_update.reload()
        return redirect(url_for("admin"))

@app.route("/sign-in", methods = ["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("sign_in.html")
    elif request.method == "POST":
        form = request.form 
        user_name = form["user_name"]
        pass_word = form["pass_word"]
        email = form["email"]
        full_name = form["full_name"]

        new_user = User(
            user_name = user_name,
            pass_word = pass_word,
            email = email,
            full_name = full_name
        )

        new_user.save()
        return redirect(url_for("sign_in"))

@app.route("/log-in", methods = ["GET", "POST"])
def log_in():
    if request.method == "GET":
        return render_template("log_in.html")
    elif request.method == "POST":
        form = request.form 
        user_name = form["user_name"]
        pass_word = form["pass_word"]
        account_info = User.objects(user_name = user_name).get().to_mongo()
        correct_pass_word = account_info["pass_word"]
        if pass_word == correct_pass_word:
            session["loggedin"] = True
            session["user_name"] = user_name
            return redirect(url_for("search1"))
            # return "Welcome"
        else:
            return "Incorrect"

@app.route("/logout")
def log_out():
    del session["loggedin"]
    return redirect(url_for("index"))

@app.route("/order/<service_id>", methods = ["POST", "GET"])
def order(service_id):
    # if "loggedin" in session:
    service_id = service_id
    order_time = str(datetime.now())
    is_accepted = False
    user_id = session.get("user_name")

    new_order = Order(
        service_id = service_id,
        order_time = order_time,
        is_accepted = is_accepted,
        user_id= user_id
    )
    new_order.save()    
    return "Request sent"

if __name__ == '__main__':
    
    app.run(debug=True)   
 
