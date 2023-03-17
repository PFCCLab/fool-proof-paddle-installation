# fool-proof-paddle-installation
You can use this foolproof tool to download and install PADDLE automatically.

自动、快速的下载你想要下载的 Paddle 开源库，并且安装依赖。

目前已支持linux/windows环境下的 Paddle 和套件的安装。

## Call for Contributor
- 为linux版本加入paddleRS TS 3D REC VisualDL库的支持,给出 awesome-DeepLearning
- 在每一个库的后面加上一些字作为简介

## Linux环境下的安装
你只需要运行`source main.sh`然后根据提示操作即可.
【注意，如果你使用`bash main.sh`，那么在安装结束后请自行`source ~/.bashrc`一次才能看到`nvcc -V`的结果并成功运行paddle。

ubuntu20.04 22.04 wsl下完美测试通过。

## windows环境下的安装
你只需要在目录下运行`python main.py`然后根据提示操作即可。

AIstudio地址：
https://aistudio.baidu.com/aistudio/projectdetail/5448389
