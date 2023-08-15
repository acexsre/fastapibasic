# fastapibasic
Basic FastAPI example app with Dockerfile. [For Quick Testing and R&amp;D] 

# How to use with K8S
- Add the deployment (It is a public image) 
```
cd deploy
kubectl create deploy backend --image=ayushl33t/samplefastapi:latest --port=80  --dry-run=client -o yaml > deployment.yml
kubectl apply -f deployment.yml
```

- Add the service
```
kubectl expose deployment backend --type="NodePort" --target-port=80 --dry-run=client -o yaml > service.yml
kubectl apply -f service.yml
minikube service backend
```

- To enable ingress: 
```
minikube addons enable ingress
```
