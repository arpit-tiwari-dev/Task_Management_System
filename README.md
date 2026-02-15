
# Task Management API — Cloud Ready FastAPI Service

A cloud-ready Task Management API built with **FastAPI**, **MongoDB**, and **Kubernetes**, demonstrating scalable backend architecture, containerization, SDK integration, and deployment practices.

This project was developed as part of a technical assessment to showcase backend engineering skills, cloud readiness, and system design understanding.

---

## Features

### Core API Features
- Create, update, delete, and list tasks
- Pagination support
- Task completion endpoint
- Task priority and status management
- Optional task due dates

### Persistence
- MongoDB used for persistent task storage
- Repository layer abstraction for clean DB interaction

### External SDK Integration
- GitHub SDK integration
- Automatically creates GitHub issues for tasks (optional)
- Stores GitHub issue ID in database

### Background Processing
- Background jobs handle GitHub issue creation asynchronously
- API responses remain fast while external operations run in background

### Cloud & Deployment Ready
- Dockerized application
- Multi-container setup with MongoDB
- Kubernetes deployment using Minikube
- Autoscaling using Horizontal Pod Autoscaler
- Health and readiness probes configured

---

## Tech Stack

- FastAPI
- MongoDB
- Motor (Async Mongo client)
- PyGithub SDK
- Docker
- Kubernetes (Minikube)
- Python 3.10+

---

## Architecture Overview



      Client

        ↓

    FastAPI API Layer

        ↓

    Service Layer (Business Logic)

        ↓

    Repository Layer

        ↓

      MongoDB




    Background Jobs 

         ↓

    GitHub issue creation

---

Responsibilities are cleanly separated:
- Routes contain no database logic
- Repository handles persistence
- Services handle business logic
- SDK integrations isolated in services

---

## API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/tasks` | Create task |
| GET | `/tasks` | List tasks |
| GET | `/tasks/{id}` | Get task |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |
| POST | `/tasks/{id}/complete` | Mark complete |
| GET | `/health` | Liveness check |
| GET | `/ready` | Readiness check |

Interactive docs available at:

```

/docs

````

---

## Task Model

```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "status": "pending | in_progress | completed",
  "priority": "low | medium | high",
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "due_date": "optional timestamp",
  "external_reference_id": "github issue id"
}
````

---

## Running Locally

### Requirements

* Docker
* Docker Compose

### Start services

```bash
docker-compose up --build
```

API runs at:

```
http://localhost:8000/docs
```

---

## Kubernetes Deployment (Minikube)

### Start cluster

```bash
minikube start
```

### Use Minikube Docker

```bash
minikube docker-env | Invoke-Expression
```

### Build image

```bash
docker build -t task-api .
```

### Deploy resources

```bash
kubectl apply -f k8s/
```

### Access service

```bash
minikube service task-api
```

---



## Health Monitoring

Kubernetes probes ensure reliability:

* `/health` → container alive
* `/ready` → app ready to serve traffic

Pods automatically restart if unhealthy.

---

## Design Decisions

### Why FastAPI?

High performance, async support, automatic documentation.

### Why MongoDB?

Flexible schema suited for task storage and rapid iteration.

### Why Background Jobs?

Prevents API slowdown during external SDK calls.

### Why Kubernetes?

Demonstrates deployment and scalability readiness.

---

## Future Improvements

Possible extensions:

* Authentication & user ownership
* Email notifications for due tasks
* Slack integration
* Retry mechanisms for SDK failures
* Metrics & monitoring dashboards
* Task search and filtering
* Autoscaling for scalability

---

## Project Structure

```
app/
├── routes.py
├── services/
├── repository.py
├── db/
├── service.py
├── model.py
├── main.py
├── settings.py
k8s/
Dockerfile
docker-compose.yml
requirements.txt
```

---

## Demo Walkthrough

A walkthrough video demonstrates:

* API usage
* Architecture explanation
* Containerization
* Kubernetes deployment
* Autoscaling behavior

(Video link included in submission)

---

## Conclusion

This project demonstrates the ability to:

* Design scalable backend services
* Integrate external SDKs
* Containerize applications
* Deploy to Kubernetes
* Build production-ready API architecture

```
```
