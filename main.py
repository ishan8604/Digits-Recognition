import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras._tf_keras.keras.models import load_model

model =load_model('handwritten.keras')

image_number = 1
while os.path.isfile(f"digits/digit{image_number}.png"):
    try:
        img = cv2.imread(f"digits/digit{image_number}.png")[:, :, 0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"This digit is probably a {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()

    except:
        print("Error")
    finally:
        image_number += 1