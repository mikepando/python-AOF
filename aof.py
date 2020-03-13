import re
import os
import smtplib

from datetime import date
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from list import users

#Walking the directory
os.path.join('usr','bin','spam') #allows this to run on windows/mac/linux

#SMTP Settings
port=587 
smtp_server="smtp.office365.com"
myemail="username@mail.com" #this is your email address login and the sender email
password="password" #to bypass MFA with Office365, you need to use an App Password

today=date.today()
subject="Files for " + str(today) #Shows subject text with the current date.
body="""\
Hello,

Attached is your file. Please confirm that it is accurate.
If there are any issues or concerns, please reach out.

Thank you,
Your Name"""

success=0 #counters for success/failure
failures=0

email_list = dict((k.lower(), v) for k, v in users.items()) #Creates a new dictionary with all the keys in lowercase

for folderName, subfolders, filenames in os.walk(".\\outgoing_files"):
    for filename in filenames:
        justfilename, file_extension = os.path.splitext(filename) #splits the filename from the extension
        client_name=justfilename.lower()
        if client_name in email_list:
            client_email=email_list[client_name]
            print(client_name,"-",client_email)
            try:    #If we find a match, lets try sending the file using SMTP
                message=MIMEMultipart()
                message["From"]=myemail
                message["To"]=client_email
                message["Subject"]=subject
                message.attach(MIMEText(body, "plain"))
                with open(".\\outgoing_files\\"+filename, "rb") as attachment:
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
                mailserver.login(myemail, password)
                mailserver.sendmail(myemail, client_email, text)
                mailserver.quit()
                success=success+1
                print("An email has been sent!\n")
            except Exception as e:
                failures=failures+1
                print("Oops!", e ,"occured.\n")
        else: 
            failures=failures+1
            print("Error:", client_name, "was not found in the email list. Please check the REPS.PY file.\n")
print("This script has finished with",failures,"errors and",success,"emails sent.")
