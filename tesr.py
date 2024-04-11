import os 
from cryptography.fernet import Fernet


#key = Fernet.generate_key()
key = b'Pi36QMaVySjaQBVjm37jxrIQyRxJyL8PuyhD2OhL3Ck='
cipher_suite = Fernet(key)

path = "//mypath//test linux//"
file = "test.linux"


with open(file=os.path.join(path,file),mode="w") as filee:
      text = "a7a,17-Feb-24"
      text2 = "AHmed moshen,5-mar-24 23:29"
      #filee.writelines([cipher_suite.encrypt(text),cipher_suite.encrypt(text2)])
      filee.writelines(["\n",text,text2])



# try:
#     with open(file=os.path.join(path, file), mode="rb") as filee:
#         for everyfile in filee:
#             decrypted_data = cipher_suite.decrypt(everyfile.strip()).decode().split(",")
#             print(decrypted_data)
# except Exception as e: print(e)
