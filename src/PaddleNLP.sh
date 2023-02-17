echo "====== 欢迎使用 PaddleNLP 安装工具 ======"
echo "请确保在 PaddleNLP 目录下运行此脚本"
echo " "

echo "开始安装依赖，请等待"

pip install setuptools_scm
pip install --upgrade paddlenlp -i https://pypi.tuna.tsinghua.edu.cn/simple

echo "恭喜安装成功，接下来进行验证安装测试"
python -c "from pprint import pprint;\
from paddlenlp import Taskflow;\
schema = ['时间', '选手', '赛事名称'];\
ie = Taskflow('information_extraction', schema=schema);\
pprint(ie('2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌!'))"

echo "❀ 若出现识别结果，则恭喜你完成 PaddleNLP 的安装！开始你的快乐使用吧 ❀"
