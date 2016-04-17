import os

filename = '/Users/Gale/Documents/ObjectDetector/julia/bg.txt'
target = open(filename, 'w')

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths

    # Walk the tree
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_paths.append(filename)  # Add it to the list

    return file_paths  # Self-explanatory

path = get_filepaths('/Users/Gale/Documents/ObjectDetector/julia/negative')

print len(path)
for i in range(0, len(path)):
	print "path = ", path[i]
	line = '/Users/Gale/Documents/ObjectDetector/julia/negative/' + str(path[i])
	target.write(line)
	target.write('\n')

target.close()