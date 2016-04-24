import sys
sys.path.append("/Users/Gale/.virtualenvs/cv/lib/python2.7/site-packages")

import cv2

videoPath = sys.argv[1]
cascPath = sys.argv[2]

video_object = cv2.VideoCapture(videoPath)
catboxCascade = cv2.CascadeClassifier(cascPath)

j = 1
success = True
while success:
    success,frame = video_object.read()
    if success:
        pathw = "/Users/Gale/Documents/ObjectDetector/return-catbox/tmpcadur.bmp"
        cv2.imwrite(pathw,frame)
        imagePath = pathw;
        
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        catboxs = catboxCascade.detectMultiScale(
            gray,
            scaleFactor=1.24,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        
        print "Found {0} cats in boxes!".format(len(catboxs))
        
        for (x, y, w, h) in catboxs:
            imgcrop = image[y:(y+h), x:(x+w)]
            cv2.imwrite("/Users/Gale/Documents/ObjectDetector/return-catbox/found-catboxs/catbox" + str(j) + ".jpg", imgcrop)
            j = j + 1
            
print("Done!")
