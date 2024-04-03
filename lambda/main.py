import smtplib
from email.mime.text import MIMEText
import base64
import os
import json
import pymysql

# SMTP environment variables
smtp_host =  os.environ.get("SMTP_HOST") #"smtp.mailgun.org"
smtp_port = os.environ.get("SMTP_PORT") #587 
smtp_username = os.environ.get("SMTP_USERNAME")
smtp_password = os.environ.get("SMTP_PASSWORD")
smtp_verification_link = os.environ.get("SMTP_VERIFICATION_LINK")
smtp_from_email = os.environ.get("SMTP_FROM_EMAIL")
# Db environment variables
db_host = os.environ.get("DB_HOST_IP")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_database = os.environ.get("DB_DATABASE")
db_table = os.environ.get("DB_TABLE")

def store_sent_email(username):
    # Create connection to private cloud sql and run update query
    Connection = pymysql.connect(host = db_host,
    user=db_user,
    password=db_password,
    database=db_database,
    cursorclass=pymysql.cursors.DictCursor)
    with Connection:
        with Connection.cursor() as cursor:
            print("Connected to database")
            query = "UPDATE " + db_table + " SET email_sent = CURRENT_TIMESTAMP, verify_email_sent = TRUE WHERE username = '" + username + "';"
            print(query)
            cursor.execute(query)
            Connection.commit()
    print("Update query executed")

def send_email(username):
    try:
        message = """<!DOCTYPE html>
                      <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        </head>
                        <body>
                            <p>Dear {},</p>
                            <p>Here is your verification link: <a href="{}/{}" target="_blank">{}/{}</a></p>
                        </body>
                      </html>"""
        message = message.format(username, smtp_verification_link, username, smtp_verification_link, username)

        msg = MIMEText(message, "html")
        msg["Subject"] = "Verify Your  Email"
        msg["From"] = smtp_from_email
        msg["To"] = username

        s = smtplib.SMTP(smtp_host, smtp_port)
        s.login(smtp_username, smtp_password)
        s.sendmail(msg["From"], msg["To"], msg.as_string())
        s.quit()
        print("Email sent to user: ", username)

        store_sent_email(username)  
    except Exception as e:
        print("Exception e: ", e)
        print("Email not sent")

def lambda_function(cloud_event, e):
    # Get PubSub message as JSON
    userData = base64.b64decode(cloud_event["data"])
    userJSON = json.loads(userData)
    userEmail = userJSON["username"]
    # Get the data from cloud event
    print("userData: ", userData)
    print("Stack Trace e: ", e)
    send_email(userEmail)