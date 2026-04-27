import cv2
import matplotlib.pyplot as plt

# 1. 이미지 불러오기 (컬러)
img = cv2.imread("cat.jpg")

# 2. 흑백(Grayscale)으로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. 흑백 이미지 저장
cv2.imwrite("gray_image.jpg", gray)

# 4. 저장된 이미지 다시 불러오기
loaded_img = cv2.imread("gray_image.jpg")

# 5. 이미지 출력
plt.imshow(loaded_img, cmap='gray')
plt.title("Loaded Grayscale Image")
plt.axis("off")
plt.show()