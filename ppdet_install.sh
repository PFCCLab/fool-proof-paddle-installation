echo "====== 欢迎使用 PaddleDetection 安装工具 ======"
echo "请确保在 PaddleDetection 目录下运行此脚本"
echo " "

echo "开始安装依赖，请等待"
pip install -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple

echo "开始编译安装paddledet"
python setup.py install

echo "恭喜安装成功，接下来进行验证安装测试（出现OK即可）"
python ppdet/modeling/tests/test_architectures.py

echo "最后在CPU上进行预测测试"
python tools/infer.py -c configs/ppyolo/ppyolo_r50vd_dcn_1x_coco.yml \
                      -o use_gpu=false weights=https://paddledet.bj.bcebos.com/models/ppyolo_r50vd_dcn_1x_coco.pdparams \
                      --infer_img=demo/000000014439.jpg

echo "❀ 恭喜你完成 PaddleDetection 的安装，请前往 output 文件夹下查看 000000014439.jpg文件是否包含预测框 ❀"