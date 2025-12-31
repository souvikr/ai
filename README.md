Zone 1: Code Deployment (Getting your code there) Azure Repo (DAGs & Scripts) --> CI/CD Pipeline (Git Sync) --> Kubernetes Cluster Volume --> Airflow Scheduler reads the new code.

Zone 2: Infrastructure (How Airflow runs) Helm Charts (The Blueprints) --> Kubernetes API Server --> Deploys Airflow Components (Scheduler, Webserver, Triggerer) + Vault Operator (The Security Guard).

Zone 3: Execution (The moment a Job runs) Scheduler Triggers Task --> Kube Executor requests a Pod --> Vault injects SSH Key into Pod --> Pod SSH connects to uk.example.com --> Script executes on server.
