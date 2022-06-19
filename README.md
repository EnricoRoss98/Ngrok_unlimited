# Ngrok_unlimited
This project is based on Visitishan's Ngrok Unlimited repo (https://github.com/visitishan/ngrok_unlimited) so, read his README first.
However, this project insthead of using PHP, uses CloudFunctions on GCP and Firestore DB.

The two Python files in the directory are: one for open HTTPS connection with Ngrok and the other for a SSH connection. Before its execution on the server, remember to update the url with the url of the function already uploaded in your GCP account. This programs are made for use on Linux (tested on Ubuntu 22.04).

- A call of the url of the read_data_http function will redirect on the HTTPS server page
- A call of the url of the read_data_ssh function will print on the page the command to open the ssh connection (for a Mac Terminal)

### SETUP AND USE:
#### 1. Upload the functions on GCP:
Upload the CloudFunction folder in GCP console, change directory inside the uploaded folder and run:
```
gcloud functions deploy read_data_https --region europe-west1 --runtime python37 --trigger-http --allow-unauthenticated
```
```
gcloud functions deploy read_data_ssh --region europe-west1 --runtime python37 --trigger-http --allow-unauthenticated
```
```
gcloud functions deploy update_data --region europe-west1 --runtime python37 --trigger-http --allow-unauthenticated
```
#### 2. Update URLs inside the Python files in root folder
#### 3. Run one of the two Python files in root folder
