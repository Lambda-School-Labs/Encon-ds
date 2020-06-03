#Baseline classification with pretrained model ResNet50

import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions


def predict(img):
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  model = ResNet50( include_top=True, weights='imagenet', input_tensor=None, input_shape=None,
    pooling=None, classes=1000)
  features = model.predict(x)
  results = decode_predictions(features, top=4)[0]
  return {results}
