import os
import re
from importlib.util import find_spec
import src.paddle_tools
import sys

download_list=[
    "PaddleSlim",
    "FastDeploy",
    "PaddleSpeech",
    "PaddleClas",
    "PaddleDetection",
    "PaddleSeg",
    "PaddleOCR",
    "PaddleNLP",
    "PaddleVideo",
    "PaddleGAN",
]

def cuda_version_detect():
    print("接下来检查CUDA驱动情况：")
    command = 'nvidia-smi | findstr CUDA'
    result = os.popen(command).read()
    pattern = r"CUDA Version: (\d+\.\d+)"
    if (len(result)==0):
        print("\n没有检测到驱动，请检查！")
        exit()
    else:
        match = re.search(pattern, result)
        if match:
            cuda_version=match.group(1)
        else:
            print("CUDA驱动可能存在问题，请联系开发")
            exit()
        if float(cuda_version) < 11.2:
            print("你的CUDA驱动版本过低，无法支持最新paddle，请重新安装大于11.2的版本！")   
            exit()

def cuda_install():
    _CUDA_if_install = input("你是否需要安装CUDA？ 输入[Y/y]进入安装，输入其他默认已安装")
    if _CUDA_if_install in ["Y","y","yes","YES"]:
        command = 'nvcc -V'
        cuda_result = os.popen(command).read()
        if (len(cuda_result)==0) :
            print("开始下载 CUDA，请等待.......")
        else:
            print("已检测到你已经安装CUDA! 接下来开始下载并安装CUDNN")
            return 
    else:
        command = 'nvcc -V'
        cuda_result = os.popen(command).read()
        if (len(cuda_result)==0) :
            print("未检测到你已经安装CUDA! 接下来开始下载并安装CUDA")
        else:
            return     
    
    url = "https://developer.download.nvidia.com/compute/cuda/11.2.2/local_installers/cuda_11.2.2_461.33_win10.exe"
    filePath = "cuda_11.2.2_461.33_win10.exe"
    command = f"powershell Invoke-WebRequest -Uri {url} -OutFile {filePath}"
    os.system(command)
    if os.path.isfile("cuda_11.2.2_461.33_win10.exe"):
        print("接下来开始安装")
        os.system("cuda_11.2.2_461.33_win10.exe")
        print("=======注意======")
        print("由于 Windows 系统特性，CUDA安装结束后你需要关闭当前终端并重开，否则无法进入进一步安装")
        print("如果你成功重启终端，再次运行该脚本后会自动跳过CUDA安装")

    else:
        print("未检测到CUDA安装文件，请重新运行下载或手动下载后安装")
        print("https://developer.download.nvidia.com/compute/cuda/11.2.2/local_installers/cuda_11.2.2_461.33_win10.exe")
        exit()

    
    CUDA_if_install = input("请在安装完成后继续，你是否已经安装好CUDA [Y/y]")
    if CUDA_if_install in ["Y","y","yes","YES"]:
        command = 'nvcc -V'
        result = os.popen(command).read()
        if (len(result)==0) :
            print("CUDA未检测到！请查看是否安装CUDA，或联系开发人员")
            print("\n")
            print(r"如果在 C:\Program Files\NVIDIA GPU Computing Toolkit 目录下有 CUDA 文件夹")
            print("请你确保已重启所有终端，或重新启动即可解决问题。")
            exit()
        print("恭喜你安装完CUDA，请继续安装CUDNN")
    else:
        print("输入错误！")
        exit()

def cudnn_install():
    CUDA_PATH = os.environ.get("CUDA_PATH")

    print("\n请ctrl+左键点击网页自行登录并下载CUDNN并把压缩包放到当前目录下：")
    print("https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.2.1.32/11.3_06072021/cudnn-11.3-windows-x64-v8.2.1.32.zip")
    CUDNN_if_zip = input("你是否已经下载好CUDNN压缩包，并将其移动到当前目录下 [Y/y]（完成后再选择，否则直接进入下一步）")
    if CUDNN_if_zip in ["Y","y","yes","YES"]:
        print("开始自动解压......")
        if os.path.isdir("cuda/lib") and os.path.isdir("cuda"):
            pass
        else:   
            os.system("powershell Expand-Archive -Path cudnn-11.3-windows-x64-v8.2.1.32.zip -DestinationPath .")
        
        # 确保已经解压成功
        if os.path.isdir("cuda/lib") and os.path.isdir("cuda"):
            print("接下来开始安装")
            os.system("powershell Start-Process -FilePath \"python\" -Verb RunAs -ArgumentList \"copy_cudnn.py\"")
            
        else:
            print("未检测到CUDNN安装文件夹，自动解压失败，请自行解压放到文件夹下")
            print("当前目录下有的文件：")
            print(os.popen("dir").read())
            exit()

#环境变量设置


def paddle_install():
    os.system("pip install paddlepaddle-gpu==2.4.1.post112 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html")


def main_install():
    if_gpu = input("你是否想要安装GPU版本的paddle？[Y]，选择其他默认安装CPU版")
    if_paddle_install = True
    try:
        import paddle
    except:
        if_paddle_install = False
    
    os.system(f'{sys.executable} -m pip install --upgrade pip')
    
    if if_gpu in ["Y","y","yes","YES"]:
        print("开始安装GPU版本的paddle并进行环境配置安装")
        if if_paddle_install:
            print("检测到 paddle 已安装,进入CUDA安装环节")
        else:
            paddle_install()
    
    else:
        print("开始安装CPU版本的paddle")
        _do_install(["paddlepaddle"])
        print("安装CPU版paddle完毕！请开始你的使用之旅")
        exit()
    cuda_version_detect()
    cuda_install()
    cudnn_install()
    print("安装GPU版paddle完毕！请开始你的使用之旅")
    print("====最后验证安装是否成功====")
    os.system("python -c 'import paddle;paddle.utils.run_check()'")
    print("如果未成功，请尝试退出终端后重新输入 python -c 'import paddle;paddle.utils.run_check()' ")
    print("如果还发生异常，请联系开发人员，祝你使用愉快！")

def _do_install(pkgs):
    try:
        from pip._internal import main
    except Exception:
        from pip import main
    return main(['install'] + pkgs+["-i"]+["https://pypi.tuna.tsinghua.edu.cn/simple"])

# 套件的下载与安装

def download_PaddlePaddle():
    osresult = os.system('start "" "%ProgramFiles%\Git\git-bash.exe" -c "echo 1 "')
    if osresult ==1:
        print("未安装git bash或git bash安装地址不对，如果一路next仍报错请联系开发人员")

        if not os.path.isfile(""):
            print("开始下载git bash安装程序")
            url = "https://registry.npmmirror.com/-/binary/git-for-windows/v2.39.0.windows.2/Git-2.39.0.2-64-bit.exe"
            filePath = "Git-2.39.0.2-64-bit.exe"
            command = f"powershell Invoke-WebRequest -Uri {url} -OutFile {filePath}"
            os.system(command)

        print("开始安装git bash, 请一路next即可")
        os.system("Git-2.39.0.2-64-bit.exe")
        print("安装完毕后，请关闭当前终端，重新运行即可启动一键下载功能！")
    
    os.system('start "" "%ProgramFiles%\Git\git-bash.exe" -c "bash ./src/download_paddle.sh "')
    print("恭喜下载完毕，请开始接下来的安装！")
    
    

def install_PaddlePaddle():
    # 批量导入模块方法
    install_dict = {}
    for i in download_list:
        install_dict[i] = getattr(src.paddle_tools,i)

    print("开始扫描当前目录下的套件......")
    install_list = []
    dirs = os.listdir(".")
    for i in dirs:
        if i in download_list:
            install_list.append(i)
    
    print("即将安装以下仓库的环境到本虚拟环境：")
    if install_list == []:
        print("未搜索到任何库，请下载后重试！")
        print("当前路径下的文件为：",os.listdir("."))
        exit()

    for i in install_list:
        print(i)
        install_dict[i]()



if __name__ == "__main__":
    os.system("cls")
    welcome_str = """
      ___         ___          _____         _____                        ___     
     /  /\       /  /\        /  /::\       /  /::\                      /  /\    
    /  /::\     /  /::\      /  /:/\:\     /  /:/\:\                    /  /:/_   
   /  /:/\:\   /  /:/\:\    /  /:/  \:\   /  /:/  \:\   ___     ___    /  /:/ /\  
  /  /:/~/:/  /  /:/~/::\  /__/:/ \__\:| /__/:/ \__\:| /__/\   /  /\  /  /:/ /:/_ 
 /__/:/ /:/  /__/:/ /:/\:\ \  \:\ /  /:/ \  \:\ /  /:/ \  \:\ /  /:/ /__/:/ /:/ /
 \  \:\/:/   \  \:\/:/__\/  \  \:\  /:/   \  \:\  /:/   \  \:\  /:/  \  \:\/:/ /:/
  \  \::/     \  \::/        \  \:\/:/     \  \:\/:/     \  \:\/:/    \  \::/ /:/ 
   \  \:\      \  \:\         \  \::/       \  \::/       \  \::/      \  \:\/:/  
    \  \:\      \  \:\         \__\/         \__\/         \__\/        \  \::/   
     \__\/       \__\/                                                   \__\/    

    """
    print(welcome_str)
    print("欢迎你使用 Windows-Paddle 全家桶一键下载&CUDA环境配置及套件安装工具！")
    print("windows环境下请使用python3.7安装！推荐使用anaconda或miniconda：")
    print("https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda3-py37_23.1.0-1-Windows-x86_64.exe")
    print("请选择:(输入1,2或者3)")
    print("（1）下载 Paddle 系列开源库\n（2）安装 Paddle 及系列开源库\n（3）退出程序")

    while True:
        option = input()
        if option == "1":
            os.system("cls")
            download_PaddlePaddle()
            exit()
        elif option =="2":
            os.system("cls")
            print ("请选择要安装的内容:(输入1,2或者3)")
            print ("警告：请在安装完 Paddle 后再安装套件")
            print ("（1）一键安装 Paddle 及CUDA环境\n（2）一键安装 Paddle 套件\n（3）退出程序")
            while True:
                option = input()
                if option == "1":
                    os.system("cls")
                    main_install()
                    exit()
                elif option =="2":
                    os.system("cls")
                    install_PaddlePaddle()
                    exit()
                elif option =="3":
                    os.system("cls")
                    print("再见，祝你有美好的一天！")
                    exit()
                else:
                    continue
        elif option =="3":
            os.system("cls")
            print("再见，祝你有美好的一天！")
            exit()
        else:
            continue
    
    
