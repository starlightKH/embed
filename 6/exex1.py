import cv2
import matplotlib.pyplot as plt

img = cv2.imread("horse.jpg", cv2.IMREAD_COLOR)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
resized = cv2.resize(img_rgb, (300, 100))

cv2.imwrite("new_horse.jpg", cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))

plt.imshow(resized)
plt.title("new_horse.jpg")
plt.axis("off")
plt.show()