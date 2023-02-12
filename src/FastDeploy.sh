echo "====== 欢迎使用 FastDeploy 安装工具 ======"
echo "请确保在 FastDeploy 目录下运行此脚本"
echo " "

echo "开始安装依赖，请选择你想要安装的版本"
echo "是否选择使用 GPU 版本？[Y/N]，若选择N则使用 CPU 版本"

read -r -p "Are You Sure? [Y/N] " input

case $input in
    [yY][eE][sS]|[yY])
        echo "Yes,安装 GPU 版本"
        pip install numpy opencv-python fastdeploy-gpu-python -f https://www.paddlepaddle.org.cn/whl/fastdeploy.html
        ;;

    [nN][oO]|[nN])
        download_source="gitee"
        echo "No,安装 CPU 版本"
        pip install numpy opencv-python fastdeploy-python -f https://www.paddlepaddle.org.cn/whl/fastdeploy.html
        ;;

    *)
        echo "Invalid input...please tap Y or N"
        ;;
esac

echo " "
echo "接下来验证安装，请稍后......"
wget https://bj.bcebos.com/paddlehub/fastdeploy/ppyoloe_crn_l_300e_coco.tgz
tar xvf ppyoloe_crn_l_300e_coco.tgz
wget https://gitee.com/paddlepaddle/PaddleDetection/raw/release/2.4/demo/000000014439.jpg

python -c "\
import cv2;\
import fastdeploy.vision as vision;\
model = vision.detection.PPYOLOE('ppyoloe_crn_l_300e_coco/model.pdmodel',\
                                 'ppyoloe_crn_l_300e_coco/model.pdiparams',\
                                 'ppyoloe_crn_l_300e_coco/infer_cfg.yml');\
im = cv2.imread('000000014439.jpg');\
result = model.predict(im);\
print(result);\
vis_im = vision.vis_detection(im, result, score_threshold=0.5);\
cv2.imwrite('vis_image.jpg', vis_im);"

echo "运行完毕，你可以查看当前目录下的图片是否显示出检测结果"
ls | grep vis_image
echo "❀ 若出现检测结果，则恭喜你完成 FastDeploy 的安装！开始你的快乐使用吧 ❀"
