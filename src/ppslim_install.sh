echo "====== 欢迎使用 PaddleSlim 安装工具 ======"
echo "请确保在 PaddleSlim 目录下运行此脚本"
echo " "

echo "开始安装依赖，请稍等"

pip install paddleslim -i https://pypi.tuna.tsinghua.edu.cn/simple

echo " "
echo "接下来验证安装，请稍后......"
# 进入测试目录
cd example/auto_compression/
下载MobileNet预测模型``
wget -c https://paddle-imagenet-models-name.bj.bcebos.com/dygraph/inference/MobileNetV1_infer.tar
tar -xf MobileNetV1_infer.tar
# 下载ImageNet小型数据集
wget -c https://sys-p0.bj.bcebos.com/slim_ci/ILSVRC2012_data_demo.tar.gz
tar -xf ILSVRC2012_data_demo.tar.gz
python -c '''
# 导入依赖包
import paddle
from PIL import Image
from paddle.vision.datasets import DatasetFolder
from paddle.vision.transforms import transforms
from paddleslim.auto_compression import AutoCompression
paddle.enable_static()
# 定义DataSet
class ImageNetDataset(DatasetFolder):
    def __init__(self, path, image_size=224):
        super(ImageNetDataset, self).__init__(path)
        normalize = transforms.Normalize(
            mean=[123.675, 116.28, 103.53], std=[58.395, 57.120, 57.375])
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(image_size), transforms.Transpose(),
            normalize
        ])

    def __getitem__(self, idx):
        img_path, _ = self.samples[idx]
        return self.transform(Image.open(img_path).convert("RGB"))

    def __len__(self):
        return len(self.samples)

# 定义DataLoader
train_dataset = ImageNetDataset("./ILSVRC2012_data_demo/ILSVRC2012/train/")
image = paddle.static.data(
    name="inputs", shape=[None] + [3, 224, 224], dtype="float32")
train_loader = paddle.io.DataLoader(train_dataset, feed_list=[image], batch_size=32, return_list=False)
# 开始自动压缩
ac = AutoCompression(
    model_dir="./MobileNetV1_infer",
    model_filename="inference.pdmodel",
    params_filename="inference.pdiparams",
    save_dir="MobileNetV1_quant",
    config={"QuantPost": {}, "HyperParameterOptimization": {"ptq_algo": ["avg"], "max_quant_count": 3}},
    train_dataloader=train_loader,
    eval_dataloader=train_loader)
ac.compress()
'''

echo "测试压缩前模型的精度:"
python ./image_classification/eval.py

echo "测试压缩前模型的精度:"
python ./image_classification/eval.py --model_dir='MobileNetV1_quant'

echo "❀ 若出现精度结果，则恭喜你完成 PaddleSlim 的安装！开始你的快乐使用吧 ❀"
