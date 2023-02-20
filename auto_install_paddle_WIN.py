import os
import re
from importlib.util import find_spec

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
    print("https://developer.nvidia.com/downloads/c118-cudnn-windows-8664-880121cuda11-archivezip")
    CUDNN_if_zip = input("你是否已经下载好CUDNN压缩包，并将其移动到当前目录下 [Y/y]（完成后再选择）")
    if CUDNN_if_zip in ["Y","y","yes","YES"]:
        print("开始自动解压......")
        if os.path.isdir("cudnn-windows-x86_64-8.8.0.121_cuda11-archive/lib") and os.path.isdir("cudnn-windows-x86_64-8.8.0.121_cuda11-archive"):
            pass
        else:   
            os.system("powershell Expand-Archive -Path cudnn-windows-x86_64-8.8.0.121_cuda11-archive.zip -DestinationPath .")
        
        # 确保已经解压成功
        if os.path.isdir("cudnn-windows-x86_64-8.8.0.121_cuda11-archive/lib") and os.path.isdir("cudnn-windows-x86_64-8.8.0.121_cuda11-archive"):
            print("接下来开始安装")
            pwd = os.getcwd()
            src = '"'+f"{pwd}\cudnn-windows-x86_64-8.8.0.121_cuda11-archive\*"+'"'
            dst = '"`"'+f"{CUDA_PATH}"+'`""'
            print(src)
            # print(f"powershell Start-Process -FilePath powershell -Verb RunAs -Wait -ArgumentList \"Copy-Item\",\"-Path\",\".\cudnn-windows-x86_64-8.8.0.121_cuda11-archive\*\",\"-Recurse\",\'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\',\"-Force\"")
            # os.system(f"powershell Start-Process -FilePath powershell -Verb RunAs -Wait -ArgumentList \"Copy-Item\",\"-Path\",\".\cudnn-windows-x86_64-8.8.0.121_cuda11-archive\*\",\"-Recurse\",\'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\',\"-Force\"")
            print(f"powershell Start-Process -FilePath powershell -Verb RunAs -ArgumentList \"cp\",{src},\"-Recurse\",{dst}")
            os.system(f"powershell Start-Process -FilePath powershell -Verb RunAs -ArgumentList \"cp\",{src},\"-Recurse\",{dst}")
            # os.system(f"Copy-Item -Path {src} -Recurse {dst} -Force")
        else:
            print("未检测到CUDNN安装文件夹，自动解压失败，请自行解压放到文件夹下")
            print("当前目录下有的文件：")
            print(os.popen("dir").read())
            exit()

#环境变量设置


def paddle_install():
    os.system("pip install paddlepaddle-gpu==2.4.1.post112 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html")


def main_install():
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
    print("=====欢迎你使用 paddle windows 自动安装及环境配置工具=====\n\n")
    if_gpu = input("你是否想要安装GPU版本的paddle？[Y]，选择其他默认安装CPU版")
    if_paddle_install = find_spec("paddle")
    os.system('pip install --upgrade pip')
    
    if if_gpu in ["Y","y","yes","YES"]:
        print("开始安装GPU版本的paddle并进行环境配置安装")
        if if_paddle_install != None:
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
    os.system("powershell python -c 'import paddle;paddle.utils.run_check()'")
    print("如果未成功，请尝试退出终端后重新输入 powershell python -c 'import paddle;paddle.utils.run_check()' ")
    print("如果还发生异常，请联系开发人员，祝你使用愉快！")

def _do_install(pkgs):
    try:
        from pip._internal import main
    except Exception:
        from pip import main
    return main(['install'] + pkgs)

if __name__ == "__main__":
    main_install()
    
