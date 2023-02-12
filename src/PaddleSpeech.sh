echo "====== 欢迎使用 PaddleSpeech 安装工具 ======"
echo "请确保在 PaddleSpeech 目录下运行此脚本"
echo " "

echo "开始安装 PaddleSpeech，请等待"
pip install pytest-runner
pip install .

echo " "
echo "恭喜安装成功，接下来进行验证安装测试"
wget -c https://paddlespeech.bj.bcebos.com/PaddleAudio/zh.wav

echo " "
echo "-> 运行语音识别测试验证"
echo "若出现'我认为跑步最重要的就是给我带来了身体健康'则表示成功"
paddlespeech asr --lang zh --input zh.wav
echo " "
echo "-> 进行标点符号补全验证"
echo "输入：今天的天气真不错啊你下午有空吗我想约你一起去吃饭"
paddlespeech text --task punc --input 今天的天气真不错啊你下午有空吗我想约你一起去吃饭
echo " "
echo "-> 进行声音分类验证"
echo "若出现置信度则表示成功"
paddlespeech cls --input zh.wav

echo "若上面测试都能出现预期结果，则通过测试"
echo " "
echo "❀ 恭喜你完成  PaddleSpeech 的安装与验证，开始愉快的使用吧！"
