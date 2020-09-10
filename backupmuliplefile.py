import ftplib
import os

SERVER = 'uncle-test-server.com'
PORT = 2002
USER = 'testuser@uncle-test-server.com'
PASSWORD = "]6';bL;di"

ftp = ftplib.FTP()
ftp.connect(SERVER,PORT)
ftp.login(USER,PASSWORD)
mypath = '/testcopyfile/uncle'

enterpath = ftp.cwd(mypath)
print('BEFORE:',ftp.nlst())
print('----------')
# ------------------

path = r'C:\Users\Uncle Engineer\Desktop\Work'
allfile = os.listdir(path)

for f in allfile:
    if f[-3:] == 'txt':
        filename = os.path.join(path,f)
        fileupload = open(filename, 'rb')
        result = ftp.storbinary('STOR ' + f, fileupload)
        print('RESULT:',result)
        print('AFTER:',ftp.nlst())
        print('-----')




