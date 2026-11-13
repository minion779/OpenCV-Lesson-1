import cv2

image = cv2.imread("spongebob.jpeg", 0)

cv2.imshow("blahh", image)

cv2.waitKey(0)
cv2.destroyAllWindows()