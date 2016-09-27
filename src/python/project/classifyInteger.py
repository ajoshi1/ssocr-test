import cv2
import numpy as np
import subprocess
import sys
import os

def get_integer(img_name):
    currentPath = os.path.dirname(os.path.abspath(__file__))
    SSOCR_PATH = os.path.join(currentPath, '../../../libs/ssocr')

    # Reading the passed image
    img = cv2.imread(img_name)
    # Adding median blur to the image pixels
    img = cv2.medianBlur(img,5)

    # define range of required  color in HSV (blue)
    lower_blue = np.array([55,55,55])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)
    
    # threshold the image 
    ret2,thresh = cv2.threshold(res,130,255,0)
    
    # Convert the image to black and white
    bw = cv2.cvtColor(thresh, cv2.COLOR_RGB2HSV)

    # write the bw image to a temp file
    cv2.imwrite('temp_bw_img.png', bw)

    result = subprocess.check_output(SSOCR_PATH + ' -T -f white  -d -1 temp_bw_img.png', shell=True)
    subprocess.call('rm temp_bw_img.png', shell=True)
    return int(result)

def cleanup():
    subprocess.call('rm temp_bw_img.png', shell=True)

if __name__ == "__main__":
    print get_integer(sys.argv[1])
    cleanup()
