# python resnet.py

import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import os
import pandas as pd 
from matplotlib import pyplot as plt 

path_app_info = os.path.join(os.getcwd(),"data/app_info.csv")
app_info = pd.read_csv(path_app_info)
resnet = ResNet50(weights='imagenet')

def res_model(file):
    img = load_img(file, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    plt.imshow(np.uint8(img[0]))
    img = preprocess_input(img.copy())
    predictions = resnet.predict(img)
    label = decode_predictions(predictions)
    res = str(label[0][0][1])
    detection = {str(label[0][0][1])}
    info = app_info.loc[app_info['appliances'] == res, 'tips']
    if info.empty:
      return {"not in our inventory take a better picture"}
    else:
      return {str(info)}
      




if __name__ == "__main__":
    img =  './static/uploads/best-refrigerators-1571069203.jpg' 
    print(res_model(img))