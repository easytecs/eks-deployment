import sys
import json
 
secretFile = "CI=false"
file_object = open('./deployment/.env.production.local', 'a')
file_object.write(secretFile)

envJson = sys.argv[1].split("=")
print("here 1", envJson)
env = json.loads(envJson[1])
print"here 2", (env)


for key, val in env.items():
  file_object.write('\n{0}={1}'.format(key, val))

file_object.close()
