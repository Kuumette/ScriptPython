from astropy.io import fits
import sys

img = fits.getdata('C:\\Users\\Ballatore\\Desktop\\testImage\\image\\' + sys.argv[1], ext=0) 

dark = fits.getdata('C:\\Users\\Ballatore\\Desktop\\testImage\\image\\' + sys.argv[2]) 

darksub = dark - img 

fits.writeto('C:\\Users\\Ballatore\\Desktop\\testImage\\sub\\' + sys.argv[3], darksub) # save 

  
print("This is the name of the program:", sys.argv[0])
  
print("Argument List:", str(sys.argv))