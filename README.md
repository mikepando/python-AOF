# Automate Outgoing Files with Python
*This Python script sends a file as an attachment to an email address derived from the filename.*

![Output](https://i.imgur.com/2cY0q5b.png)


This was made to automate the task of sending batches of individual files to their respective users. This script crawls the ```outgoing_files``` directory for filenames to then index our user directory. Only files in the ```outgoing_files``` folder are affected. 

### Requirements
You only need Python to run this script.
* [Python 3.8.1](https://www.python.org/downloads/)

#### Utilizes
* [os](https://docs.python.org/3/library/os.html) - To crawl a directory
* [smtplib](https://docs.python.org/3/library/smtplib.html) - For sending files as attachments


## Configuration
You need to populate the dictionary in the **list.py** file with the names and email addresses of your recipients. 

There are a few variables in the **AOF.py** file which need their values adjusted.

##### SMTP Settings
1. The ```port``` and ```smpt_server``` variables need to match the settings of your email provider. 
   - A list of common servers and ports can be found at [Arclab](https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html).
2. The ```myemail``` variable needs to be changed to your full email address. You need to include the extension: ```username@mail.com```.
3. The ```password``` variable needs ***special attention***. If you use MFA (Multi-factor authentication) with your provider, you need to create an _App Password_. MFA will prevent authorization otherwise. If you do not use MFA, just use your regular password.
   - App Passwords with [Office 365](https://support.office.com/en-us/article/Create-an-app-password-for-Office-365-3e7c860f-bda4-4441-a618-b53953ee1183).
   - App Passwords with [Gmail](https://support.google.com/accounts/answer/185833?hl=en).
4. Change the ```subject``` variable to fit your needs. It's default output is ```Files for 2020-02-03``` where the date changes to the current date when the file is run.
5. Then modify the ```body``` variable to fit the message you intend to mass send. It is set send in plain text.

##### (Optional) Running from a Batch file
- You can run this file by launching a batch file instead of using an IDE.
- Right Click -> Edit the ```Send.bat``` file and change ```"Path where your Python exe is stored\python.exe"``` to match the location of your python exe. Make sure to ***keep the quotations***.
  - A common installation location is ```Users\USERNAME\AppData\Local\Programs\Python\Python38\python.exe```

###### Disclaimer
*This was made for educational purposes and was tailored to a specific scenario. The code is available to anyone to use and modify to fit their purpose.*
