import numpy as np
import cv2


cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.waitKey(2000)
img = cv2.imwrite("C:\\path\\pcimg1.jpg",frame)

ret, frame = cap.read()
cv2.waitKey(2000)
img = cv2.imwrite("C:\\path\\pcimg2.jpg",frame)

ret, frame = cap.read()
cv2.waitKey(2000)
img = cv2.imwrite("C:\\path\\pcimg3.jpg",frame)

ret, frame = cap.read()
cv2.waitKey(2000)
img = cv2.imwrite("C:\\path\\pcimg4.jpg",frame)


# When everything done, release the capture

cap.release()