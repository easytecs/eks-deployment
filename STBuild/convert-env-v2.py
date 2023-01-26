import sys
import re 
import json
 
apcliationNameSplited =  sys.argv[1].split("=")
serviceNameSplited =  sys.argv[2].split("=")

secretFile = """
apiVersion: v1
kind: ConfigMap
metadata:
  name: env-{0}
  namespace: {1}
data:
  IS_ST: "YES"
""".format(apcliationNameSplited[1], serviceNameSplited[1])

file_object = open('./deployment/config-map.yaml', 'a')
file_object.write(secretFile)

envJson = sys.argv[3].split("=")
print(envJson)
env = json.loads(envJson[1])

for key, val in env.items():
  file_object.write('\n  {0}: "{1}"'.format(key, val))

file_object.close()
