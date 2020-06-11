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
# import matplotlib.pyplot as plt
# %matplotlib inline

# resnet_model = resnet50.ResNet50(weights='imagenet')
resnet = ResNet50(weights='imagenet')

def res_model(file):
    original = load_img(file, target_size=(224, 224))
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    plt.imshow(np.uint8(image_batch[0]))
    processed_image = preprocess_input(image_batch.copy())
    predictions = resnet.predict(processed_image)
  
    label = decode_predictions(predictions)
    res = {str(label[0][0][1])}
    return res

# im23 =  './static/uploads/washer_644.jpg' 



if __name__ == "__main__":
    im23 =  './static/uploads/washer_644.jpg' 
    print(res_model(im23))