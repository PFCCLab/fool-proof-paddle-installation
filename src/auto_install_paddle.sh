#!/bin/bash
echo "====== 欢迎使用 Paddle 全自动安装与环境配置工具 ======"

echo "初始环境配置中，请输入密码......"
# sudo apt update
sudo apt -y install wget gcc g++  python3-pip
python3 -m pip3 install --upgrade pip3
python3 -m pip install --upgrade pip

echo "配置完毕，接下来开始GPU库的安装，请确保你已经安装好驱动"

nvidia-smi

echo "上述出现详细信息则正常，若出现错误，请检查你的GPU驱动"
echo "请问你是否选择安装GPU版本的 Paddle？[Y/N]，若选择N则安装CPU版本"
read -r -p "Are You Sure? [Y/N] " input
 
case $input in
    [yY][eE][sS]|[yY])
        echo "接下来开始 Paddle GPU 版本的安装（默认安装 post11.2 的版本）"
        python_version=$(python -V)
        # Extract the number
        number=`echo $python_version | cut -d'.' -f2`
        if [ $number -eq 10 ]
        then
            wget -c https://paddle-wheel.bj.bcebos.com/2.4.1/linux/linux-gpu-cuda11.2-cudnn8-mkl-gcc8.2-avx/paddlepaddle_gpu-2.4.1.post112-cp310-cp310-linux_x86_64.whl
            pip3 install paddlepaddle_gpu-2.4.1.post112-cp310-cp310-linux_x86_64.whl -i https://pypi.tuna.tsinghua.edu.cn/simple
        elif [ $number -eq 9 ]
        then
            wget -c https://paddle-wheel.bj.bcebos.com/2.4.1/linux/linux-gpu-cuda11.2-cudnn8-mkl-gcc8.2-avx/paddlepaddle_gpu-2.4.1.post112-cp39-cp39-linux_x86_64.whl
            pip3 install paddlepaddle_gpu-2.4.1.post112-cp39-cp39-linux_x86_64.whl -i https://pypi.tuna.tsinghua.edu.cn/simple
        elif [ $number -eq 8 ]
        then
            wget -c https://paddle-wheel.bj.bcebos.com/2.4.1/linux/linux-gpu-cuda11.2-cudnn8-mkl-gcc8.2-avx/paddlepaddle_gpu-2.4.1.post112-cp38-cp38-linux_x86_64.whl
            pip3 install paddlepaddle_gpu-2.4.1.post112-cp38-cp38-linux_x86_64.whl -i https://pypi.tuna.tsinghua.edu.cn/simple
        elif [ $number -eq 7 ]
        then
            wget -c https://paddle-wheel.bj.bcebos.com/2.4.1/linux/linux-gpu-cuda11.2-cudnn8-mkl-gcc8.2-avx/paddlepaddle_gpu-2.4.1.post112-cp37-cp37m-linux_x86_64.whl
            pip3 install paddlepaddle_gpu-2.4.1.post112-cp37-cp37m-linux_x86_64.whl -i https://pypi.tuna.tsinghua.edu.cn/simple
        elif [ $number -eq 6 ]
        then
            wget -c https://paddle-wheel.bj.bcebos.com/2.4.1/linux/linux-gpu-cuda11.2-cudnn8-mkl-gcc8.2-avx/paddlepaddle_gpu-2.4.1.post112-cp36-cp36m-linux_x86_64.whl
            pip3 install paddlepaddle_gpu-2.4.1.post112-cp36-cp36m-linux_x86_64.whl -i https://pypi.tuna.tsinghua.edu.cn/simple
        else
            echo "您的 python 版本不支持！请确保python版本在3.6到3.10，若有疑问请联系开发者"
            echo "您现在的python版本为：$number"
            exit 0
        fi

        python3 -m pip3 install paddlepaddle-gpu==2.4.1.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
        echo " "
        echo "Paddle GPU 版本安装完毕，接下来进行依赖库的安装"
        echo " "
        ;;

    [nN][oO]|[nN])
        python3 -m pip3 install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
        echo "❀ 恭喜你完成 Paddle CPU 版本的安装，接下来开启愉快的使用把！"
        exit 0
        ;;

    *)
        echo "错误的输入，请输入Y或者N"
        exit 0
        ;;
esac

echo "若上述wget下载失败，请重新运行程序会自动断线重连，有其他问题请联系开发者"

echo "接下来进行 CUDA 的安装，你是否已经安装好 CUDA【注意，安装的CUDA必须小于12】？[Y/N]"

read -r -p "Are You Sure? [Y/N] " input
case $input in
    [yY][eE][sS]|[yY])
        echo "是，直接进入 CuDNN 安装环节"
        ;;

    [nN][oO]|[nN])
        echo "否，将会安装 CUDA"

        CUDA_VERSION=$(nvidia-smi | grep CUDA | grep -oP '(?<=CUDA Version: )[^ ]+')
        #判空
        if [ -z "$CUDA_VERSION" ] || [ -z "${CUDA_VERSION// }" ]; then
        echo "你的显卡驱动似乎存在问题，运行nvidia-smi结果如下："
        nvidia-smi
        echo "如果出现错误请重启，如果正常显示请联系开发人员"
        fi

        check_results=`"gcc" "-dumpversion"`
        gcc_version=11

        IF_PROBLEM1=$(a=$CUDA_VERSION b=11.2;expr $a \< $b)
        if [ $IF_PROBLEM1 -eq 1 ]
        then
        echo "你的显卡驱动存在问题或版本有问题，请截图反馈开发人员"
        nvidia-smi
        exit 0
        fi
        
        if [ $check_results -lt $gcc_version ]
        then
            # gcc 小于 11，通常为9，可以编译任意版本
            echo "将会安装 cuda-11.2 运行时"
            echo "【警告！！如果里面看到了安装驱动的选项如 [x] 410.xxx】"
            echo "【请选择后，按回车键取消至 [ ] 410.xxx，避免让电脑黑屏！】"
            wget -c https://developer.download.nvidia.com/compute/cuda/11.2.2/local_installers/cuda_11.2.2_460.32.03_linux.run
            echo " "
            echo "================================="
            echo "此处打开和安装结束都需要一些时间...根据机器和网络有所不同可能需要几分钟，请耐心等待"
            echo "================================="
            echo " "
            sudo sh cuda_11.2.2_460.32.03_linux.run
        else
            # gcc 大于等于 11 ，只编译cuda11.4、11.5以上的版本
            echo "你的gcc版本为$gcc_version 只能安装CUDA>=11.4的版本"
            IF_PROBLEM2=$(a=$CUDA_VERSION b=11.4;expr $a \< $b)
            if [ $IF_PROBLEM2 -eq 1 ]
            then
                echo "你的驱动CUDA兼容版本太低！请升级至少至11.4以上，若有疑问请联系开发人员"
                exit 0 
            fi

            echo "【警告！！如果里面看到了安装驱动的选项如 [x] 410.xxx】"
            echo "【请选择后，按回车键取消至 [ ] 410.xxx，避免让电脑黑屏！】"
            wget -c https://developer.download.nvidia.com/compute/cuda/11.4.4/local_installers/cuda_11.4.4_470.82.01_linux.run
            echo " "
            echo "================================="
            echo "此处打开和安装结束都需要一些时间...根据机器和网络有所不同可能需要几分钟，请耐心等待"
            echo "================================="
            echo " "
            sudo sh cuda_11.4.4_470.82.01_linux.run
        fi
        ;;

    *)
        echo "错误的输入，请输入Y或者N"
        exit 0
        ;;
esac
echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
echo " "
ls /usr/local | grep cuda
echo " "
echo "若上述出现CUDA，则CUDA安装完成，如果没有出现，请检查是否运行了CUDA安装脚本！"
echo " "
echo "恭喜你来到最后一步，接下来将安装CUDNN与配置环境"
echo "请点击下列网址下载CUDNN库，随后放到和脚本一致的路径下"
echo "https://developer.nvidia.com/downloads/c118-cudnn-linux-8664-87084cuda11-archivetarz"
echo " "
echo "是否已放到脚本同路径下？[Y] 请在放置后再选择Y！否则会出错"

read -r -p "Are You Sure? [Y/N] " input

case $input in
    [yY][eE][sS]|[yY])
        echo "是，将会安装 CUDNN"
        if [ ! -f "cudnn-linux-x86_64-8.7.0.84_cuda11-archive.tar.xz" ]; then
        ls | grep cudnn-linux
        echo "错误，未发现CUDNN安装包，请重试！"
        echo "你现在处在的目录为："
        pwd
        echo " "
        echo "你当前目录下所拥有的文件："
        ls
        exit 0
        fi

        ls | grep cudnn-linux
        echo "成功发现安装包，开始安装......"

        if [ $(du -b cudnn-linux-x86_64-8.7.0.84_cuda11-archive.tar.xz | awk '{print $1}') -gt 800000000 ]; then
           echo " "
        else
        echo "cudnn安装文件大小小于800mb，可能下载有问题（最终在850左右），请重新下载！"
        exit 0
        fi
        ;;

    *)
        echo "错误的输入，请输入Y"
        exit 0
        ;;
esac

echo "开始解压......"
tar -xvf cudnn*.tar.xz
echo " "
echo "开始安装......"
cd cudnn*-archive

if [ -d "lib" ] || [ -d "include" ]; then
    echo " "
else
    echo "未发现安装依赖文件夹，可能解压出错或进入错误的文件夹，当前所在目录："
    pwd
    echo "请使安装文件夹内只有一份cudnn安装文件，否则会出错，如果还有问题请联系研发人员"
    exit 0
fi

sudo cp lib/* /usr/local/cuda/lib64/
sudo cp include/* /usr/local/cuda/include/
echo " "
echo "验证是否安装成功（此时你应该看到有多个CUDNN_MAJOR类似字样）"
cat /usr/local/cuda/include/cudnn_version.h | grep CUDNN_MAJOR -A 2
echo 'export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/targets/x86_64-linux/lib' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/targets/x86_64-linux/lib/stubs/' >> ~/.bashrc

