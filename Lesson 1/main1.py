import cv2

image = cv2.imread("spongebob.jpeg", 1)

cv2.imshow("output", image)

cv2.waitKey(0)
cv2.destroyAllWindows()