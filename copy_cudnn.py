import os
import shutil

CUDA_PATH = os.environ.get("CUDA_PATH")
pwd = os.getcwd()
src = f"{pwd}\cuda"
dst = f"{CUDA_PATH}"

shutil.copytree(src, dst, dirs_exist_ok=True)