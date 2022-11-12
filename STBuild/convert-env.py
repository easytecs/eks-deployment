import sys
 
apcliationNameSplited =  sys.argv[1].split("=")

secretFile = """
apiVersion: v1
kind: ConfigMap
metadata:
  name: env-{0}
  namespace: st-service
data:""".format(apcliationNameSplited[1])

file_object = open('./deployment/config-map.yaml', 'a')
file_object.write(secretFile)

for key, value in enumerate(sys.argv):
    if key <= 1:
      continue

    keyAndValue = value.split("=")
    if keyAndValue[0].startswith("ST_") and keyAndValue[1] != "1":
        file_object.write("\n  {0}: {1}".format(keyAndValue[0].replace("ST_", ""), keyAndValue[1]))

file_object.close()
