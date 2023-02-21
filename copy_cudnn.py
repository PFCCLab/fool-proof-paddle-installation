import os
import shutil

CUDA_PATH = os.environ.get("CUDA_PATH")
pwd = os.getcwd()
src = f"{pwd}\cudnn-windows-x86_64-8.8.0.121_cuda11-archive"
dst = f"{CUDA_PATH}"

shutil.copytree(src, dst, dirs_exist_ok=True)