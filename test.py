from lastImage import *
import time

start = time.time()
print("The time used to execute this is given below")
# ------------------------------------------------ #

###----### LastImage ###----###
# fits_to_png_niveaux("./image/") ## OK
# png_to_jpg("./image/*.png", 80) ## OK
# remove_image('./image/*.', "png") ## OK
# remove_image('./image/*.', "fits") ## OK

# ------------------------------------------------ #

###----### Soustraction ###----###
# soustraction("./image/", "APICAM.2020-02-16T01_32_15.000.fits", "APICAM.2020-02-16T01_34_45.000.fits", "APICAM.2020-02-16T01_32_15.000C.fits") ## OK
# fits_to_png_niveaux("./image/") ## OK
# png_to_jpg("./image/*.png", 20) ## OK
# remove_image('./image/*.', "png") ## OK
# remove_image('./image/*.', "fits") ## OK

# ------------------------------------------------ #

###----### Animation ###----###
# fits_to_png_niveaux("./image/") ## OK
# png_to_jpg("./image/*.png", 80) ## OK
# remove_image('./image/*.', "png") ## OK
# remove_image('./image/*.', "fits") ## OK
# resize_for_anim("./image/", 1024, 1024, 80) ## OK
# date_image("./image/") ## OK
# remove_first_image("../imgVideo/") ## OK
# move_image("../image/", "../imgVideo/") ## OK
# rename_image_anim("../imgVideo/") ## OK
# video('../imgVideo', '1024', '1024', '30', 'a') ## OK

# ------------------------------------------------ #

###----### Sub Animation ###----###
# soustraction("./image/", "APICAM.2020-02-16T01_37_45.000.fits", "APICAM.2020-02-16T01_40_15.000.fits", "APICAM.2020-02-16T00_37_45.000C.fits") ## OK
# fits_to_png_niveaux("./image/") ## OK
# png_to_jpg("./image/*.png", 20) ## OK
# remove_image('./image/*.', "png") ## OK
# remove_image('./image/*.', "fits") ## OK
# resize_for_anim("./image/", 1024, 1024, 50) ## OK
# date_image("./image/") ## OK
# remove_first_image("../imgVideo/") ## OK
# move_image("../image/", "../imgVideo/") ## OK
# rename_image_anim("../imgVideo/") ## OK
# video('../imgVideo', '1024', '1024', '30', 'a') ## OK

# ------------------------------------------------ #

end = time.time()

print(end - start)