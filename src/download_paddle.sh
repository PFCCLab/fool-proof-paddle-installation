#变量区
download_source="github"
download_way="http"

PADDLE_SROUCE=(
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

# 执行区

echo "====== Welcome to use paddle-full-download-tools,please choose these options ======"
echo "====== 欢迎使用 paddle 全家桶下载工具，请根据以下选项选择自己的下载需求 ======"
echo ""

echo '''
请选择你想要下载的仓库,输入对应字母:
如我想下载 Paddle/PaddleSlim/Paddle-Lite 只需输入ABC即可,中间无需空格.
   A - Paddle
   B - PaddleSlim
   C - Paddle-Lite
   D - FastDeploy
   E - PaddleX
   F - PaddleSpeech
   G - PaddleClas
   H - PaddleDetection
   I - PaddleSeg
   J - PaddleOCR
   K - PaddleNLP
   L - PaddleYOLO
   M - PaddleVideo
   N - PaddleGAN
'''

echo "请输入对应字母:"
read str
if [[ $str == *"A"* ]]; then    
  download_list+=(${PADDLE_SROUCE[0]})
fi
if [[ $str == *"B"* ]]; then
  download_list+=(${PADDLE_SROUCE[1]})
fi
if [[ $str == *"C"* ]]; then
  download_list+=(${PADDLE_SROUCE[2]})
fi
if [[ $str == *"D"* ]]; then
  download_list+=(${PADDLE_SROUCE[3]})
fi
if [[ $str == *"E"* ]]; then
  download_list+=(${PADDLE_SROUCE[4]})
fi
if [[ $str == *"F"* ]]; then
  download_list+=(${PADDLE_SROUCE[5]})
fi
if [[ $str == *"G"* ]]; then
  download_list+=(${PADDLE_SROUCE[6]})
fi
if [[ $str == *"H"* ]]; then
  download_list+=(${PADDLE_SROUCE[7]})
fi
if [[ $str == *"I"* ]]; then
  download_list+=(${PADDLE_SROUCE[8]})
fi
if [[ $str == *"J"* ]]; then
  download_list+=(${PADDLE_SROUCE[9]})
fi
if [[ $str == *"K"* ]]; then
  download_list+=(${PADDLE_SROUCE[10]})
fi
if [[ $str == *"L"* ]]; then
  download_list+=(${PADDLE_SROUCE[11]})
fi
if [[ $str == *"M"* ]]; then
  download_list+=(${PADDLE_SROUCE[12]})
fi
if [[ $str == *"N"* ]]; then
  download_list+=(${PADDLE_SROUCE[13]})
fi


echo "现在开始下载以下仓库:"
for i in "${download_list[@]}"
do
    echo "$i" 
done

echo " "
echo "Please choose the source where download paddle-files:"
echo "请选择下载来源："
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
        git clone --depth=1 https://$download_source.com/PaddlePaddle/$line.git
    done
else
    echo "Start download all files of paddle:[by $download_way]"
    for line in  ${download_list[@]}
    do
        git clone --depth=1 git@$download_source.com:PaddlePaddle/$line.git
    done
fi
echo ""
echo "❀ Congratulations! All files download completely. Start your installation and use ❀"
echo "❀ 恭喜！全部文件已经下载完成，接下来请根据需求安装并使用。❀"












