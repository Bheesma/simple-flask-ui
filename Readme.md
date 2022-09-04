# Simple Flask UI

Simple Flask based UI for playing with Docker and Kubernetes.

## Run the app from local machine

* Execute the following commands:
```
cd src
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
flask run
```
* Browse http://localhost:8080

## Run the app from Docker container

* Build docker image and start the container
```
docker build -t flask-ui:1 .
docker run -p 8080:8080 -d flask-ui:1
```
* Browse http://localhost:8080


