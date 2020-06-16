# python resnet.py

import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions


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
    return data


if __name__ == "__main__":
    img =  './static/uploads/1658.jpg' 
    print(res_model(img))