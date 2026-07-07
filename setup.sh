#!/bin/bash
# setup.sh — Local environment setup for TheContactBook

echo "🚀 Starting TheContactBook environment setup..."

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null
then
    echo "❌ kubectl not found. Please install it first."
    exit 1
fi

# Check namespace existence
echo "🔍 Checking namespace 'thecontactbook'..."
kubectl get namespace thecontactbook &> /dev/null
if [ $? -ne 0 ]; then
    echo "⚠️ Namespace 'thecontactbook' not found. Creating it..."
    kubectl create namespace thecontactbook
else
    echo "✅ Namespace 'thecontactbook' already exists."
fi

# Port‑forward Grafana
echo "📊 Forwarding Grafana dashboard (port 3000)..."
kubectl port-forward -n monitoring svc/kube-stack-grafana 3000:80 &
sleep 3

# Port‑forward Argo CD
echo "🔄 Forwarding Argo CD server (port 8090)..."
kubectl port-forward svc/argocd-server -n argocd 8090:443 &
sleep 3

# Port‑forward TheContactBook service
echo "📒 Forwarding TheContactBook service (port 8000)..."
kubectl port-forward svc/thecontactbook-service 8000:8000 -n thecontactbook &
sleep 3

echo "✅ All services are now accessible:"
echo "   • TheContactBook → http://localhost:8000"
echo "   • Grafana → http://localhost:3000"
echo "   • Argo CD → https://localhost:8090"
echo "🎯 Setup complete!"
