using Images

image = load("/Users/Gale/Documents/ObjectDetector/julia/positive_julia/5.jpg")

grayscaleimage = convert(Image{Images.Gray}, image)

resizeimage = Images.imresize(grayscaleimage, (100, 100))

imwrite(resizeimage, "/Users/Gale/Documents/ObjectDetector/julia/positive_julia/1.jpg")