import re
import os

os.path.join('usr','bin','spam')

##folder='C:\\Users\\username\\Desktop\\folder'   #either hardcode the location or
folder=os.getcwd()  #have the file in the directory to walk
pattern="^([a-zA-Z]{2,}\s[a-zA-z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"
email='@guaranteedreturns.com'


for folderName, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        regex=re.match(pattern,filename)
        if regex: 
            first=filename[0]
            last=(regex.group(0)).split(" ", 1)[1]
            address=str(first+last+email).lower()
            print(filename, address)
        else:
            print('\nThe file name is INVALID. Please format as FIRST LAST: ', filename, "\n")