

import os
import time

path = 'C:/Users/Ballatore/Desktop/testImage/sub/'
files = os.listdir(path)


for index, file in enumerate(files):
    print(index)
    if index < 10:
        os.rename(path+file, path + '00' + str(index)+ '.jpg')
    else:
        os.rename(path+file, path + '0' + str(index)+ '.jpg')
  




# Renaming the file

# Essayez ce code :

# from os import listdir,path,rename
# from sys import argv
# import re
# import os
# paths = 'C:/Users/Ballatore/Desktop/testImage/imgVideo/'
# files = os.listdir(paths)
# for i in files:
#     if i == argv[0] or not path.isfile(i):
#         continue
#     if re.match('\d{3}',i):
#         rename(i,'0'+i)
