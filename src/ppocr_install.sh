echo "====== 欢迎使用 PaddleOCR 安装工具 ======"
echo "请确保在 PaddleOCR 目录下运行此脚本"
echo " "

echo "开始安装依赖，请等待"
pip install "paddleocr>=2.0.1" -i https://pypi.tuna.tsinghua.edu.cn/simple

echo "恭喜安装成功，接下来进行验证安装测试"
echo "是否选择使用 GPU 验证？[Y/N]，若选择N则使用 CPU 验证"

read -r -p "Are You Sure? [Y/N] " input

case $input in
    [yY][eE][sS]|[yY])
        echo "Yes,使用 GPU 验证"
        paddleocr --image_dir ./doc/imgs/11.jpg --use_angle_cls true --use_gpu true
        ;;

    [nN][oO]|[nN])
        download_source="gitee"
        echo "No,使用 CPU 验证"
        paddleocr --image_dir ./doc/imgs/11.jpg --use_angle_cls true --use_gpu false
        ;;

    *)
        echo "Invalid input...please tap Y or N"
        ;;
esac


echo "❀ 若出现检测结果，则恭喜你完成  PaddleOCR 的安装！开始你的快乐使用吧 ❀"
