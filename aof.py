import re
import os
import smtplib
import xlrd

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Walking the directory
os.path.join('usr','bin','spam') #allows this to run on windows/mac/linux

#SMTP Settings
port=587 
smtp_server="smtp.office365.com"
myemail="username@email.com" #this is your email address login
password="" #to bypass MFA with Office365, you need to use an App Password
sender_email='alias@email.com' #The outgoing email address. For aliases or mailboxes your account has send-as permissions for

excel_file='sheet.xlsx' #this is the location of the excel file where the values are stored
file_path='\outgoing_files' #location to crawl for files 

subject="This is a subject (Do not reply to this email)"
body="""\
<html>
    <body>
        <div>
        <p>some text</p>
        </div>
    </body
></html>
"""

class bcolors:  #Defining the color we will add to our output
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

success=0 #counters for success/failure
failures=0

def find_email(path,unique):  #function that opens a workbook, then returns the cell value of the email address column, if the unique value matches the cell value of the unique column 
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)

    for row_num in range(sheet.nrows):
        row_value = sheet.row_values(row_num)
        if row_value[0] == float(unique):
            email=row_value[2] #Change the value to match the desired row on your spreadsheet
            return(email)

f=open('last_sent.txt','w')
for folderName, subfolders, filenames in os.walk(file_path): #crawls shared folder on network
    for filename in filenames:
        justfilename, file_extension = os.path.splitext(filename) #splits the filename from the extension
        getUnique=justfilename.split("_")
        unique=getUnique[3]
        email=find_email(excel_file,unique)
        if email != None:
            print(f"{bcolors.UNDERLINE}File{bcolors.ENDC}:",filename,f"{bcolors.UNDERLINE}Recipient{bcolors.ENDC}:",email)
            try:    #If the email value is not NULL, lets try sending it as an attachment
                message=MIMEMultipart()
                message["From"]=sender_email
                message["To"]=email
                message["Subject"]=subject
                message.attach(MIMEText(body, "html"))
                with open(file_path+"/"+filename, "rb") as attachment:
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
                mailserver.sendmail(myemail, email, text)
                mailserver.quit()
                success=success+1
                f.write(filename+" "+email+"\n")
                print(f"{bcolors.OKGREEN}An email has been sent!{bcolors.ENDC}\n")
            except Exception as e:
                failures=failures+1
                print(f"{bcolors.FAIL}Oops!{bcolors.ENDC}", e ,f"{bcolors.FAIL}occured.{bcolors.ENDC}\n")
        else: 
            failures=failures+1
            print(f"{bcolors.FAIL}Error:{bcolors.ENDC}", filename, f"{bcolors.WARNING}has a NULL email field or is missing from the excel sheet.{bcolors.ENDC}")
f.close()
print("This script has finished with",failures,"error(s) and",success,"files sent.")
