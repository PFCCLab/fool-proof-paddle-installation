echo "====== 欢迎使用 PaddleClas 安装工具 ======"
echo "请确保在 PaddleClas 目录下运行此脚本"
echo " "

echo "开始安装依赖，请等待"
pip install paddleclas -i https://pypi.tuna.tsinghua.edu.cn/simple

echo "恭喜安装成功，接下来进行验证安装测试"

paddleclas --model_name=person_exists --infer_imgs=docs/images/inference_deployment/whl_demo.jpg

echo "❀ 若出现识别结果，则恭喜你完成  PaddleClas 的安装！开始你的快乐使用吧 ❀"
