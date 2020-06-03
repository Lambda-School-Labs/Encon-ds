# python app.py
# set FLASK_APP=app.py

# Imports
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
from cal import calculator
from classification import predict
from flask_cors import CORS
from werkzeug.utils import secure_filename
from resnet import res_model, im23
import os

# Instantiate App
# upload_file = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# path = os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)
UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['upload_file'] = upload_file #name of module
CORS(app)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

	
@app.route('/upload')
def upload_form():
	return render_template('upload.html')

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
		#print('upload_image filename: ' + filename)
		# flash('Image successfully uploaded and displayed')
		return render_template('upload.html', filename=filename, result=res_model('./static/uploads/'+filename))
	else:
		# flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

    




if __name__ == "__main__":
    app.run(debug=True)
    # print(calculator("Ceiling Fan","Missouri",8,5))

