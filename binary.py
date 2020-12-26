import cv2

img = cv2.imread('koala.jpeg',2)
a = "11011111101100110110011001011101000"


ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

imageF = bin(bw_img ^ a)

cv2.imshow("Binary Image",imageF)


cv2.waitKey(0)
cv2.destroyAllWindows()