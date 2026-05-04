# -v /dev:/dev의 의미 설명 및 왜 실행결과가 다른지 해석.

# mkdir ~/docker_workspace
# sudo docker run -it --rm --privileged \
# -p 8888:8888 \
# -v /dev:/dev \
# -v ~/docker_workspace:/workspace \
# --runtime=nvidia \
# my_torch:1.0 /bin/bash

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
else:
    print("카메라 연결 성공")

while True:
    ret, frame = cap.read()

    if not ret:
        print("프레임 읽기 실패")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# sudo docker run -it --rm --privileged \
# -p 8888:8888 \
# -v ~/docker_workspace:/workspace \
# --runtime=nvidia \
# my_torch:1.0 /bin/bash