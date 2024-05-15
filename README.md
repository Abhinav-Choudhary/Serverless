# GCP (Google Cloud) Serverless Lambda Function
This Lambda function is designed to handle events triggered by an GCP Pub/Sub topic. The primary purpose of this function is to process messages received from the GCP topic, retrieve username from message, sent verification email to user and update Cloud SQL database.

# Linked Repositories
Explore the 2 additional repositories that complement this project, housing code for the REST-based CRUD operations APIs (Webapp) crafted in Java Enterprise Edition (J2EE), and the Infrastructure as Code (IaC) crafted in Terraform. 
<br>
[Webapp](https://github.com/Abhinav-Choudhary/Webapp)
<br>
[Infrastructure as Code](https://github.com/Abhinav-Choudhary/Terraform-GCP-Infrastructure)
<br>

# Functionality
This function performs following tasks:
- Retrieve base64 decoded body from GCP topic
- Decode the body and parse the JSON generated to retrieve username
- Send a verification email to the user using SMTP from Mailgun
- Update database to reflect email sent

# Environment Variables
Following environment variables are present:
- SMTP_HOST
  - default = "smtp.mailgun.org"
- SMTP_PORT
  - default = 587
- SMTP_USERNAME
- SMTP_PASSWORD
- SMTP_VERIFICATION_LINK
- SMTP_FROM_EMAIL
  - From email address to send the mail
- DB_HOST_IP
  - Private IP of Cloud SQL instance
- DB_USER
  - User for CLoud SQL instance
- DB_PASSWORD
  - Password for Cloud SQL instance
- DB_DATABASE
  - Database name for Cloud SQL instance
- DB_TABLE
  - Table name for Cloud SQL instance
