import sys
sys.path.append("/Users/Gale/.virtualenvs/cv/lib/python2.7/site-packages")

import cv2

import plotly.plotly as py
py.sign_in('gale_st','i2wp2o4poq')

import plotly.graph_objs as go

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
        i = i + 1
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
        
        print "Found {0} faces!".format(len(faces))
        
        resx.append(i)
        resy.append(len(faces))
        
        for (x, y, w, h) in faces:
            imgcrop = image[y:(y+h), x:(x+w)]
            cv2.imwrite("/Users/Gale/Documents/ObjectDetector/return-face/found-faces/face" + str(j) + ".jpg", imgcrop)
            j = j + 1

trace = go.Scatter(
                   x = resx,
                   y = resy,
                   name = 'faces'
                   )
data = [trace]
py.plot(data, filename='faces-line-mode')
py.image.save_as(data, 'video-faces-data.png')
print("Done!")
