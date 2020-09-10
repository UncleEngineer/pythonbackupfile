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
print('----------')
# ------------------

path = r'C:\Users\Uncle Engineer\Desktop\Work\download'
allfile = os.listdir(path)

'''
filename = 'test.txt'
filename = os.path.join(path,filename)
file = open(filename, 'wb').write

filename = 'test.txt'
result = ftp.retrbinary("RETR " + filename, file)
print('RESULT:',result)
'''
allfileserver = ftp.nlst()

for f in allfileserver:
    if f[-3:] == 'txt':
        print(f)
        filename = f
        filename = os.path.join(path,filename)
        file = open(filename, 'wb').write
        filename = f
        result = ftp.retrbinary("RETR " + filename, file)
        print('RESULT:',result)
