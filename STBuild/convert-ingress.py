import sys
import json

def formatArgs ():
  argsObject = {}
  for key, value in enumerate(sys.argv):
    if key < 1:
      continue

    keyAndValue = value.split("=")
    argsObject[keyAndValue[0]] = keyAndValue[1]

  return argsObject

argsObject = formatArgs()

apiMapping = open('./api-mapping/api.json')

paths = ""

for value in json.load(apiMapping)["endpoints"]:
  paths = paths + """
      - path: {2}
        pathType: ImplementationSpecific
        backend:
          service:
            name: {0}
            port:
              number: {1}
  """.format(
    argsObject["APPLICATION_NAME"],
    argsObject["APPLICATION_PORT"],
    value
  )

print(paths)

ingressFile = """
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {0}
  namespace: st-application
spec:
  ingressClassName: kong
  rules:
  - http:
      paths:
{1}
""".format(
  argsObject["APPLICATION_NAME"],
  paths
)

file_object = open('./deployment/ingress.yaml', 'a')
file_object.write(ingressFile)
file_object.close()
