import os
import shutil as backup
import pandas as pd
import datetime


db_location = r'\\VBOXSVR\mypath\mypath\DB'
file = 'usersettings.linux'
lock_file = os.path.join(db_location, file +".lock")



def write_file(path, line=None):
          with open(file=lock_file,mode="w"): pass # create lock file
          try: backup.copy(src=path,dst=os.path.join(db_location,"Backup",datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + " " + file))
          except: pass
          with open(file=path, mode="a") as linuxfile: linuxfile.writelines(line)
                    
     
while not os.path.exists(lock_file):
     write_file(path=os.path.join(db_location,file),line=['Mahmoud Linux,test,Admins\n','Samysam\n'])
     try: os.remove(lock_file)
     except: pass
     break


df = pd.read_csv(os.path.join(db_location,file), skip_blank_lines=True)
print(df)
