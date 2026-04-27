import cv2
import matplotlib.pyplot as plt

img = cv2.imread("horse.jpg", cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 1번: 크기 변환
img1 = cv2.resize(img_rgb, (300, 100))

# 2번: 흑백 변환
img2 = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# 3번: 90도 회전
img3 = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)

# 4번: 크기 변환 + 흑백 변환
img4 = cv2.resize(img_rgb, (100, 200))
img4 = cv2.cvtColor(img4, cv2.COLOR_RGB2GRAY)

plt.subplot(2, 2, 1)
plt.imshow(img1)
plt.title("1")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title("2")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(img3)
plt.title("3")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(img4, cmap='gray')
plt.title("4")
plt.axis("off")

plt.show()