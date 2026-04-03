#ACEest Fitness & Gym – DevOps CI/CD Project
Project Overview
This project demonstrates an end-to-end DevOps implementation for a Gym Management System using Flask, GitHub, Objective
To build a Flask-based application and implement CI/CD pipeline using modern DevOps tools.
Features
Home API
Health API
Member Management APIs
Automated Testing
Dockerized Application
CI/CD Pipeline
Technologies Used
Python, Flask, Pytest, Docker, GitHub, GitHub Actions, Jenkins
Project Structure
ACEest-Fitness-Gym/
app.py
requirements.txt
test_app.py
Dockerfile
README.md
.github/workflows/main.yml
Setup Instructions
git clone https://github.com/kulkarnimrudula3-png/ACEest-Fitness-Gym.git
pip install -r requirements.txt
python app.py
Run Tests
pytest
Docker Commands
docker build -t aceest-fitness-gym .
docker run -d -p 5000:5000 aceest-fitness-gym
CI/CD Pipeline
GitHub Actions: Build, Test, Docker Build
Jenkins: Pull code, run tests, build Docker image
Conclusion
This project demonstrates a complete DevOps lifecycle with automation and reliability.
