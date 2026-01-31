# 🌐 Website Visitor Counter  
**Flask • Redis • Docker • Docker Compose**

A production-style, containerized and deploying a web application that tracks website visits using a Flask backend and Redis for persistent storage. This project demonstrates modern backend development practices, microservice communication, Docker-based deployment, and persistent state management.

---

## 📌 Project Overview

This application increments and displays a visitor count every time the homepage is accessed. The counter value is stored in Redis and persists across container restarts using Docker volumes. The frontend is rendered using Jinja2 templates, and the entire stack runs via Docker Compose.

This project is ideal for **portfolio showcasing and resume demonstration**.
---
## 🧰 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, Jinja2 Templates  
- **Database:** Redis  
- **Containerization:** Docker, Docker Compose  

---
## 📐 Architecture
- Client Browser
↓
- Flask Web App (Container)
↓
- Redis Data Store (Container + Volume)


---

## ✨ Features

- Dynamic visitor counter
- Server-side rendering using Jinja2
- Reset counter functionality (POST request)
- Persistent Redis storage with Docker volumes
- Fully containerized microservice setup
- One-command startup using Docker Compose


---
## 📂 Project Structure
<img width="199" height="206" alt="image" src="https://github.com/user-attachments/assets/2528eacb-2163-430f-ad60-c99a26fbb0e8" />


--- 

## 🚀 Getting Started

## 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/sofiane-jell/Capstone_project-02-Website-Visitor-Counter-Application-using-Flask-and-Redis-using-docker.git
cd Capstone_project-02-Website-Visitor-Counter-Application-using-Flask-and-Redis-using-docker
```
## 🔹 Step 2: Build and Start the Application
```bash
docker-compose up -d --build
```
## 🔹 Step 3: Access the Application

Once the containers are running, open your browser and go to:

👉 http://localhost:5000

You’ll see a webpage showing how many times the page has been visited.
<img width="1259" height="412" alt="image" src="https://github.com/user-attachments/assets/bcb7dae8-9f1a-4177-8102-e0b2d3892449" />
Refresh the page to increment the counter.
Click <b>Reset Counter</b> to reset the value.

<img width="1044" height="483" alt="image" src="https://github.com/user-attachments/assets/f8d6a723-0e75-4974-97dc-c84bd7907dc1" />

## 🔹 Step 4: Check Running Containers
<img width="1885" height="135" alt="image" src="https://github.com/user-attachments/assets/91cc8199-02e6-4a3a-aa8c-7cb84cffa6a9" />

## 🔹 Step 5: Stop the Application
To stop and remove the containers:
<img width="1899" height="190" alt="image" src="https://github.com/user-attachments/assets/ba9d626e-e747-4b32-9ab7-825003468971" />

---
## 💾 Data Persistence
Redis data is persisted using a Docker named volume, ensuring the visitor count remains intact even after container restarts or shutdowns.
Setting Up Redis to Save Data with a Volume named in docker-compose.yml:
```yaml
volumes:
  redis-data:
```



## 🧠 Key Learning Outcomes
- Building and containerizing a Flask web application

- Inter-service communication using Docker networking

- Managing persistent state in containerized applications

- Applying REST principles (GET/POST)

- Using Docker Compose for multi-container orchestration




