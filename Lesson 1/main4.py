import cv2

image = cv2.imread("spongebob.jpeg", 1)
print(image)
cv2.imshow("origImage", image)
B,G,R = cv2.split(image)
cv2.imshow("blueSatImage", B)
cv2.imshow("greenSatImage", G)
cv2.imshow("redSatImage", R)

cv2.waitKey(0)
cv2.destroyAllWindows()