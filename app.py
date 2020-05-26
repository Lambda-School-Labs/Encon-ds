# python app.py
# set FLASK_APP=app.py

# Imports
from flask import Flask, render_template, request, jsonify, redirect
from cal import calculator
from flask_cors import CORS

# Instantiate App
app = Flask(__name__) #name of module
CORS(app)

# Routes
@app.route("/")
def home():
    print("Visited Home Page")
    print("------------------------------")
    return render_template("home.html")

@app.route("/calculator")
def form():
    print("Visited Calculator Form Page")
    print("------------------------------")
    return render_template("calculator.html")

@app.route("/calculator/output", methods=["POST", "GET"])
def cal_output():
    print("Visited Calculator Output Page")
    print("------------------------------")
    device = request.form["device"] #<class 'str'>
    state = request.form["state"] #<class 'str'>
    hours = float(request.form["hours"]) #<class 'int'>
    days = int(request.form["days"]) #<class 'int'>
    x = {"device": device,"state": state,"hours": hours,"days": days}
    y = calculator(device,state,hours,days)
    return {"inputs": x, "outputs": y}

@app.route("/<device>/<state>/<hours>/<days>", methods=["POST", "GET"])
# Ceiling Fan/Missouri/8/5
def cal(device,state,hours,days):
    print("Visited Calculator URL Page")
    print("------------------------------")
    device = device
    state = state
    hours = float(hours)
    days = float(days)
    x = {"device": device,"state": state,"hours": hours,"days": days}
    y = calculator(device,state,hours,days)
    return jsonify(y)



if __name__ == "__main__":
    app.run(debug=True)
    print(calculator("Ceiling Fan","Missouri",8,5))

