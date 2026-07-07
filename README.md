
# 📒 TheContactBook

A CRUD application built with **FastAPI**, **Python**, **PostgreSQL**, and a simple frontend using **HTML, CSS, JS**.  
It is deployed locally using **Docker** and **Kubernetes**, with **GitOps** principles implemented via **Argo CD**.  
Application statistics are monitored on **Grafana** using **Prometheus**.

---

## 🚀 Features
- **CRUD Operations**: Create, Read, Update, Delete contacts.
- **GitOps Workflow**: Declarative deployments managed via Git.
- **Argo CD Integration**: Continuous delivery and sync with Git.
- **Monitoring**: Metrics scraped by Prometheus and visualized in Grafana.
- **Local Deployment**: Runs on Docker and Kubernetes.

---

## 🛠️ Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Docker, Kubernetes
- **GitOps**: Argo CD
- **Monitoring**: Prometheus + Grafana

---

## ⚙️ Setup & Deployment Steps

### 1. Clone Repository
```bash
git clone https://github.com/your-repo/thecontactbook.git
cd thecontactbook
```

### 2. Build Docker Image
```bash
docker build -t thecontactbook:latest .
```

### 3. Run Locally with Docker
```bash
docker run -d -p 8000:8000 --name thecontactbook thecontactbook:latest
```

### 4. Deploy on Kubernetes
Create a namespace:
```bash
kubectl create namespace thecontactbook
```

Apply manifests:
```bash
kubectl apply -f k8s/deployment.yaml -n thecontactbook
kubectl apply -f k8s/service.yaml -n thecontactbook
```

### 5. Port Forward Service
Access the app locally:
```bash
kubectl port-forward svc/thecontactbook-service 8000:8000 -n thecontactbook
```
Now open: `http://localhost:8000` 

### 6. GitOps with Argo CD
- Install Argo CD in your cluster.
- Connect your Git repository containing Kubernetes manifests.
- Argo CD continuously syncs cluster state with Git.

### 7. Monitoring with Prometheus & Grafana
- Prometheus scrapes metrics from FastAPI and Kubernetes.
- Grafana dashboards visualize application statistics.
- Example: API request counts, latency, DB connections.

---

## 📊 Workflow Summary
1. Developer pushes code → Git repository updated.
2. Argo CD detects changes → Syncs manifests to Kubernetes.
3. Application runs in cluster → Exposed via service.
4. Prometheus scrapes metrics → Grafana displays dashboards.

---

## 🔑 Useful Commands
- **Build Docker image**: `docker build -t thecontactbook:latest .`
- **Run container**: `docker run -d -p 8000:8000 thecontactbook:latest`
- **Create namespace**: `kubectl create namespace thecontactbook`
- **Apply manifests**: `kubectl apply -f k8s/ -n thecontactbook`
- **Port forward service**: `kubectl port-forward svc/thecontactbook-service 8000:8000 -n thecontactbook`

---

## 📌 Notes
- Ensure Docker and Kubernetes are installed locally.
- PostgreSQL should be configured either as a container or Kubernetes StatefulSet.
- Update `deployment.yaml` with correct DB connection strings.
- Grafana dashboards can be customized for API and DB metrics.

---

## ✅ Conclusion
This project demonstrates a **full DevOps lifecycle**:  
CRUD app → Containerized → Deployed on Kubernetes → GitOps with Argo CD → Monitored via Prometheus & Grafana.
```
