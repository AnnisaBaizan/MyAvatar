# Annisa Baizan
# 061930700722
# 5 CA
# UTS Pengolahan Citra Digital ("Shape Identification")
# --image/-i UTS_Identification.png

import argparse
import imutils
import cv2

def sort_contours(cnts, method="bottom-to-top"):
    reverse = True
    i = 1
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    return (cnts, boundingBoxes)

class ShapeDetector:
    def _init_(self):
        pass
    def detect(self, c):
        shape = "unidentified"
        approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
        if len(approx) == 3: shape = "Segitiga" 
        elif len(approx) == 4: shape = "Persegi"
        elif len(approx) == 5: shape = "Segilima"
        elif len(approx) == 8:
            cX, cY, w, h = cv2.boundingRect(approx)
            ar = float(w)/h
            print(ar)
            if ar >= 0.1 and ar <=1: shape = "Lingkaran"
            elif ar >= 1 and ar <=1.1: shape = "Octagon"
            else: shape = "Bintang"
        elif len(approx) == 10: shape = "Bintang"
        else: shape = "Elips"
        return shape

ap = argparse.ArgumentParser()
ap.add_argument("--image", "-i", required = True, help = "Path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3,1), 0)
thres = cv2.threshold(blurred, 52, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thres.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
(cnts, boundingBoxes) = sort_contours(cnts, method="bottom-to-top")

sd = ShapeDetector()

for (i, c) in enumerate(cnts):
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    shape = sd.detect(c)

    c = c.astype("float")
    c = c.astype("int")
    cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
    cv2.putText(img, shape, (cX - 35, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
    
    cv2.imshow("UTS-Annisa_Baizan-061930700722", img)
    cv2.waitKey()

cv2.imwrite('UTSAnnisaBaizan061930700722.png', img)
cv2.destroyAllWindows()