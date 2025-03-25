import cv2
from PIL import Image

from util import get_limits
##################################################
object_color = input('Enter name of color')

n = 3
print("Acoording to the color name ,enter the three colors code no. (from 0 to 255) search on browser")
colorBoxlst = []  

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))  
    colorBoxlst.append(element)  

print("Your list:", colorBoxlst)
############################################################
#green = [0, 255, 0]  # yellow in BGR colorspace

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=colorBoxlst)          ############

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()

cv2.destroyAllWindows()


