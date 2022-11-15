import sys

def formatArgs ():
  argsObject = {}
  for key, value in enumerate(sys.argv):
    if key < 1:
      continue

    keyAndValue = value.split("=")
    argsObject[keyAndValue[0]] = keyAndValue[1]

  return argsObject


argsObject = formatArgs()

args = ""
if argsObject["APPLICATION_ARGS"] != "":
  args = """
        args: ["{0}"]
  """.format('","'.join(argsObject["APPLICATION_ARGS"].split(",")))

applicationFile = """
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {0}
  namespace: st-service
spec:
  selector:
    matchLabels:
      app: {0}
  replicas: 1
  template:
    metadata:
      labels:
        app: {0}
    spec:
      containers:
      - image: {1}
        name: {0}
{5}
        ports:
        - containerPort: {2}
        livenessProbe:
          failureThreshold: 3
          httpGet:
            path: {4}
            port: {2}
            scheme: HTTP
          initialDelaySeconds: 15
          periodSeconds: 7
          successThreshold: 1
          timeoutSeconds: 2
        readinessProbe:
          failureThreshold: 3
          httpGet:
            path: {4}
            port: {2}
            scheme: HTTP
          initialDelaySeconds: 15
          periodSeconds: 7
          successThreshold: 1
          timeoutSeconds: 2
        envFrom:
         - configMapRef:
            name: env-{0}
      imagePullSecrets:
       - name: regcred
---
apiVersion: v1
kind: Service
metadata:
  name: {0}
  namespace: st-service
spec:
  ports:
  - port: {2}
    protocol: TCP
  type: ClusterIP
  selector:
    app: {0}
""".format(
  argsObject["APPLICATION_NAME"], # 0 application_name
  argsObject["DEPLOYMENT_IMAGE"], # 1 deployment_image
  argsObject["APPLICATION_PORT"], # 2 application_port
  argsObject["NBL_NAME"], # 3 nbl_namne
  argsObject["APPLICATION_PATH_HEALTH"], # 4 path_health
  args  # 5 args
)

file_object = open('./deployment/application.yaml', 'a')
file_object.write(applicationFile)

file_object.close()
