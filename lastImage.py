import sys
import numpy as np
import os
import cv2
from astropy.io import fits
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from skimage.exposure import rescale_intensity
import glob
import os
import re
import shutil

# Fonction fits en png en modifiant le niveaux avec en parametre le chemin ou se trouve les images
def fits_to_png_niveaux(path):
    print("Fits to Png")
    # Chemin ou se trouve les images
    dir_list = os.listdir(path) 

    # Pour chaque element de mon dossier
    for fit in dir_list:
        fitsfilename = path + '/' + fit
        
        # Ouverture de l'image
        d = fits.open(fitsfilename)[0].data

        # Calculez le q-ième centile des données le long de l'axe spécifié.
        p0,p99 = np.percentile(d,(10,99))

        # Renvoie l'image après avoir étiré ou réduit ses niveaux d'intensité.
        a = rescale_intensity(d, in_range=(p0, p99))

        # Crée une nouvelle image avec le mode et la taille donnés.
        image = Image.fromarray(a)

        # remplace fits en png
        imagename = fitsfilename.replace('.fits', '.png')
    
        # Sauvgarde l'image
        image.save(imagename)

# Fonction png en jpg en parametre le chemin et la qualiter
def png_to_jpg(path, quality):
    print("Png to Jpg")
    png_file_paths = glob.glob(path)

    for i, png_file_path in enumerate(png_file_paths):
        jpg_file_path = png_file_path[:-3] + "jpg"
    
        # Load .png image
        image = cv2.imread(png_file_path)

        # Save .jpg image
        cv2.imwrite(jpg_file_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

        pass

# Suppression des images inutile
def remove_image(path, extension):
    print("Suppression")
    py_files = glob.glob(path + extension)
    # Pour chaque element de mon dossier
    for py_file in py_files:
        try:
            # Supression des fichiers
            os.remove(py_file)
        except OSError as e:
            print(f"Error:{ e.strerror}")

# Soustraction de deux image avec comme parametre le nom de la premiere image le nom de la deuxieme image et le nom de la soustraction avec la suppresion de l'image a et b
def soustraction(path, a, b, c):
    print("Soustraction")
    imgA = path + a
    imgB = path + b
    a = fits.getdata(path + a, ext=0) 
    b = fits.getdata(path + b) 

    darksub = b - a 

    fits.writeto(path + c, darksub) # save 

    os.remove(imgA)
    os.remove(imgB)

# Fonction qui permet de redimentionner les image de la video
def resize_for_anim(path, x, y, quality):
    print("Resize Image")
    root_dir = path

    for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
        im = Image.open(filename)
        imResize = im.resize((x,y), Image.ANTIALIAS)
        imResize.save(filename , 'JPEG', quality=quality)

# Fonction qui permet d'ajouter la date et l'heure sur les image de la video en fonction de leur nom 
def date_image(path):
    print("Ajouter date heure sur image")
    url = path

    list_of_files = os.listdir(url)
    print (list_of_files)

    os.chdir(url)   

    i = 0
    # Pour chaque fichier 
    for a in os.listdir('.'):
        # j'ai tranformer le nom du fichier en tableau 
        l = list_of_files[i]
        # Je recup la date
        date = l[7:17]
        # Je recup l'heure
        heure = l[18:20] + ":" + l[21:23] + " UT"
        
        # creating a image object 
        img = Image.open(a)
        I1 = ImageDraw.Draw(img)
        I2 = ImageDraw.Draw(img)
        I3 = ImageDraw.Draw(img)

        # Choix de la police d'écriture
        myFont = ImageFont.truetype('arial', 20)
        
        # Insert le text sur l'image
        I1.text((28, 36), date, font=myFont, fill=(255, 255, 255))
        I2.text((28, 56), heure, font=myFont, fill=(255, 255, 255))
        I3.text((28, 76), "Apicam", font=myFont, fill=(255, 255, 255))

        # Save
        img.save(list_of_files[i])
        i += 1

# Fonction qui permet de renomer les images
def rename_image_anim(path):   
    files = os.listdir(path)

    for index, file in enumerate(files):
        # Si index et plus petit que 10
        if index < 10:
            # Alors rename avec 2 zero
            os.rename(path+file, path + '00' + str(index)+ '.jpg')
        else:
            # Sinon rename avec 1 zero
            os.rename(path+file, path + '0' + str(index)+ '.jpg')

# Fonction qui permet de faire la video (parametre : 1. path, 2. x, 3. y, 4. quality, 5. name)
def video(path, x, y, quality, name):
    # Changement de dossier
    os.chdir(path)
    # Ligne de commande pour la creation de la video
    os.system('ffmpeg -r 5 -f image2 -s ' + x + 'x' + y + ' -i %03d.jpg -vcodec libx264 -crf ' + quality + ' -pix_fmt yuv420p ' + name + '.mp4')

# Fonction qui permet de supprimer la premiere image
def remove_first_image(path):
    files = os.listdir(path)
    a = files[0]
    print(a)
    file_name= path + a
    os.remove(file_name)

# Fonction qui permet de deplacer la nouvelle image dans le dossier pour la video
def move_image(source, destination):
   
    files = os.listdir(source)

    for file in files:
        new_path = shutil.move(f"{source}/{file}", destination)
        print(new_path)
