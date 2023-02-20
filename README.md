# Assignment


Requirements: 

# Part 1: Create an API server

Using an API server framework of your choice (FastAPI, Express.js, etc.) create an API server
with the following APIs. We work mostly with Python and Node JS at Finn AI, so we do appreciate
selecting a framework written in those languages!

1. Jumble API
a. Takes a word and re-arranges the characters randomly.

2. Audit API
a. Returns the last 10 API calls made to the server.
i. What API was called.
ii. What payload was given.

If you find you have time leftover, feel free to show off your technical skills! Do tell
us what extras you’ve done.
Latest supported python versions for Fast-API: to be 3.7 and above!

Implemented Extras:
Input sanitization

# Part 2: Dockerize your solution

● Construct a Dockerfile to containerize your API server in Part 1.

● Provide a README with clear instructions on how another developer can update and
build your solution locally.

# Part 3: Deploy your solution to minikube / minishift

● Create a deployment template for your API server.
○ Helm is our tool of preference.

● Provide clear instructions on how to deploy this API server to a local orchestration
platform (minikube / minishift).

Implemented Extras:

This project utilizes Kubernetes YAML files, which are written in a declarative configuration language in YAML format, to define the desired state of Kubernetes resources such as deployments and services. In addition to using Helm for deployment template creation, I have also tried creating deployment files using these YAML files.

# Quick Start:

The following command will clone the repository to your local terminal and allow you to build the project using your preferred editor, such as VS Code:

$ git clone https://github.com/chintan9999/Assignment.git
 
# Containerization of Fast-API Server:

This section provides instructions for containerizing the Fast-API server using Docker. The following steps must be performed to download and install Docker on a local machine and build the Docker image locally:

To download and install docker on local machine:

1.) For Windows operating system:

 Download docker-desktop from https://www.docker.com/products/docker-desktop/ and install Docker-Desktop

2.) For Linux operating system:

On CentOS, you can install Docker by running the following commands in a terminal:

$sudo yum install docker
$sudo systemctl start docker
$sudo systemctl enable docker

3.) For MAC operating system:

Visit the Docker website (https://www.docker.com/products/docker-desktop) and download the Docker Desktop installer for Mac.

Building the Docker Image locally:

4.) To build or use this image, navigate to the project directory where the "Assignment" folder is stored using the terminal.

5) Navigate to the project directory where "Assignment" folder stored
   For Example, 
   cd C:\python_tutorials\Assignment

6) Pull the Docker image from Docker Hub to the local machine by running the following command in the VScode terminal:

   $ docker pull cpatel4/fastapi-assignment:latest

   Note that since this image is pulled from a public repository, it won't ask for any username or password.
   
# Note: Only follow below steps 7 and 8, if you wish to change anything in existing docker image.

7) If you wish to modify any variable or settings, you can open the existing Dockerfile or create a new one in your preferred editor and rebuild the image to reflect your changes.

8) To build the Docker image, run the following command, replacing [image name] with the desired name for the image and [tag] with a version tag (e.g., latest or 1.0.0):

$ docker build -t [image name]:[tag] .

# Running the Docker Container from Dokcer Image:

1) Run the Docker container by executing the following command:

Use the command "docker run" to start the container, with the option "-p" to specify the port mapping between the container and the host machine, and the option "--name" to give a name to the container. The command should be followed by the name of the Docker image.

Example:

$ docker run -p 8000:8000 --name fastapi-container fastapi-assignment:latest

Note: This will map the port 8000 on the host machine to the port 8000 on the container, where the FastAPI server is running.
   
    
2) Access the running application in the container by opening a web browser and navigating to http://localhost:8000. You can also try other endpoints by adding "/audit", "/jumble/hello", or "/jumble/ns8eqnd" to the URL.

3)To stop the running container, open another terminal/bash in VS Code and execute the following command:

 $ docker kill fastapi-container

Note: This will kill the container with the name "fastapi-container".



----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Steps to deploy Fast-API server to a local orchestration platform like minikube using a Helm chart:

1) If you don't have Minikube installed on your computer, follow the instructions on the Kubernetes website to install it.

2) If you don't have Helm installed on your computer, follow the instructions on the Helm website to install it.

3) After making sure that Minikube and Helm are properly installed, download the necessary files and deployment files created using Helm by cloning the provided Git repository. You can either use the Git command-line tool or download the repository as a ZIP file and extract it to a local directory.

4) Go to the root directory of the cloned Helm chart repository.

5) To make sure everything is correct, you can validate the template by running the following command in your terminal:

 $ helm template .\fastapi-chart\
 $ helm lint .\fastapi-chart\
If no errors appear, proceed to the next step.

6) Install the release using the provided Helm chart:

$ helm install <release-name> .\fastapi-chart\
For example: helm install fastapi .\fastapi-chart\
Replace <release-name> with a name for your Helm release.
 
7) Check that the API server is running in the Kubernetes cluster by running the following command:

$ kubectl get pods
$ kubectl get all

Obtain the URL to access your API server by running the following command in PowerShell:

 $ minikube service fast-api-service --url
 
This command will output the URL you can use to access your API server.

By following these steps, you should have successfully deployed your API server to a local orchestration platform like Minikube using a Helm chart.

# Steps to deploy Fast-API server to a local orchestration platform like minikube using declarative Kubernetes YAML files:

Assuming that you have already cloned the Git repository and are currently in the "Assignment" directory, follow these steps:
 
1.) To navigate inside the "Assignment" directory, type the following command in your terminal:

    $ cd Assignment/
 
 2.) Inside the "Assignment" directory, there is a k8s deployment template folder that contains the deployment.yml and service.yml files. To execute both files at  
     once, run the following command:
     
     $ kubectl apply -f k8s
     
 3.) Once you execute the above command, both files will be successfully applied to the local Minikube cluster and three pods will be created. You can check this by 
     running the following command:
     
     $ kubectl get pods
 
 4.) To obtain more information about the deployment, run the following command:
     
     $ kubectl get all
 
 5.) To access the services running on the pods, open the Minikube (command line or PowerShell) and run the following command:

     $ minikube service fast-api-service --url
 
 This will display a URL that can be used to access the services running inside the Minikube cluster from outside. By accessing this URL, you can verify that the 
 services are running properly behind the cluster.
