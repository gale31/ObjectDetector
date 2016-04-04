import sys
sys.path.append("/Users/Gale/.virtualenvs/cv/lib/python2.7/site-packages")

import cv2

videoPath = sys.argv[1]
cascPath = sys.argv[2]

video_object = cv2.VideoCapture(videoPath)
wallclockCascade = cv2.CascadeClassifier(cascPath)

i = 1
j = 1

success = True
while success:
    success,frame = video_object.read()
    if success:
        pathw = "/Users/Gale/Documents/ObjectDetector/return-wallclock/shots/tmpcadur.bmp"
        cv2.imwrite(pathw, frame)
        i = i + 1
        imagePath = pathw;
        
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        wallclocks = wallclockCascade.detectMultiScale(
            gray,
            scaleFactor=1.24,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
            
        print "Found {0} wallclocks!".format(len(wallclocks))
                                             
        for (x, y, w, h) in wallclocks:
            imgcrop = image[y:(y+h), x:(x+w)]
            cv2.imwrite("/Users/Gale/Documents/ObjectDetector/return-wallclock/found-wallclocks/wallclock" + str(j) + ".jpg", imgcrop)
            j = j + 1

print("Done!")