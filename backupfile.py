import ftplib

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
filename = 'test.txt'

fileupload = open(filename, 'rb')
result = ftp.storbinary('STOR ' + filename, fileupload)
print('RESULT:',result)
print('AFTER:',ftp.nlst())






