import cv2
img = cv2.imread("Map of Physics.png")
cv2.imshow("Image",img)
scale= 60
width = int(img.shape[1] * scale/100)
height = int(img.shape[0] * scale/100)
dim = (width,height)
resized_img = cv2.resize(img, dim, cv2.INTER_AREA)
cv2.imshow("Image-small",resized_img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()