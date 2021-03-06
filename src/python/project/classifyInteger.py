import cv2
import numpy as np
import subprocess
import sys
import os

def get_integer(img_str):
    current_path = os.path.dirname(os.path.abspath(__file__))
    SSOCR_PATH = os.path.join(current_path, '../../../libs/ssocr')

    # converting image str (ByteIO) to numpy array
    np_array = np.fromstring(img_str, np.uint8)

    # decode the nparray to a color image
    cv_img = cv2.imdecode(np_array, cv2.CV_LOAD_IMAGE_COLOR)

    # Adding median blur to the image pixels
    img = cv2.medianBlur(cv_img,5)

    # define range of required  color in HSV (blue)
    lower_color = np.array([55,55,55])
    upper_color = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img, lower_color, upper_color)

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
