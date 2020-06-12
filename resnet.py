# python resnet.py

import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import os
import pandas as pd 

path_app_info = os.path.join(os.getcwd(),"data/app_info.csv")
app_info = pd.read_csv(path_app_info)
model = ResNet50(weights='imagenet')

def res_model(file):
    image = load_img(file, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    pred = model.predict(image)
    label = decode_predictions(pred)
    res = str(label[0][0][1])
    detection = {str(label[0][0][-2:])}
    info = app_info.loc[app_info['appliances'] == res, 'tips']
    info = {str(info)}

    return detection, info


# if __name__ == "__main__":
#     img =  './static/uploads/1658.jpg' 
#     print(res_model(img))