
import os
import numpy as np

path = 'C:/Users/Ballatore/Desktop/testImage/image/'
files = os.listdir(path)
# arr=np.array(files)
a = files[0]
print(a)
file_name= path + a
# for file in files:
# arr=np.delete(arr,49)
# print(arr)
os.remove(file_name)
