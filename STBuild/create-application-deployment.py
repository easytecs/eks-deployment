import sys
 
applicationFile = """
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {0}
  namespace: st-application
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
            port: {2}
            scheme: HTTP
          initialDelaySeconds: 15
          periodSeconds: 7
          successThreshold: 1
          timeoutSeconds: 2
        readinessProbe:
          failureThreshold: 3
          httpGet:
            path: /health
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
  namespace: st-application
spec:
  ports:
  - port: {2}
    protocol: TCP
  type: LoadBalancer
  selector:
    app: {0}
""".format(
  sys.argv[1], # 0 application_name
  sys.argv[2], # 1 deployment_image
  sys.argv[3], # 2 application_port
  sys.argv[4]  # 3 nbl_namne
)

file_object = open('./deployment/application.yaml', 'a')
file_object.write(applicationFile)

file_object.close()
