import sys
sys.path.append("/Users/Gale/.virtualenvs/cv/lib/python2.7/site-packages")

import cv2
import numpy as np
from six.moves import urllib
import os

import socket
socket.setdefaulttimeout(5)

def StoreInitialImages():
    PositiveImagesLink = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04082710'
    PositiveImageURLs = urllib.request.urlopen(PositiveImagesLink).read().decode(encoding = 'UTF-8',errors = 'strict')

    path = '/Users/Gale/Documents/ObjectDetector/return-cat_in_a_box/Negative/'
    if not os.path.exists(path):
        os.makedirs(path)

    count = 1045
        
    for i in PositiveImageURLs.split('\n'):
        try:
            print(i)
            path2 = path + str(count) + '.jpg'
            urllib.request.urlretrieve(i, path2)
            image = cv2.imread(path2)
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            resizedImage = cv2.resize(grayImage, (100, 100))
            cv2.imwrite(path2, resizedImage)
        except Exception as e:
            print(str(e))
        count = count + 1

	#PositiveImagesLink = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02982515'
    #NegativeImagesLink = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03579538'
    #NegativeImagesLink = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04082710'

StoreInitialImages()

print("Done!")