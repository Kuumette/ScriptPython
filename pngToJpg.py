import cv2
import glob
import os
import re

png_file_paths = glob.glob(r"./image/*.png")
for i, png_file_path in enumerate(png_file_paths):
    jpg_file_path = png_file_path[:-3] + "jpg";
   
    # Load .png image
    image = cv2.imread(png_file_path)

    # Save .jpg image
    cv2.imwrite(jpg_file_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 80])

    pass
    