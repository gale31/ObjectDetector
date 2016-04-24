import sys
sys.path.append("/Users/Gale/.virtualenvs/cv/lib/python2.7/site-packages")

import cv2

# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# Create the haar cascade
catboxCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect catboxs in the image
catboxs = catboxCascade.detectMultiScale(
    gray,
    scaleFactor=1.24,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print "Found {0} cats in boxes!".format(len(catboxs))

"""
newpath = r'Documents\ObjectDetector\return-catbox\found-catboxs'
if not os.path.exists(newpath):
    os.makedirs(newpath)
"""
# Draw a rectangle around the catboxs
i = 1
for (x, y, w, h) in catboxs:
    imgcrop = image[y:(y+h), x:(x+w)]
    cv2.imwrite("/Users/Gale/Documents/ObjectDetector/return-catbox/found-catboxs/catbox" + str(i) + ".jpg", imgcrop)
    i = i + 1
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.namedWindow('catboxs found', cv2.WINDOW_NORMAL)
image2 = cv2.resize(image, (1000, 550))
cv2.imshow("output", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
