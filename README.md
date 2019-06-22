# ObjectDetector

ObjectDetector uses OpenCV Haar cascade classifiers to detect different objects in images and videos with Python. 

Firstly, I wrote two programs, which used the default haar cascade classifier for faces to find those in images and video. They are located in the return-face folder. Then I used a classifier for bananas from coding-robin and did the same, which can be found in return-banana. After that I repeated the process with a classifier for wallclocks from Celal Caoyn Elgun. The result can be found in, you guessed it, 'return-wallclock'.

<img src= "https://i.postimg.cc/zfZRvJt3/forever-1-up.png" width="600">

Above you can also see results from a 24 second segment of the youtube video "How to Keep Bananas Fresh for Longer". The detected bananas were 3534, and about 35% of these were fake positives.

Then, I trained my own classifier for cars using the UIUC Image Database for car detection. Find more in the folder 'return-car'. 

<img src= "https://i.postimg.cc/0NVx3nwx/forever-2-up.png" width="600">

Finally, I trained a classifier for cats in boxes using the ImageNet database (yes, they do have [this](http://www.image-net.org/synset?wnid=n02982515) synset). Find more in the 'return-catbox' folder.

<img src= "https://i.postimg.cc/zX4kwY2Y/forever-3uo.png" width="600">

This project was inteded simply as an exepriment and for fun.

