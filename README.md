# Fastapi-mysql-docker-compose
## 🚀 FastAPI + MySQL Multi-Container App with Docker Compose
This project demonstrates a multi-container application using FastAPI as the backend and MySQL as the database, orchestrated with Docker Compose. It includes CRUD operations for managing users.

## ✅ Features
-FastAPI backend running inside a Docker container
-MySQL database with persistent storage
-Docker Compose for multi-container orchestration

## 📂 Project Structure

fastapi-mysql-docker-compose/
│
├── docker-compose.yml       # Docker Compose configuration
└── web/
    ├── Dockerfile           # FastAPI image build file
    ├── main.py              # FastAPI application
    └── requirements.txt     # Python dependencies
    
## 🛠️ Prerequisites
### Docker installed
```
docker compose version
```
comes with Docker Desktop or CLI plugin.

### 📥 Clone This Repository:

#### To clone this portfolio on your local system, run:
```
https://github.com/aakansha113/fastapi-mysql-docker-compose.git
```

#### ▶️ How to Run the Project:
```
cd fastapi-mysql-docker-compose
```

#### 2️⃣ Start Services:
```
sudo docker compose up --build -d
```

#### 3️⃣ Verify Running Containers:
```
docker ps
```

### You should see:
1-fastapi-mysql-docker-compose-web-1 (FastAPI)

2-fastapi-mysql-docker-compose-db-1 (MySQL)

### 🌐 Access the API
#### FastAPI Root Endpoint:
```
http://localhost:8000
```
### Swagger Docs:

```
http://localhost:8000/docs
```
### 🛠️ Database Access
#### To connect to MySQL inside the container:
```
docker exec -it fastapi-mysql-docker-compose-db-1 mysql -uroot -prootpass
```

#### Stop Services:
```
sudo docker compose down
sudo docker compose down -v
```

###  Author
#### Aakansha Chandrakant Hujare
#### 🚀 DevOps & Cloud Enthusiast

### ⭐ Show Your Support

#### If you like this portfolio, feel free to ⭐ star the repo!
