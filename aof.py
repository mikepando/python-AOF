import re
import os
import smtplib

from datetime import date
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Walking the directory
os.path.join('usr','bin','spam') #allows this to run on windows/mac/linux
folder=os.getcwd() #change this to the location of the excel sheets

#Creating the receiver_email address
pattern=r"^([a-zA-Z]{2,}\s[a-zA-z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"
email='@mail.com' #change this if the email extension changes

#SMTP Settings
port=587 
smtp_server="smtp.office365.com"
login="username@mail.com" #this is your email address login
password="password" #to bypass MFA with Office365, you need to use an App Password

today=date.today()
subject="Files for " + str(today) #Shows text and current date. Change the text in the ""
sender_email="username@mail.com" #change this to match your email address (same as login email)
body="""\
Hello,

Attached is your file. Please confirm that it is accurate.
If there are any issues or concerns, please reach out.

Thank you,
Your Name"""

for folderName, subfolders, filenames in os.walk(str(folder+"\\outgoing_files")):
    for filename in filenames:
        regex=re.match(pattern,filename)
        if regex:
            first=filename[0]
            last=(regex.group(0)).split(" ", 1)[1]
            receiver_email=str(first+last+email).lower()
            print(filename, receiver_email)
            try:
                message=MIMEMultipart()
                message["From"]=sender_email
                message["To"]=receiver_email
                message["Subject"]=subject
                message.attach(MIMEText(body, "plain"))
                with open(str(folder+"\\outgoing_files\\"+filename), "rb") as attachment:
                    part=MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
                )
                message.attach(part)
                text=message.as_string()

                mailserver=smtplib.SMTP(smtp_server,port)
                mailserver.ehlo()
                mailserver.starttls()
                mailserver.ehlo()
                mailserver.login(login, password)
                mailserver.sendmail(sender_email, receiver_email, text)
                mailserver.quit()
            except Exception as e:
                print("Oops!",e,"occured.\n")  
            else:
                print('Sent\n')
        else:
            print('\nThe', filename, 'file is INVALID. Please format as: FIRST LAST.\n')
