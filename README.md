# Ngrok_unlimited
This project is based on Visitishan's Ngrok Unlimited repo (https://github.com/visitishan/ngrok_unlimited) so, read his README first to better understand what problem this project is trying to solve.
However in this repo, insthead of using PHP, i'm using CloudFunctions on GCP and Firestore DB to save and retrive the link assigned from Ngrok.

The two Python files in the directory are: one for open HTTPS connection with Ngrok and the other for a SSH connection. This programs are made for use on Linux (tested on Ubuntu 22.04), and. af course Google Cloud Platform.

- A call of the read_data_http URL will automaticly redirect on the server page shared with Ngrok
- A call of the read_data_ssh URL will print on the page the shell command to open the SSH connection (for a Mac Terminal)

### SETUP AND USE:
#### 1. Upload the functions on GCP:
Upload the CloudFunction folder in GCP's console, change directory inside the uploaded folder and run:
```
gcloud functions deploy read_data_https --region europe-west1 --runtime python37 --trigger-http --allow-unauthenticated
```
```
gcloud functions deploy read_data_ssh --region europe-west1 --runtime python37 --trigger-http --allow-unauthenticated
```
```
gcloud functions deploy update_data --region europe-west1 --runtime python37 --trigger-http --allow-unauthenticated
```
#### 2. Update URLs inside Python files in root folder with the URL assigned by GCP for access at the save_data function
#### 3. Run one of the two Python files in root folder (you can add the script inside "chrontab -e" to automaticly run it after boot)
