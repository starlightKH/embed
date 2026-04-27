import cv2
import matplotlib.pyplot as plt

# 이미지 불러오기
img = cv2.imread("cow.jpg")

# BGR 기준 빨간색 = [0, 0, 255]
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img[540:550, 890:990, :] = [255, 0, 0]
img[540:1200, 940:950, :] = [0, 255, 0]
img[1190:1200, 890:990, :] = [0, 0, 255]
img[540:1200, 890:900, :] = [100, 100, 100]

plt.imshow(img)
plt.axis("off")
plt.show()