import cv2
import numpy as np

img = 255 * np.ones((395,420,3), np.uint8)

#box 
cv2.rectangle(img, (66,18), (384,334), (0,0,0),3)
cv2.rectangle(img, (66,18), (384,334), (15,54,138),-1)
cv2.line(img, (384,334), (357,374), (0,0,0),3)
cv2.line(img, (357,374), (39,374), (0,0,0),3)
cv2.line(img, (39,374), (66,334), (0,0,0),3)
cv2.line(img, (39,374), (39,58), (0,0,0),3)
cv2.line(img, (66,18), (39,58), (0,0,0),3)

j = 0
for i in range(315):
 j = j + 1
 cv2.line(img, (382 - j,337), (355 - j,374), (18,38,94),1)

 k = 0
for l in range(312):
 k = k + 1
 cv2.line(img, (39,374 - k), (63,337 - k), (18,38,94),1)

#kelopak bunga layer 1
cv2.ellipse(img,(225,175),(150,80),0,0,360,(171,130,255),-1)
cv2.ellipse(img,(225,175),(150,80),90,0,360,(171,130,255),-1)
cv2.ellipse(img,(225,175),(150,80),45,0,360,(171,130,255),-1)
cv2.ellipse(img,(225,175),(150,80),-45,0,360,(171,130,255),-1)

#kelopak bunga layer 2
cv2.ellipse(img,(225,175),(128,50),68,0,360,(137,104,205),-1)
cv2.ellipse(img,(225,175),(128,50),-68,0,360,(137,104,205),-1)
cv2.ellipse(img,(225,175),(128,50),22,0,360,(137,104,205),-1)
cv2.ellipse(img,(225,175),(128,50),-22,0,360,(137,104,205),-1)

#kelopak bunga layer 3
cv2.ellipse(img,(225,175),(96,30),0,0,360,(93,71,139),-1)
cv2.ellipse(img,(225,175),(96,30),90,0,360,(93,71,139),-1)
cv2.ellipse(img,(225,175),(96,30),45,0,360,(93,71,139),-1)
cv2.ellipse(img,(225,175),(96,30),-45,0,360,(93,71,139),-1)

#bagian center bunga
cv2.circle(img, (225,175), 50, (64,125,255), -1)

# #Antena
cv2.ellipse(img,(240,175),(50,10),68,0,225,(255,48,48),3)
cv2.ellipse(img,(215,185),(50,10),68,-225,0,(255,48,48),3)

#sayap layer 1
cv2.ellipse(img,(245,215),(85,40),-55,0,360,(48,48,255),-1)
cv2.ellipse(img,(245,215),(85,40),10,0,360,(48,48,255),-1)

#sayap layer 2
cv2.ellipse(img,(245,215),(70,30),-55,0,360,(255,48,48),-1)
cv2.ellipse(img,(245,215),(70,30),10,0,360,(255,48,48),-1)

#motif sayap
cv2.circle(img, (200,205), 10, (48,48,255), -1)
cv2.circle(img, (219,250), 10, (48,48,255), -1)
cv2.circle(img, (269,177), 10, (48,48,255), -1)
cv2.circle(img, (289,223), 10, (48,48,255), -1)

#badan
cv2.circle(img, (225,175), 15, (38,71,139), -1)
cv2.circle(img, (235,195), 15, (84,112,205), -1)
cv2.circle(img, (245,215), 15, (38,71,139), -1)
cv2.circle(img, (255,235), 15, (84,112,205), -1)
cv2.circle(img, (265,255), 15, (38,71,139), -1)

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.imwrite('MyLogo.png', img)
cv2.imshow('Show Logo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()