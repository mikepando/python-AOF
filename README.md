# Automate Outgoing Files with Python
*This Python script sends a file as an attachment to an email address derived from the filename.*

![Output](https://i.imgur.com/PYtfFui.png)


This was made to automate the task of sending batches of individual files to their respective users. This script crawls the ```outgoing_files``` directory for filenames with a unique number to then match to an email dictionary we have created in an Excel. Only files in the ```outgoing_files``` folder are affected. 

### Requirements
* [Python 3.8.1](https://www.python.org/downloads/)
* [xlrd](https://xlrd.readthedocs.io/en/latest/)
* _Optional:_ [Enable ANSI in console](https://stackoverflow.com/questions/16755142/how-to-make-win32-console-recognize-ansi-vt100-escape-sequences)
"In latest Windows 10, you can enable ANSI in console via the following reghack -- in ```HKCU\Console``` create a DWORD named ```VirtualTerminalLevel``` and set it to ```0x1```; then restart cmd.exe." - [BrainSlugs83](https://stackoverflow.com/questions/16755142/how-to-make-win32-console-recognize-ansi-vt100-escape-sequences#comment92954461_16799175)

#### Utilizes
* [os](https://docs.python.org/3/library/os.html) - To crawl a directory
* [smtplib](https://docs.python.org/3/library/smtplib.html) - For sending files as attachments

## How It Works
This script runs based on a unique identifier at the end of a filename. In the environment for which it was built, filenames looked like this: ```15648_271_1902_159406.pdf```. That last group of characters (159406) is the unique identifier. This script will take that number and search the excel sheet for a matching number in the first column. If a match is found, it will use the email address from the fourth column. An email will then be sent to that address with the file as an attachment.

##### SMTP Settings
1. The ```port``` and ```smpt_server``` variables need to match the settings of your email provider. 
   - A list of common servers and ports can be found at [Arclab](https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html).
2. The ```myemail``` variable needs to be changed to your full email address. You need to include the extension: ```username@mail.com```.
3. The ```password``` variable needs ***special attention***. If you use MFA (Multi-factor authentication) with your provider, you need to create an _App Password_. MFA will prevent authorization otherwise. If you do not use MFA, just use your regular password.
   - App Passwords with [Office 365](https://support.office.com/en-us/article/Create-an-app-password-for-Office-365-3e7c860f-bda4-4441-a618-b53953ee1183).
   - App Passwords with [Gmail](https://support.google.com/accounts/answer/185833?hl=en).
4. The ```sender_email``` variable allows you to choose the outgoing email address. This will be different from ```myemail``` if you have an alias or send-as permissions to another mailbox you want to use. 
5. Change the ```subject``` variable to fit your needs. It's default output is ```Files for 2020-02-03``` where the date changes to the current date when the file is run.
6. Then modify the ```body``` variable to fit the message you intend to mass send. It is set send in plain text.

#### Customization
To change the rows/columns that are used for the unique identifier and email address:
- Change the numbers in the brackets of the find_email function. Numbers start at 0.
- ```if row_value[0] == float(unique):``` and ```email=row_value[2]```
            
##### (Optional) Running from a Batch file
- You can run this file by launching a batch file instead of using an IDE.
- Right Click -> Edit the ```Send.bat``` file and make sure the path for python.exe matches the location of your python installation.

###### Disclaimer
*This was made for a very niche use in an office environment. It won't work for you out of the box.*
