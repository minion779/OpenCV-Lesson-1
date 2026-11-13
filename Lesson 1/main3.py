import cv2
import os

image = cv2.imread("spongebob.jpeg", 0)
cv2.imshow("sdfsdf", image)
path = r"C:\Users\anaad\OneDrive\Documents\Desktop\OpenCV with Python\Lesson 1"
os.chdir(path)
cv2.imwrite("blackandWhiteSpongebob.jpeg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()