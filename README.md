# Digits Recognition 

##  Final.py - application itself. To run it: 
1.  Open console.
2.  Type **python Final.py**
3.  Wait till you see the message, and then either type path to image, or type "quit" to stop app running.

### DataAugmentationAttempt.ipynb - Notebook with main work I did, you can fin there my new approach for this promleb, model training, and model estimation.


### images - folder with sample images.

### model_weights_2attempt.h5 - pretrained weight for tf keras model. 


* P.S. Ok, so this time I've changed my strategy. I had 3 ideas to work out. 
  1. 1st one was to find some more suitable dataset, with typed digits, or something. I did found SVHN dataset, and tried to train model, but it wasn't very succesful. 
  2. Another idea was to use OCR, but I wasn't familiar at all with this technique, so I decided to pass it till I will have no choice.
  3. Final idea was to use ImageDataGenerators for Data Augmentation(to increase amount of training examples). I had only 10 example images, 4 digits each. So that I cropped those images into 40 1-digit images, and applied ImageDataGenerator to them, an made something like 10000 images. I think it will work out perfect for this problem, as long as I assume that other images(in your test set) are similar to those ones you've send me(they are of standard shape).
* P.S.P.S. And thank you a lot for the 2nd opportunity! I hope this time I did better:)

