# TestTaskFaifly

##  Final.py - application itself. To run it: 
1.  Open console.
2.  Type **python Final.py**
3.  Wait till you see the message, and then either type path to image, or type "quit" to stop app running.

### PreparationWork.ipynb - Notebook with some of the work I did, some test, and also you can use it to generate some test data.

### images - folder with sample images.
### GeneratedTestImages - folder with images I created to test a bit my app.

### model_weights_50epochs.h5 - pretrained weight for tf keras model. I did all the trainings on kaggle kernel to train model faster.


* P.S. The app idea is based on the fact that it takes as input images like you send me, so that I just separate each image on several images, depending on their lenght, and than I feed each splitted image to the model. So that means, as long as you will feed this app with images like ones, that you sent me, it will work, but for example if image size won't be like (28, number_of_digits_on_the_image·28), or (number_of_digits_on_the_image·28, 28), it won't work. 
  * Also I want to add that as model was trained on MNIST dataset(handwritten digits), it is not as perfect on images you sent me(because the are more like printed digits), but nevertheless it does pretty good accuracy. 
  * And finally, this app doesn't take into account that, for example, all four images will me placed in first half of image, and ther rest will be empty. I did that way cause all sample images were like several several 1-digit images stacked together, so I assume for this task it is enough. But if it is not, I can do so that it will for any kind of image by separating task into 1) digit detection, 2) dectected areas classification.
* P.S.P.S. And of course thank you for opportunity!

