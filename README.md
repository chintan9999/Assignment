# Assignment
Containerization of FAST-API Server:

This docker image contains necessary files, dependencies, and modules require to run FAST-API server locally.

Requirements: 

Latest supported python versions for Fast-API: to be 3.7 and above!


Docker must be installed on local machine to pull the image from Docker Hub, update the local image and build solutions locally.

To download and install docker on local machine:

1.) For Windows operating system:

 Download docker  from https://www.docker.com/products/docker-desktop/ and Install Docker-Desktop

2.) For Linux operating system:

On Ubuntu, you can install Docker by running the following commands in a terminal:
sudo yum install docker
sudo systemctl start docker
sudo systemctl enable docker

On CentOS, you can install Docker by running the following commands in a terminal:
sudo yum install docker
sudo systemctl start docker
sudo systemctl enable docker

3.) For MAC operating system:

Visit the Docker website (https://www.docker.com/products/docker-desktop) and download the Docker Desktop installer for Mac.

Building the Docker Image:

In order to build or use this image, please execute following command at your local terminal.

1) Clone the GIT repository

    git clone [repository URL]

2) Navigate to the project directory

     cd [project directory]

3) Pull this image from docker hub to your local machine.

     docker pull cpatel4/fastapi-assignment:latest

     NB: Since this image is pulled from public repo., it won't ask any userid or password.


4) If you wish to change any variable or settings, open or create new Dockerfile in your choice of editor locally and rebuild the image to reflect your changes.

5) Build the Docker image:
    docker build -t [image name]:[tag] .

    N.B: Replace [image name] with the desired name for the image and [tag] with a version tag (e.g. latest or 1.0.0).

Running the Docker Container

1) Start the Docker container by executing following command:

   docker run -p [host port]:[container port] --name [container-name] [image name]:[tag]

   Note: replace [host port] with the port on your local machine that you want to use to access the container and [container port] with the port that the container is listening on.
   replace [image name] and [tag] with the name and tag of the image you built in the previous step.
    
2) Open a web browser and navigate to http://localhost:[host port] to access the running application.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Steps to deploy Fast-API server to a local orchestration platform like minikube using a Helm chart:

1.) Install Minikube on your local machine, if it is not already installed. You can find instructions for installing Minikube on the Kubernetes website.

2.) Install Helm on your local machine, if it is not already installed. You can find instructions for installing Helm on the Helm website.

3.) Clone the Git repository provided for the project which includes necessary files including deployment files created using Helm. You can either use the Git 
     command-line tool or download the repository as a ZIP file and extract it to a local directory.
   
4.) Navigate to the root directory of the cloned Helm chart repository.

5.) you can validate the template prior installing in your local machine for sanity check, using following command.

     helm template .\fastapi-chart\
      helm lint .\fastapi-chart\ 

6.) If file is showing no errors, please go ahead and install the release using the helm chart provided.

      helm install <release-name> .\fastapi-chart\

      Replace <release-name> with a name for your Helm release.

7.)  Verify that the API server is running in the Kubernetes cluster using the following command:
        
       kubectl get pods

       Kubectl get all
       
8.) Obtain the URL to access your API server by running the following command:

     minikube service fast-api-service --url

    This command will output the URL you can use to access your API server.

With these steps, you should have successfully deployed your API server to a local orchestration platform like minikube using a Helm chart.
