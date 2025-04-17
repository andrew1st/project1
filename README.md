# Project 1: Asynchronous API with FastAPI
**Goal:** Build a high-performance, scalable REST API using FastAPI with asynchronous processing, authentication (JWT/OAuth2), database integration (PostgreSQL), and deployment using Docker &amp; AWS Lambda.

## 🏗️ Project Setup
1️⃣ Prerequisites:
- Python 3.8+
- PostgreSQL (or SQLite for local dev)
- Docker
- AWS Account (for Lambda deployment)
- GitHub (for version control)

## 🎯 Project Goals & Progress Checklist
✅ Create a REST API with FastAPI

✅ Use Async Programming (asyncio) for improved efficiency

✅ Secure API with JWT Authentication

✅ Integrate a PostgreSQL Database with SQLAlchemy

✅ Dockerize the Application for Deployment

[ ] Deploy to AWS Lambda using Terraform

[ ] Implement CI/CD Pipeline for Auto Deployment


#### 📌 Next Steps
1. Optimize API performance (profiling, caching).
1. Extend API with new features (WebSockets, caching with Redis).


#### ☑ Task Breakdown: Project 1 – Async API with FastAPI ☑
✅ *Phase 1: Environment Setup*
-  ~~Create project folder and initialize Git repository~~
- ~~Set up virtual environment and install packages (fastapi, uvicorn, sqlalchemy, databases, etc.)~~
- ~~Set up base main.py and a /docs endpoint~~

*Phase 2: Async CRUD API*
- ~~Define a SQLAlchemy model for a resource (e.g., Task, User, Note)~~
- Set up PostgreSQL or SQLite DB and connect with databases package
- Implement basic async CRUD endpoints (GET, POST, PUT, DELETE)

*Phase 3: Authentication*
- Add JWT-based login and registration routes
- Create middleware or dependencies to protect routes
- Add OAuth2PasswordBearer flow

*Phase 4: Docker & Testing*
- Write Dockerfile and .dockerignore
- Add pytest test suite for endpoints
- Spin up containers and test locally

*Phase 5: Deployment*
- Set up deployment scripts or use Terraform
- Deploy to AWS Lambda or EC2 using Docker image
- Monitor logs and test endpoint response from a hosted environment

*Phase 6: CI/CD*
- Create .github/workflows/deploy.yml
- Automate testing and deployment to your staging/production environment
