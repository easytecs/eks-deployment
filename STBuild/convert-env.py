import sys
 
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

for key, value in enumerate(sys.argv):
    if key <= 2:
      continue

    keyAndValue = value.split("=")
    if keyAndValue[0].startswith("ST_") and keyAndValue[1] != "":
        print(keyAndValue[1])
        file_object.write('\n  {0}: "{1}"'.format(keyAndValue[0].removeprefix("ST_"), keyAndValue[1]))

file_object.close()
