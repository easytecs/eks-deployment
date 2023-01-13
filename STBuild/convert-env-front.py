import sys
 
secretFile = "CI=false"
file_object = open('./deployment/.env.production.local', 'a')
file_object.write(secretFile)

for key, value in enumerate(sys.argv):
    if key < 1:
      continue
    
    print(key)
    print(value)
    
    file_object.write('\n{0}'.format(value))

file_object.close()
