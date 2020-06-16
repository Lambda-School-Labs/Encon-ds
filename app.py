# python app.py
# set FLASK_APP=app.py

# Imports
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from flask_cors import CORS
from cal import calculator
from resnet import res_model
from werkzeug.utils import secure_filename
import os

# Instantiate App
app = Flask(__name__)
CORS(app)

# Allowed file extentions
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



## ROUTES ##
#Home Route: displays list of devices
@app.route("/")
def home():
    print("Visited Home Page")
    print("------------------------------")
    return render_template("home.html")

#Calculator Route: displays calculator function in user friendly form
@app.route("/calculator")
def form():
    print("Visited Calculator Form Page")
    print("------------------------------")
    return render_template("calculator.html")

#Ouput Route: displays output from calculator form
@app.route("/calculator/output", methods=["POST", "GET"])
def cal_output():
    print("Visited Calculator Output Page")
    print("------------------------------")
    device = request.form["device"]
    state = request.form["state"] 
    hours = float(request.form["hours"]) 
    days = int(request.form["days"]) 
    x = {"device": device,"state": state,"hours": hours,"days": days}
    y = calculator(device,state,hours,days)
    return {"inputs": x, "outputs": y}

#API Route: Takes in FE request and returns json response
@app.route("/<device>/<state>/<hours>/<days>", methods=["POST", "GET"])
#Example: Ceiling Fan/Missouri/8/5
def cal(device,state,hours,days):
    print("Visited Calculator URL Page")
    print("------------------------------")
    device = device
    state = state
    hours = float(hours)
    days = int(days)
    y = calculator(device,state,hours,days)
    return jsonify(y)

#Upload Form Route: allows user to upload image
@app.route('/upload')
def upload_form():
	return render_template("upload.html")

#Upload Prediction Route: runs image through model and returns prediction
@app.route('/upload', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return render_template('upload.html', filename=filename, result=res_model('./static/uploads/'+filename))
	else:
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

    


if __name__ == "__main__":
    app.run(debug=True)
    # print(calculator("Ceiling Fan","Missouri",8,5))

