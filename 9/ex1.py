#명령어들만 나열. 가상환경 생성 및 numpy버전 확인
# python3 -m venv venv_test
# source ./venv_test/bin/activate
# python3 -m pip install --upgrade pip
# pip install numpy
# pip install numpy==1.24.4

# check_numpy_venv.py
import numpy as np

print("numpy 버전:", np.__version__)
print("numpy 설치 위치:", np.__file__)

# python3 check_numpy_venv.py
# deactivate