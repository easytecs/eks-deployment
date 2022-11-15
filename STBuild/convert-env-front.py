import sys
 
apcliationNameSplited =  sys.argv[1].split("=")
serviceNameSplited =  sys.argv[2].split("=")

secretFile = "CI=false"
file_object = open('./deployment/.env.production.local', 'a')
file_object.write(secretFile)

for key, value in enumerate(sys.argv):
    if key <= 2:
      continue

    file_object.write('\n{0}'.format(value))

file_object.close()
