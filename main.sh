#!/bin/bash
# This is a simple shell script with a TUI interface
# Define the options
clear 
echo '''
      ___         ___          _____         _____                        ___     
     /  /\       /  /\        /  /::\       /  /::\                      /  /\    
    /  /::\     /  /::\      /  /:/\:\     /  /:/\:\                    /  /:/_   
   /  /:/\:\   /  /:/\:\    /  /:/  \:\   /  /:/  \:\   ___     ___    /  /:/ /\  
  /  /:/~/:/  /  /:/~/::\  /__/:/ \__\:| /__/:/ \__\:| /__/\   /  /\  /  /:/ /:/_ 
 /__/:/ /:/  /__/:/ /:/\:\ \  \:\ /  /:/ \  \:\ /  /:/ \  \:\ /  /:/ /__/:/ /:/ /\
 \  \:\/:/   \  \:\/:/__\/  \  \:\  /:/   \  \:\  /:/   \  \:\  /:/  \  \:\/:/ /:/
  \  \::/     \  \::/        \  \:\/:/     \  \:\/:/     \  \:\/:/    \  \::/ /:/ 
   \  \:\      \  \:\         \  \::/       \  \::/       \  \::/      \  \:\/:/  
    \  \:\      \  \:\         \__\/         \__\/         \__\/        \  \::/   
     \__\/       \__\/                                                   \__\/    


'''
echo "欢迎你使用 Paddle 全家桶一键下载&CUDA环境配置及套件安装工具！"
options=("下载 Paddle 系列开源库" "安装 Paddle 及系列开源库" "退出程序")
# Display the menu
echo "请选择:(输入1,2或者3)"

download_list=(
    Paddle
    PaddleSlim
    Paddle-Lite
    FastDeploy
    PaddleX
    PaddleSpeech
    PaddleClas
    PaddleDetection
    PaddleSeg
    PaddleOCR
    PaddleNLP
    PaddleYOLO
    PaddleVideo
    PaddleGAN
)

function paddle_install()
{
clear
echo "请选择要安装的内容:(输入1,2或者3)"
echo "警告：请在安装完 Paddle 后再安装套件"
echo " "
options2=("一键安装 Paddle 及CUDA环境" "一键安装 Paddle 套件" "退出程序")
select optt in "${options2[@]}"
do
    case $optt in
    "一键安装 Paddle 及CUDA环境")
        cp ./src/auto_install_paddle.sh  ./
        bash auto_install_paddle.sh
        rm ./auto_install_paddle.sh
        source ~/.bashrc
        echo "验证是否成功，打印nvcc信息"
        nvcc -V
        echo "如果没有打印，请在程序结束后自行输入 source ~/.bashrc"
        echo " "
        echo "====最后验证安装是否成功，请你进入安装环境下运行下列命令行===="
        echo "python3 -c 'import paddle;paddle.utils.run_check()'"
        echo " "        
        echo '''如果成功，你能看到如下显示:
PaddlePaddle works well on 1 GPU.
PaddlePaddle works well on 1 GPUs.
PaddlePaddle is installed successfully! Lets start deep learning with PaddlePaddle now.
             '''
        echo "如发现错误，请联系开发人员"
        echo " "
        echo "❀ 恭喜你完成环境配置，接下来请根据喜好安装 paddle 套件"
        echo " "
        break
        ;;
    "一键安装 Paddle 套件")
        echo "开始扫描当前目录下的套件......"
        str_ls=$(ls)
        for i in "${download_list[@]}"
        do
            if [[ $i == "Paddle" ]]; then  
            continue
            fi
            if [[ $i == "PaddleX" ]]; then  
            continue
            fi
            if [[ $i == "PaddleX" ]]; then  
            continue
            fi
            if [[ $i == "PaddleYOLO" ]]; then  
            continue
            fi        
            if [[ $str_ls == *$i* ]]; then  
            install_list+=($i)
            fi
        done
        echo "即将安装以下仓库的环境到本虚拟环境："
        for i in "${install_list[@]}"
        do
            echo "$i" 
        done

        DIR_PWD=$(pwd)
        for i in "${install_list[@]}"
        do
            cd $DIR_PWD
            cp ./src/"$i.sh"  ./"$i"
            cd $i
            bash "$i.sh"
        done

        echo "恭喜你安装完所有套件，开始快乐的使用吧！"
        break        
        ;;       
    "退出程序")
        exit 0
    esac     
done
}

select opt in "${options[@]}"
do
    case $opt in
        "下载 Paddle 系列开源库")
            bash ./src/download_paddle.sh
            break
            ;;
        "安装 Paddle 及系列开源库")
            paddle_install
            break
            ;;
        "退出程序")
            echo "再见，祝你有美好的一天！"
            exit 0
            ;;
        *) echo "输入错误,请输入对应选项";;
    esac
done


