import cv2

img = cv2.imread('BVP-logobk-rgb.jpg')
print(img.shape)
img1 = cv2.resize(img, (589, 474))
cv2.imwrite("BVP-logobk-rgb.jpg", img1)
