import cv2
import matplotlib.pyplot as plt

img = cv2.imread("cat.jpg", cv2.IMREAD_COLOR)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

resized = cv2.resize(img, (100, 200))

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

trans = cv2.resize(img, (200, 100))
trans = cv2.rotate(trans, cv2.ROTATE_90_COUNTERCLOCKWISE)

# 원본 사진
plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

# 이미지 크기 변환
plt.subplot(2, 2, 2)
plt.imshow(resized)
plt.title("RGB Image")
plt.axis("off")

# 이미지 회전
plt.subplot(2, 2, 3)
plt.imshow(rotated)
plt.title("Rotated")
plt.axis("off")

# 이미지 변환 + 회전
plt.subplot(2, 2, 4)
plt.imshow(trans)
plt.title("trans")
plt.axis("off")

plt.show()