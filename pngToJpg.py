#importing required packages and library
# import cv2
# import os
# from os.path import splitext
# # Loading .png image
# path = "C:\\Users\\Ballatore\\Desktop\\testImage\\image\\"
# dir_list = os.listdir(path) 
# #print(dir_list)
# for i in dir_list:
#     print(i)
 
#     png_img = cv2.imread(i)
#     cv2.imwrite(i, png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


# from PIL import Image
# from os import listdir
# from os.path import splitext

# target_directory = 'C:\\Users\\Ballatore\\Desktop\\testImage\\image\\'
# target = '.jpg'

# for file in listdir(target_directory):
#     filename, extension = splitext(file)
#     try:
#         if extension not in ['.py', target]:
#             im = Image.open(filename + extension)
#             im.save(filename + target, "JPEG")
#     except OSError:
#         print('Cannot convert %s' % file)
from PIL import Image
import os

directory = r'C:\\Users\\Ballatore\\Desktop\\testImage\\image\\'
c=1
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        im = Image.open(filename)
        name='img'+str(c)+'.png'
        rgb_im = im.convert('RGB')
        rgb_im.save(name)
        c+=1
        print(os.path.join(directory, filename))
        continue
    else:
        print("else")
        continue