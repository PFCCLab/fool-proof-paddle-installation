# fool-proof-paddle-installation
You can use this foolproof tool to download and install PADDLE automatically.

自动、快速的下载你想要下载的 Paddle 开源库，并且安装依赖。

目前已支持linux环境下的 Paddle 和套件的安装。

你只需要运行`source main.sh`然后根据提示操作即可.
【注意，如果你使用`bash main.sh`，那么在安装结束后请自行`source ~/.bashrc`一次才能看到`nvcc -V`的结果并成功运行paddle。

ubuntu20.04 22.04 wsl下完美测试通过。

AIstudio地址：
https://aistudio.baidu.com/aistudio/projectdetail/5448389

之后会迭代加入windows的一键下载和配置工具
