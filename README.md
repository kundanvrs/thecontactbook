Perfect — let’s extend your **README.md** to also cover the **GitHub Actions CI/CD pipeline** you’ve set up for building, pushing, and updating Kubernetes manifests. Here’s a polished version that ties everything together:

```markdown
# 📒 TheContactBook

A CRUD application built with **FastAPI**, **Python**, **PostgreSQL**, and a simple frontend using **HTML, CSS, JS**.  
It is deployed locally using **Docker** and **Kubernetes**, with **GitOps** principles implemented via **Argo CD**.  
Application statistics are monitored on **Grafana** using **Prometheus**.  
CI/CD automation is handled via **GitHub Actions**.

---

## 🚀 Features
- **CRUD Operations**: Create, Read, Update, Delete contacts.
- **GitOps Workflow**: Declarative deployments managed via Git.
- **Argo CD Integration**: Continuous delivery and sync with Git.
- **Monitoring**: Metrics scraped by Prometheus and visualized in Grafana.
- **CI/CD**: Automated build, push, and manifest update via GitHub Actions.
- **Local Deployment**: Runs on Docker and Kubernetes.

---

## 🛠️ Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Docker, Kubernetes
- **GitOps**: Argo CD
- **Monitoring**: Prometheus + Grafana
- **CI/CD**: GitHub Actions

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

## ⚡ GitHub Actions Workflow

The CI/CD pipeline automates:
1. **Build & Push Docker Image** (multi‑arch: amd64 + arm64).
2. **Update Kubernetes Manifest** with the new image tag.
3. **Commit & Push** manifest changes back to Git (GitOps).
4. **Argo CD Sync** ensures cluster state matches Git.

### Example Workflow (`.github/workflows/deploy.yml`)
```yaml
name: Build, Push, and Update Manifest (GitOps)

on:
  push:
    branches: [ "main" ]

jobs:
  build-push-and-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
    - name: Checkout Repository Code
      uses: actions/checkout@v4

    - name: Set up QEMU
      uses: docker/setup-qemu-action@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Authenticate with Docker Hub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Convert Docker Username to Lowercase
      id: string
      run: echo "lowercase_owner=$(echo '${{ secrets.DOCKER_USERNAME }}' | tr '[:upper:]' '[:lower:]')" >> $GITHUB_OUTPUT

    - name: Build and Push Multi-Arch Image
      uses: docker/build-push-action@v6
      with:
        context: .
        file: ./Dockerfile
        platforms: linux/amd64,linux/arm64
        push: true
        tags: |
          ${{ steps.string.outputs.lowercase_owner }}/thecontactbook-web:latest
          ${{ steps.string.outputs.lowercase_owner }}/thecontactbook-web:${{ github.sha }}

    - name: Update Kubernetes Manifest Tag
      run: |
        git config --global user.name "GitHub Actions Bot"
        git config --global user.email "actions@github.com"
        sed -i "s|image: .*thecontactbook-web:.*|image: ${{ steps.string.outputs.lowercase_owner }}/thecontactbook-web:${{ github.sha }}|g" k8s/thecontactbook-web.yml
        if ! git diff --quiet; then
          git add k8s/thecontactbook-web.yml
          git commit -m "chore: update thecontactbook-web image tag to ${{ github.sha }} [skip ci]"
          git push
        else
          echo "No changes detected, skipping commit."
        fi
```

---

## 📊 Workflow Summary
1. Developer pushes code → GitHub Actions builds & pushes Docker image.
2. Workflow updates Kubernetes manifest → commits back to Git.
3. Argo CD detects manifest change → syncs cluster.
4. Application runs in Kubernetes → monitored via Prometheus & Grafana.

---

## 🔑 Useful Commands
- **Build Docker image**: `docker build -t thecontactbook:latest .`
- **Run container**: `docker run -d -p 8000:8000 thecontactbook:latest`
- **Create namespace**: `kubectl create namespace thecontactbook`
- **Apply manifests**: `kubectl apply -f k8s/ -n thecontactbook`
- **Port forward service**: `kubectl port-forward svc/thecontactbook-service 8000:8000 -n thecontactbook`

---

## ✅ Conclusion
This project demonstrates a **complete DevOps lifecycle**:  
CRUD app → Containerized → Deployed on Kubernetes → GitOps with Argo CD → CI/CD via GitHub Actions → Monitored via Prometheus & Grafana.
```

## 📊 Workflow Summary
1. Developer pushes code → GitHub Actions builds & pushes Docker image.
2. Workflow updates Kubernetes manifest → commits back to Git.
3. Argo CD detects manifest change → syncs cluster.
4. Application runs in Kubernetes → monitored via Prometheus & Grafana.

![TheContactBook DevOps Pipeline](main/workflow.png)
