import cv2
import matplotlib.pyplot as plt

img = cv2.imread("puppy.jpg", cv2.IMREAD_COLOR)

# BGR -> RGB로 변환
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 흑백 이미지로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# HSV 이미지로 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 원본 사진
plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("BGR Image")
plt.axis("off")

# BGR->RGB 이미지 출력
plt.subplot(2, 2, 2)
plt.imshow(img_rgb)
plt.title("RGB Image")
plt.axis("off")

# 그레이 이미지 출력
plt.subplot(2, 2, 3)
plt.imshow(gray, cmap='gray')
plt.title("Gray Image")
plt.axis("off")

# HSV 이미지 출력
plt.subplot(2, 2, 4)
plt.imshow(hsv)
plt.title("HSV")
plt.axis("off")

plt.show()