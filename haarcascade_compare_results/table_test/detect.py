import sys
sys.path.append("/Users/Gale/.virtualenvs/cv/lib/python2.7/site-packages")

import cv2

import time
start_time = time.time()

videoPath = sys.argv[1]
cascPath = sys.argv[2]

video_object = cv2.VideoCapture(videoPath)
faceCascade = cv2.CascadeClassifier(cascPath)

i = 1
j = 1

resx = []
resy = []
success = True
while success:
    success,frame = video_object.read()
    if success:
        pathw = "/Users/Gale/Documents/ObjectDetector/return-face/shots/cadur_" + str(i) + ".bmp"
        cv2.imwrite(pathw,frame)
        imagePath = pathw;
        
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.24,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        
        print "Found {0} objects!".format(len(faces))


print("--- %s seconds ---" % (time.time() - start_time))

print("Done!")
