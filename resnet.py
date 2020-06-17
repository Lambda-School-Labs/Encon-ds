# python resnet.py

import os
import numpy as np
import pandas as pd 
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

# Data file
path_app_info = os.path.join(os.getcwd(),"data/app_info.csv")
app_info = pd.read_csv(path_app_info)

# List of appliances classes Resnet model recognizes
appliances = ['dishwasher', 'washer', 'notebook', 'television', 
'desktop_computer', 'vacuum', 'microwave', 'refrigerator', 
'hand_blower', 'iron', 'electric_fan', 'toaster', 'space_heater', 
'home_theater', 'entertainment_center', 'monitor']

model = ResNet50(weights='imagenet')
def res_model(file):
    image = load_img(file, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    pred = model.predict(image)
    results = decode_predictions(pred)
    imageID, label, prob = results[0][0]
    data = {"label": label, "probability": np.float64(prob)}
    if data["label"] in appliances:
      return data["label"], app_info.loc[app_info['appliances'] == data["label"], 'tips'].item()
    else:
      return data["label"], "Image is not a common household appliance. Please select a different picture."


if __name__ == "__main__":
    img =  './static/uploads/image.png' 
    print(res_model(img))