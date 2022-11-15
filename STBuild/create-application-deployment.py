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

# Service using ingress
service = """
---
apiVersion: v1
kind: Service
metadata:
  name: {0}
  namespace: st-application
spec:
  ports:
  - port: {1}
    protocol: TCP
  type: LoadBalancer
  selector:
    app: {0}
""".format(
  argsObject['APPLICATION_NAME'],
  argsObject['APPLICATION_PORT']  
)

# Service using nbl
if 'NBL_NAME' in argsObject and argsObject['NBL_NAME'] != "":
  service = """
---
apiVersion: v1
kind: Service
metadata:
  name: {0}
  namespace: {3}
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
    service.beta.kubernetes.io/aws-load-balancer-internal: "true"
    service.beta.kubernetes.io/aws-load-balancer-name: {2}
spec:
  ports:
  - port: {1}
    protocol: TCP
  type: LoadBalancer
  selector:
    app: {0}
  """.format(
    argsObject['APPLICATION_NAME'],
    argsObject['APPLICATION_PORT'],
    argsObject['NBL_NAME'],
    argsObject['SERVICE_NAMESPACE']
  )


applicationFile = """
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {0}
  namespace: {3}
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
{5}
""".format(
  argsObject['APPLICATION_NAME'],        # 0 application_name
  argsObject['DEPLOYMENT_IMAGE'],        # 1 deployment_image
  argsObject['APPLICATION_PORT'],        # 2 application_port
  argsObject['SERVICE_NAMESPACE'],       # 3 namespace
  argsObject['APPLICATION_PATH_HEALTH'], # 4 health_path
  service                                # 5 service
)

file_object = open('./deployment/application.yaml', 'a')
file_object.write(applicationFile)

file_object.close()
