import os

import numpy as np
import tensorflow as tf

from PIL import Image

from django.conf import settings

from keras.preprocessing import image
from keras.models import load_model

class Classifier:
    IMG_SIZE = (32, 32)

    LABELS = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    def __init__(self, image):
        self.image = image

    def classify(self):
        resized_img = self.image.resize(self.IMG_SIZE, Image.ANTIALIAS)
        img_array   = image.img_to_array(resized_img)

        data = np.expand_dims(img_array, axis = 0)

        file  = os.path.join(settings.BASE_DIR, 'model/model.h5')
        model = load_model(file)
        
        prediction  = model.predict(data)
        label_index = np.argmax(prediction, axis = 1)[0]

        return self.LABELS[label_index]

    pass