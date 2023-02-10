#初始设置，配置你想要下载的paddle项目,不需要的注释即可
download_list=(
    #Paddle
    #PaddleSlim
    # Paddle-Lite
    #FastDeploy
    # PaddleX
    PaddleSpeech
    # PaddleClas
    PaddleDetection
    # PaddleSeg
    #PaddleOCR
    PaddleNLP
    # PaddleYOLO
    # PaddleVideo
    # PaddleGAN
)

#变量区
download_source="github"
download_way="http"
#执行区
echo "====== Welcome to use paddle-full-download-tools,please choose these options ======"
echo "====== 欢迎使用 paddle 全家桶下载工具，请根据以下选项选择自己的下载需求 ======"
echo ""
echo "Please choose the source where download paddle-files:"
echo "请选择 paddle 下载来源："
echo "Do you choose to get paddle from github? [Y/N], if you choose N, we will download from gitee"
echo "是否选择从 github 获取？[Y/N]，若选择N则从 gitee 获取下载来源"
echo ""

read -r -p "Are You Sure? [Y/N] " input

case $input in
    [yY][eE][sS]|[yY])
        echo "Yes,download from $download_source"
        ;;

    [nN][oO]|[nN])
        download_source="gitee"
        echo "No,download from $download_source"
        ;;

    *)
        echo "Invalid input...please tap Y or N"
        ;;
esac

echo ""
echo "Do you choose to download paddle by http? [Y/N], if you choose N we will download by ssh" 
echo "(Make sure you have set the github ssh)"
echo "是否选择用 http 方式下载？[Y/N]，若选择N则使用ssh获取（确保你已经绑定了 github ssh）"

read -r -p "Are You Sure? [Y/N] " input

case $input in
    [yY][eE][sS]|[yY])
        echo "Yes,download from $download_way"
        ;;

    [nN][oO]|[nN])
        download_way="ssh"
        echo "No,download from $download_way"
        ;;

    *)
        echo "Invalid input...please tap Y or N"
        ;;
esac


if [ $download_way == 'http' ]
then
    echo "Start download all files of paddle:[by $download_way]"
    for line in  ${download_list[@]}
    do
        git clone -depth=1 https://$download_source.com/PaddlePaddle/$line.git
    done
else
    echo "Start download all files of paddle:[by $download_way]"
    for line in  ${download_list[@]}
    do
        git clone -depth=1 git@$download_source.com:PaddlePaddle/$line.git
    done
fi
echo ""
echo "❀ Congratulations! All files download completely. Start your installation and use ❀"
echo "❀ 恭喜！全部文件已经下载完成，接下来请根据需求安装并使用。❀"












