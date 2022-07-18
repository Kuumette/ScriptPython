# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import json

fileObject = open("overlay.json", "r")
jsonContent = fileObject.read()
obj_python = json.loads(jsonContent)

# Open an Image
img = Image.open('./canvas.png')

for key in obj_python:
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    # Custom font style and font size
    myFont = ImageFont.truetype('arial', 65)
    # Add Text to an image
    # X, Y, text, font, fill = couleur
    I1.text((obj_python[key]['X'], obj_python[key]['Y']), obj_python[key]['name'], font=myFont, fill =(255, 0, 0))
    
# Display edited image
img.show()
# Save the edited image
img.save("./overlay.png")
