# Automate Outgoing Files with Python
*This Python script sends a file as an attachment to an email address derived from the filename.*

This was made to automate the task of sending files to individual users. Previously, a user would receive 60+ files (e.g. C2 forms) and send each individual their file, up to three times per month. This script creates an email address based off of the filename ```FIRST LAST.DOCX``` and sends the file as an attachment to that respective email adress with a preconfigured subject and body. It utilizes Regular Expressions to only execute on filenames that match the ```First Last``` format. Only files in the ```Outgoing_Files``` are affected. 

### Requirements
You only need Python to run this script.
* [Python 3.8.1](https://www.python.org/downloads/)


## Configuration
There are a few variables in the **AOF.py** file which need their values adjusted.

##### Creating the receiver_email address 
1. The ```email``` variable should be adjusted to match the recipients email extension, e.g., ```@gmail.com, @aol.com, @companyname.com```.
   - All the recipients have to have the same email extension. In my usage, all recipients were assigned a company email, making the username the only changing variable. 
   - This script creates email adresses based off the filename. All files must be in a ```First Last``` format. The email address format used is `First initial + Last name + email`. A file named ```John Doe.docx``` would be rendered as ```JDoe@mail.com```.

##### SMTP Settings
2. The ```port``` and ```smpt_server``` variables need to match the settings of your email provider. 
   - A list of common servers and ports can be found at [Arclab](https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html).
3. The ```login``` and ```sender_email``` variables needs to be changed to your full email address. You need to include the extension: ```username@mail.com```.
4. The ```password``` variable needs ***special attention***. If you use MFA (Multi-factor authentication) with your provider, you need to create an _App Password_. MFA will prevent authorization otherwise. If you do not use MFA, just use your regular password.
   - App Passwords with [Office 365](https://support.office.com/en-us/article/Create-an-app-password-for-Office-365-3e7c860f-bda4-4441-a618-b53953ee1183).
   - App Passwords with [Gmail](https://support.google.com/accounts/answer/185833?hl=en).
5. Change the ```subject``` variable to fit your needs. It's default output is ```Files for 2020-02-03``` where the date changes to the current date when the file is run.
6. Then modify the ```body``` variable to fit the message you intend to mass send. It is set send in plain text.

##### (Optional) Running from a Batch file
- You can run this file by launching a batch file instead of using an IDE.
- Right Click -> Edit the ```Send.bat``` file and change ```"Path where your Python exe is stored\python.exe"``` to match the location of your python exe. Make sure to ***keep the quotations***.
  - A common installation location is ```Users\USERNAME\AppData\Local\Programs\Python\Python38\python.exe```

###### Disclaimer
*This was made for educational purposes and was tailored to a specific scenario. The code is available to anyone to use and modify to fit their purpose.*
