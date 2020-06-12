import numpy as np
# import keras
# from keras.applications import resnet50
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from flask import jsonify
from matplotlib import pyplot as plt 
import pandas as pd
import os

# Data files
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
    detection = {str(label[0][0][-2:])}
    info = app_info.loc[app_info['appliances'] == res, 'tips']
    info = {str(info)}

    return detection, info

# if __name__ == "__main__":
#     im23 =  './static/washer_644.jpg' 
#     print(res_model(im23))