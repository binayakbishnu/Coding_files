import cv2

img = cv2.imread("Z:\Coding\Python\image - Copy.png")
#cv2.imshow("Image",img)

scale= 20
width = int(img.shape[1] * scale/100)
height = int(img.shape[0] * scale/100)
dim = (width,height)
resized_img = cv2.resize(img, dim, cv2.INTER_AREA)
cv2.imshow("Image-small",resized_img)
scale2= 20
width2 = int(img.shape[1] * scale2/100)
height2 = int(img.shape[0] * scale2*1.02/100)
dim2 = (width2,height2)
resized_img2 = cv2.resize(img, dim2, cv2.INTER_AREA)
cv2.imshow("Image-small2",resized_img2)
'''
gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()