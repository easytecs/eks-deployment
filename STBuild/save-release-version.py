import sys
 
file_object = open('./release-version/release.txt', 'a')
file_object.write(sys.argv[1])

file_object.close()
