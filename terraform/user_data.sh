#!/bin/bash
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Git
sudo yum install git -y

# Clone Repo and Run
cd /home/ec2-user
git clone https://github.com/valensniyonkuru/Multi-Container-App.git
cd Multi-Container-App
# Assuming the user pushes the code before this runs, or I push it. 
# We need to make sure the latest code is there. 
docker-compose up -d
