# Deploying a Website Visitor Counter – Flask + Redis + Docker

A containerized web application that tracks website visits using Flask and Redis.
Built as part of a Capstone Project to demonstrate Docker-based microservices,
persistent storage, and server-side rendering with Jinja2.

## 🛠 Tech Stack
- Python (Flask)
- Redis
- Docker & Docker Compose
- Jinja2 Templates

## 📐 Architecture
Browser → Flask App → Redis

## ✨ Features
- Counts website visits
- Reset counter functionality
- Persistent Redis storage using Docker volumes
- Fully containerized setup
- Jinja2 HTML templates

## 📂 Project Structure
visitor-counter/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── templates/
│ └── index.html
└── README.md


---

## 🚀 Getting Started
---
🚀 Step-by-Step Setup
##🔹 Step 1: Clone the Repository
git clone https://github.com/MenaMagdyHalem/Flask-Redis-DockerCompose-App.git
cd Flask-Redis-DockerCompose-App
##🔹 Step 2: Build and Start the Application

docker-compose up -d --build
##🔹 Step 3: Access the Application

Once the containers are running, open your browser and go to:

👉 http://localhost:5000

You’ll see a webpage showing how many times the page has been visited.


### Prerequisites
- Docker
- Docker Compose

### Run the Application

```bash
docker-compose up --build
```
---
## Usage



