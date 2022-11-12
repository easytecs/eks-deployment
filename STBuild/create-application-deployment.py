import sys
 
applicationFile = """
---
apiVersion: v1
kind: Namespace
metadata:
  name: st_service
  
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {0}
  namespace: st_service
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
          path: /health
          port: {3}
          scheme: HTTP
        initialDelaySeconds: 15
        periodSeconds: 7
        successThreshold: 1
        timeoutSeconds: 2
      readinessProbe:
        failureThreshold: 3
        httpGet:
          path: /health
          port: {3}
          scheme: HTTP
        initialDelaySeconds: 15
        periodSeconds: 7
        successThreshold: 1
        timeoutSeconds: 2
      envFrom:
       - configMapRef:
         name: env-{0}
---
apiVersion: v1
kind: Service
metadata:
  name: {0}
  namespace: st_service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
    service.beta.kubernetes.io/aws-load-balancer-internal: "true"
    service.beta.kubernetes.io/aws-load-balancer-name: {3}
spec:
  ports:
  - port: {2}
    protocol: TCP
  type: LoadBalancer
  selector:
    app: {0}
""".format(
  sys.argv[1], # application_name
  sys.argv[2], # deployment_image
  sys.argv[3], # application_port
  sys.argv[4]  # nbl_namne
)

file_object = open('./deployment/application.yaml', 'a')
file_object.write(applicationFile)

file_object.close()
