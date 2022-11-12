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
    # service.beta.kubernetes.io/security-groups: sg-0792960602de09f5c,sg-001c5b81c9023e47a,sg-0cf81eafa1428cb4c,sg-04d090c64a87e950e,sg-0ff683dedc1a9c596
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
