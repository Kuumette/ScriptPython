import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

url = "C:\\Users\\Ballatore\\Desktop\\testImage\\image"

list_of_files = os.listdir(url)
print (list_of_files)

os.chdir(url)   


i = 0
for a in os.listdir('.'):
    l = list_of_files[i]

    date = l[7:17]
    heure = l[18:20] + ":" + l[21:23] + " UT"
    
    img = Image.open(a)
    print(img)

    I1 = ImageDraw.Draw(img)
    I2 = ImageDraw.Draw(img)
    I3 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('arial', 20)
    
    I1.text((28, 36), date, font=myFont, fill=(255, 255, 255))
    I2.text((28, 56), heure, font=myFont, fill=(255, 255, 255))
    I3.text((28, 76), "Apicam", font=myFont, fill=(255, 255, 255))

    print(img)

    

    img.save(list_of_files[i])
    i += 1