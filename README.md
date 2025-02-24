🚀 FastAPI Deployment on AWS EC2 with Docker & GitHub Actions

This repository contains a FastAPI application that is containerized using Docker, deployed on an AWS EC2 instance, and integrated with CI/CD using GitHub Actions.
I have also attached many screenshots along the process, so people can refer to those as well.

🔥 Features

✅ FastAPI Backend with RESTful APIs✅ Dockerized Application for portability✅ AWS EC2 Hosting with automatic deployment✅ CI/CD Pipeline using GitHub Actions✅ Automated Testing using Pytest✅ WebSocket Support for real-time updates (Bonus)

📌 1️⃣ Local Setup & Running FastAPI

1. Clone the Repository

git clone https://github.com/your-username/fastapi-ec2-deploy.git
cd fastapi-ec2-deploy

2. Create a Virtual Environment and Install Dependencies

python -m venv newenv
newenv\Scripts\activate  # Windows  
source newenv/bin/activate  # macOS/Linux  

pip install -r requirements.txt

3. Run FastAPI Locally

python main.py

📌 Open Swagger UI at: http://127.0.0.1:8000/docs

📌 2️⃣ Dockerizing the FastAPI Application

1. Build the Docker Image

docker build -t my_fastapi_app .

2. Run the Docker Container

docker run -d -p 80:80 --name my_fastapi_app my_fastapi_app

📌 The application should now be accessible at: http://localhost/docs

📌 3️⃣ Deploying to AWS EC2

1. Launch an AWS EC2 Instance

Go to AWS Console → EC2 → Launch Instance

Choose Ubuntu 22.04 LTS

Select t2.micro (Free Tier Eligible)

Create and download a key pair (e.g., ec2-key.pem)

Enable port 80 in security groups for public access

2. SSH Into EC2

ssh -i ec2-key.pem ubuntu@your-ec2-public-ip

3. Install Docker on EC2

sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker $USER
newgrp docker

4. Deploy FastAPI Container on EC2

docker pull your-dockerhub-username/my_fastapi_app:latest
docker run -d -p 80:80 --name my_fastapi_app your-dockerhub-username/my_fastapi_app:latest

📌 Your API is now live at: http://your-ec2-public-ip/docs

📌 4️⃣ Automating Deployment with GitHub Actions

1. Add GitHub Secrets

Go to GitHub Repository → Settings → Secrets & Variables → Actions and add:

Secret Name

Value

EC2_HOST

your-ec2-public-ip

EC2_USER

ubuntu

EC2_SSH_KEY

(Copy-Paste contents of ec2-key.pem)

DOCKER_USERNAME

Your Docker Hub Username

DOCKER_PASSWORD

Your Docker Hub Password

2. Create GitHub Actions Workflow

📌 Create the file:

📂 .github/workflows/deploy.yml

Then, define your deployment workflow.

📌 5️⃣ Running Tests with Pytest

1. Create a Test File

📌 Location:

📂 tests/test_main.py

Add your test cases inside this file.

2. Run Tests Locally

pytest

📌 6️⃣ Verifying Deployment

1. Check Running Containers

docker ps

2. Access API in Browser

📌 Open: http://your-ec2-public-ip/docs
