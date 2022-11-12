import os
import sys
 
# total arguments
apcliationNameSplited = keyAndValue = sys.argv[0].split("=")

secretFile = """
apiVersion: v1
kind: Secret
metadata:
  name: secrets-{0}
  uid: cfee02d6-c137-11e5-8d73-42010af00002
type: Opaque
data:""".format(apcliationNameSplited[1])

file_object = open('./env/secrets.yaml', 'a')
file_object.write(secretFile)

for name, value in sys.argv:
    keyAndValue = value.split("=")
    if keyAndValue[0].startswith("ST_") and keyAndValue[1] != 1:
        file_object.write("  {0}: {1}".format(keyAndValue[0].replace("ST_", ""), keyAndValue[1]))

file_object.close()
