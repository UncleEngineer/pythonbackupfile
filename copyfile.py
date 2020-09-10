import os
import shutil

path = r'C:\Users\Uncle Engineer\Desktop\Work'
destination = 'F:\\HERE'
allfile = os.listdir(path)


for f in allfile:
    if f[-3:] == 'txt':
        #print(f)
        source = os.path.join(path,f)
        dest = os.path.join(destination,f)
        print(source)
        print(dest)
        shutil.copy2(source,dest)
        print('----')     
