# python app.py
# set FLASK_APP=app.py

from flask import Flask, render_template, request, redirect
app = Flask(__name__) #name of module

@app.route("/")
def home():
    print("Visited Home Page")
    return render_template("home.html")

@app.route("/calculator")
def calculator():
    print("Visited Cal Page")
    # title= request.form["title"]
    # author= request.form["author"]
    return render_template("calculator.html")

@app.route("/calculator/output", methods=["POST"])
def cal_output():
    print("Visited Cal Output Page")
    device = request.form["device"] #<class 'str'>
    state = request.form["state"] #<class 'str'>
    hours = int(request.form["hours"]) #<class 'int'>
    days = int(request.form["days"]) #<class 'int'>
    x = {"device": device,"state": state,"hours": hours,"days": days}
    print(type(device))
    return x


if __name__ == "__main__":
    app.run(debug=True)

