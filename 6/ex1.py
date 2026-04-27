import cv2
import matplotlib.pyplot as plt

img = cv2.imread('cow.jpg')

plt.imshow(img)
plt.axis('off')
plt.show()

print("이미지 배열\n" , img)