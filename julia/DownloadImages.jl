using Images

text = open("/Users/Gale/Documents/ObjectDetector/julia/synset/catboxsynset.txt")
lines = readlines(text)

count = 1
for imageurl in lines

	if imageurl == "\r\n"
		break
	end

	try
		name = string("/Users/Gale/Documents/ObjectDetector/julia/positive_julia/", string(count), ".jpg")

		source = imageurl[1:end-2]

		println(source)

		download(source, name)
		count += 1

		image = load(name)

		grayscaleimage = convert(Image{Images.Gray}, image)
		resizedimage = Images.imresize(grayscaleimage, (100, 100))
		
		imwrite(resizedimage, name)

	catch e
		println("caught an error $e")
        println("but we can continue with execution")
    end

end

#url = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04082710"