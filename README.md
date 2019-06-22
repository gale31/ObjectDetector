# ObjectDetector

ObjectDetector uses OpenCV Haar cascade classifiers to detect different objects in images and videos with Python. 

Firstly, I wrote two programs, which used the default haar cascade classifier for faces to find those in images and video. They are located in the return-face folder. Then I used a classifier for bananas from coding-robin and did the same, which can be found in return-banana. After that I repeated the process with a classifier for wallclocks from Celal Caoyn Elgun. The result can be found in, you guessed it, return-wallclock.

<img src= "imgur.com/a/8nyWp4K" width="600">

Above are results from a 24 second segment of the youtube video "How to Keep Bananas Fresh for Longer". The detected bananas were 3534, and about 35% of these were fake positives.

Then, I trained my own classifier for cars using the UIUC Image Database for car detection. It can be found in return-car. 

<img src= "https://s22.postimg.org/m2hz7fj9t/cars.png" width="600">

And, finally, I trained a classifier for cats in boxes using the ImageNet database (yes, they do have [this](http://www.image-net.org/synset?wnid=n02982515) synset). [Here](https://www.youtube.com/watch?v=FUmQihwrO1g) is a tutorial I did on how to download training images from there using Julia. Things about this can be found in the return-catbox folder.

<img src= "https://s22.postimg.org/uu24vdult/catsinboxes.png" width="600">

I did not train a classifier for cows.

