import os
import time
import smtplib
from email.message import EmailMessage


path = r"C:\\...."

now = time.time()

fileForUpdate = []

for filename in os.listdir(path):
    if os.path.getatime(os.path.join(path, filename)) < now - 30 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            fileForUpdate.append(filename)


fileForUpdate2='\n'.join(map(str,fileForUpdate))

print(fileForUpdate2)

def sending_email(emailMsgFile):

    try:
        login = ""# login maila  
        password = ""# password maila

        subject = ""# enter a subject 

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = login
        msg['To'] = ""#consumer e-mail address 
        msg.set_content(emailMsgFile)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(login, password)
            smtp.send_message(msg)
            print("All done , e-mail sent")

    except smtplib.SMTPAuthenticationError:

        print("Login Error")
           

sending_email(fileForUpdate2)