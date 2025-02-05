# Arborescence du projet

```

├── 📂 infra-k8s/                      # Répertoire principal de l'infrastructure Kubernetes
│   ├── 📂 cluster/                    # Configuration du cluster (Kind, Cluster Autoscaler)
│   │   ├── cluster.yaml               # Définition du cluster Kind et des nœuds
│   │   ├── storage.yaml               # Configuration du stockage persistant
│   ├── 📂 namespaces/                 # Création des namespaces
│   │   ├── namespaces.yaml            # Définition des namespaces (app, monitoring, security…)
│   ├── 📂 apps/                       # Déploiements des applications (backend, frontend…)
│   │   ├── backend/                   # Déploiement du backend (FastAPI)
│   │   │   ├── backend.yaml           # Manifest complet pour FastAPI (Deployment, Service, Ingress…)
│   │   ├── frontend/                  # Déploiement du frontend (React)
│   │   │   ├── frontend.yaml          # Manifest complet pour React (Deployment, Service, Ingress…)
│   ├── 📂 monitoring/                 # Stack Prometheus + Grafana
│   │   ├── prometheus.yaml            # Déploiement de Prometheus
│   │   ├── grafana.yaml               # Déploiement de Grafana
│   │   ├── alertmanager.yaml          # Alerting avec Prometheus
│   ├── 📂 security/                   # Gestion des secrets et sécurité
│   │   ├── vault.yaml                 # Déploiement de HashiCorp Vault
│   │   ├── rbac.yaml                  # Configuration des accès et rôles
│   ├── 📂 logging/                    # Stack ELK (Elasticsearch, Logstash, Kibana)
│   │   ├── elasticsearch.yaml         # Déploiement d’Elasticsearch
│   │   ├── logstash.yaml              # Déploiement de Logstash
│   │   ├── kibana.yaml                # Déploiement de Kibana
│   ├── 📂 ingress/                    # Configuration du reverse proxy Nginx
│   │   ├── ingress.yaml               # Configuration d’Ingress Nginx avec certificats TLS
│   ├── 📂 ci-cd/                      # Configuration de GitLab CI/CD
│   │   ├── gitlab-runner.yaml         # Déploiement de GitLab Runner
│   ├── 📂 backup/                     # Backup et restauration
│   │   ├── backup.yaml                # Déploiement des jobs de sauvegarde
```

