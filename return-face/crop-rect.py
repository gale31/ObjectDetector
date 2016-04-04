import sys
from PIL import Image

imgpath = sys.argv[1]
x = sys.argv[2]
y = sys.argv[3]
w = sys.argv[4]
h = sys.argv[5]

img = Image.open(imgpath)

imgcrop = img.crop((int(x), int(y), (int(x)+int(w)), (int(y)+int(h))))
imgcrop.save('Desktop/imgcrop.jpg')
