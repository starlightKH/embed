# 명령어는 주석처리, conda 설치 및 numpy 버전 확인
# wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh
# bash Miniforge3-Linux-aarch64.sh
# source ~/.bashrc
# conda create -n conda_test python=3.8
# conda install numpy
# conda install numpy=1.23
import numpy as np

print("numpy 버전:", np.__version__)
print("numpy 설치 위치:", np.__file__)

# python3 check_numpy_conda.py
# conda deactivate