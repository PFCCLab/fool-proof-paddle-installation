echo "====== 欢迎使用 PaddleSeg 安装工具 ======"
echo "请确保在 PaddleSeg 目录下运行此脚本"
echo " "

echo "开始安装依赖，请等待"
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -v -e .

echo "恭喜安装成功，接下来进行验证安装测试"
python tools/predict.py \
    --config configs/quick_start/pp_liteseg_optic_disc_512x512_1k.yml \
    --model_path https://paddleseg.bj.bcebos.com/dygraph/optic_disc/pp_liteseg_optic_disc_512x512_1k/model.pdparams \
    --image_path docs/images/optic_test_image.jpg \
    --save_dir output/result

echo "❀ 若没有报错，则恭喜你完成  PaddleSeg 的安装！开始你的快乐使用吧 ❀"
