# python resnet.py

import os
import numpy as np
import pandas as pd 
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

# Data files
path_states = os.path.join(os.getcwd(),"data/app_info.csv")


appliances = ['dishwasher', 'washer', 'notebook', 'television', 
              'desktop computer', 'vacuum', 'microvawe', 'refrigerator', 
              'hair blower', 'iron', 'electric fan', 'toaster', 'space heater']

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
      return app_info.loc[app_info['appliances'] == data["label"], 'tips'].item()
    else:
      return "Image is not a common household appliance. Please select a different picture."


if __name__ == "__main__":
    img =  './static/uploads/image.png' 
    print(res_model(img))