# pyapitest

- This is a basic example of a restful api created with python and Flask. 
   - [app.py](app.py)   
- The application is then Dockerized 
   - [Dockerfile](Dockerfile)  
   - A prebuilt image is made avalible on Docker Hub: 
     - [https://hub.docker.com/r/gtechnology/pyapi](https://hub.docker.com/r/gtechnology/pyapi)  
- Finally a basic manifest is provided to run the applicaiton with Kubernetes. 
   - [front_deploy.yml](front_deploy.yml)  

---
### API Usage
Since everyone loves a good dad joke, this api example uses the [icanhazdadjoke.com](https://icanhazdadjoke.com/api) public api for the source data.
All requests are returned as json and there are 3 avalible endpoints to query. 
```
'/' will redirect to '/dadjoke'
'/dadjoke' will return a random dad joke 
```
``` 
/search/{search term} will search for existing dad jokes that contain the given search term 
```
``` 
/j/{joke id} will return a specfic dad joke with the provided id 
```

---
### Starting App
This applicaiton can be run in any of the 3 forms that are provided with a few notes for each method.  

---
#### **app.py**
```
Clone this repo
  git clone {Repo}
cd into the directory
  cd {Repo}
Setup a virtual envrionment
  python3 -m venv {venv Name}
Start the applicaiton
  python3 app.py
```
The applicaiton will now be avalible from the machine it is being run from on port 3000 
```http://127.0.0.1:3000```

---
#### **Docker**
```
Clone this repo
  git clone {Repo}
cd into the directory
  cd {Repo}
Build the image
  docker build -t {app name} .  #Do not forget the . to use the current director for the build
--OR--
Pull the image from Docker Hub
  docker pull gtechnology/pyapi

Start the Docker Container
  docker run -dp 80:3000 gtechnology/pyapi #80 can be any souce port you want, 
  but the destination must remain 3000
  
```
The applicaiton will now be avalible from the machine it is being run from on port 80, or which ever port was used for the source 
```http://127.0.0.1```

---
#### **Kubernetes**
```
Clone this repo
  git clone {Repo}
cd into the directory
  cd {Repo}
Apply the manifest yml 
  kubectl apply -f ./front_deploy.yml
This should create everything needed to access the applicaiton on port 80. 
Depending on where it is run, or cloud platform used, there may be firewall or 
ingress rules that are needed to allow outside connections.
```
The applicaiton will now be avalible from the public IP over port 80
```http://127.0.0.1```

