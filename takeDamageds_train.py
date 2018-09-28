import numpy as np
import os
import cv2
import time
import serial # you need to install the pySerial :pyserial.sourceforge.net
import Tkinter
# your Serial port should be different!
arduinoData = serial.Serial('/dev/cu.usbmodem14111', 9600)

cam = cv2.VideoCapture(0)

cv2.namedWindow("Capture")

img_counter = 0

while True:
    ret, frame = cam.read()
    # cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        timestr = time.strftime("%Y%m%d-%H%M%S")
        img_name = "Bur_images/train/color/damaged/" + timestr + "DamagedBur.png".format(img_counter)
        img_name_gray = "Bur_images/train/gray/damaged/" + timestr + "GrayDamagedBur.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(img_name_gray,gray_image)
        print("{} written!".format(img_name_gray))
        arduinoData.write('1')
        img_counter += 1

cam.release()

cv2.destroyAllWindows()