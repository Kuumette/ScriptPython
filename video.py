import os 
from PIL import Image  
import cv2  
import time

start = time.time()
print("The time used to execute this is given below")
print(os.getcwd())  
  
os.chdir("C:\\Users\\Ballatore\\Desktop\\testImage\\imgVideo")   
path = "C:\\Users\\Ballatore\\Desktop\\testImage\\imgVideo"
  # C:\\Users\\Ballatore\\Desktop\\testImage\\imgVideo
mean_height = 0
mean_width = 0
num_of_images = len(os.listdir('.')) 
  
for file in os.listdir('.'): 
    im = Image.open(os.path.join(path, file)) 
    width, height = im.size 
    mean_width += width 
    mean_height += height 
    
  
mean_width = int(mean_width / num_of_images) 
mean_height = int(mean_height / num_of_images) 
  
  
for file in os.listdir('.'): 
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
        
        im = Image.open(os.path.join(path, file))  
   
        
        width, height = im.size    
        print(width, height) 
  
        
        imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)  
        imResize.save( file, 'JPEG', quality = 95) 
        
        print(im.filename.split('\\')[-1], " is resized")  
  
  
def generate_video(): 
    image_folder = '.'
    video_name = '1.mp4'
    os.chdir("C:\\Users\\Ballatore\\Desktop\\testImage\\imgVideo") 
      
    images = [img for img in os.listdir(image_folder) 
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith("png")] 
     
    
    
    print(images)  
  
    frame = cv2.imread(os.path.join(image_folder, images[0])) 
  
    
    
    height, width, layers = frame.shape   
    # cv2.VideoWriter(video_name, fourcc, fps, size)
   
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = 5.0 # 0,5 secondes
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))  
  
    
    for image in images:  
        video.write(cv2.imread(os.path.join(image_folder, image)))  
      
    
    cv2.destroyAllWindows()  
    video.release()  
  
  
generate_video() 
end = time.time()

print(end - start)