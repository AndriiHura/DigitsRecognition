import pandas as pd
import numpy as np

np.random.seed(42)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.models import load_model
from PIL import Image
from IPython.display import display

# To ignore warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'




def split_image(image_array, num_of_digits):
    """Function splits the whole image into several images - 1 image for each digit
       Takes: image_array - (1, 28, 28*num_of_digits, 1)
       returns (num_of_images, 28, 28, 1) array"""
    
    new_array = image_array.copy().reshape(num_of_digits, 28, 28, 1)
    for im in range(num_of_digits):
        new_array[im][:,:,0] = image_array[0][:,28*im:28*(im+1), 0]# separating imput image into N images
    return new_array

def predict_full_image(image_path):
    """Function predicts all numbers on input image, in order from left to right"""
    
    # Openning image
    input_image = Image.open(image_path)
    # Converting it into numpy array, each value is in range (0, 255)
    image_array = np.array(input_image, dtype = 'float32')
    # Normalizing image
    image_array = image_array / 255.
    image_shape = image_array.shape
    if(image_shape[0] > image_shape[1]): # Image is looks like column of numbers
        image_array = np.rot90(image_array)
        image_shape = image_array.shape
    # Reshaping from (28, 28*num_digits) to (1, 28, 28*num_digits,1)
    image_array = image_array.reshape(1, 28, image_shape[1],1)
    num_of_digits = image_shape[1] // 28
    # Reshaping from (1,28, 28*num_digits,1) to (num_digits, 28, 28,1)
    splitted_images = split_image(image_array, num_of_digits)
    # Predicting result
    answer = model.predict_classes(splitted_images)
    answer = "".join(str(x) for x in answer)
    return(answer)


# Defining the model
model = Sequential()

model.add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', 
                 activation ='relu', input_shape = (28,28,1)))
model.add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', 
                 activation ='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))


model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', 
                 activation ='relu'))
model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', 
                 activation ='relu'))
model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
model.add(Dropout(0.25))


model.add(Flatten())
model.add(Dense(256, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation = "softmax"))


# Loading pretrained weights
model.load_weights("model_weights_50epochs.h5")


input_data = 0
while True:
    input_data = input("Enter path to file. \nIf you want to quit enter 'quit':\t")
    if(input_data == "quit"):
        break
    print(predict_full_image(input_data), "\n")







