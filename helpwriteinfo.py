filename = '/Users/Gale/Documents/ObjectDetector/return-car/cars.txt'
target = open(filename, 'w')

for i in range(0, 499): 
    line = 'positive/pos-' + str(i) + '.pgm 1 0 0 100 40'
    target.write(line)
    target.write('\n')

target.close()