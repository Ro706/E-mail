# surdmbetvbjhlarz
from email.message import EmailMessage
import ssl
import smtplib

email_sender = input("Enter your email address: ")
email_password = input("Enter your email password: ")
email_receiver = input("Enter receiver email address: ")
subject= input("Enter subject: ")
message = input("Enter message: ")
em = EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(message)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
print("message sent successfully")
    
