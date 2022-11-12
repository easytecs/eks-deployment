import os

secretFile = """
apiVersion: v1
kind: Secret
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: { ... }
  name: secrets-{0}
  resourceVersion: "164619"
  uid: cfee02d6-c137-11e5-8d73-42010af00002
type: Opaque
data:""".format(os.getenv('APPLICATION_NAME'))

file_object = open('./secrets.yaml', 'a')
file_object.write(secretFile)

for name, value in os.environ.items():
    if name.startswith("ST_"):
        file_object.write("  {0}: {1}".format(name.replace("ST_", ""), value))

file_object.close()
