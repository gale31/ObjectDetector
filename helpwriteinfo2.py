filename = '/Users/Gale/Documents/ObjectDetector/return-car/bg.txt'
target = open(filename, 'w')

for i in range(0, 500): 
    line = '/Users/Gale/Documents/ObjectDetector/return-car/negative/neg-' + str(i) + '.pgm'
    target.write(line)
    target.write('\n')

target.close()