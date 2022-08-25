import shutil
import os
src = ('C:/Users/Ballatore/Desktop/testImage/sub')
dst = ('C:/Users/Ballatore/Desktop/testImage/image')
 
for fic in os.listdir(src):
     shutil.copy2((src+'/'+fic),dst)