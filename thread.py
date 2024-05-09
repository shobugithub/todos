import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading

from_email = "enter your email ...@gmail.com"


def send_email(to_email):
    email_message = MIMEMultipart()
    email_message['From'] = from_email
    email_message['To'] = to_email
    email_message['Subject'] = "Salom"
    email_message.attach(MIMEText("Your ad could be here, just joking", 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    server.login(from_email, 'your code')
    try:
        server.sendmail(from_email, to_email, email_message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


users = [
    "enter user's email"
]


def send_email_to_users():
    for user in users:
        send_email(user)


t1 = threading.Thread(target=send_email_to_users)
t1.start()