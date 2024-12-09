# Project-Template
## Researcher-Service Installation Guide

### Installation Methods


1. Create and activate a Python virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   ```

2. Fill in .env
    ```
    cp .env-example .env
   ```
   fill in GCP_MYSQL_CONNECTION_STRING

2. Install required packages and launch the backend service:
   ```
   pip3 install -r requirements.txt
   uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
   ```


### Deploy conatiner to vm
```
gcloud compute instances create-with-container user-profile-vm \
    --container-image=us-central1-docker.pkg.dev/coms-4153-cloud-computing/user-profile/user-profile:364cba1021a84d0db2cb5dca5f6db4421f604386 \
--machine-type e2-micro --tags http-server
```

```
gcloud compute firewall-rules create allow-http \
 --allow tcp:80 --target-tags http-server
 ```
