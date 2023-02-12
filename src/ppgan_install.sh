echo "====== 欢迎使用 PaddleGAN 安装工具 ======"
echo "请确保在 PaddleGAN 目录下运行此脚本"
echo " "

echo "开始安装依赖，请等待"
pip install -v -e . -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

echo "涉及视频的任务都需安装ffmpeg，这里使用conda安装："
conda install x264=='1!152.20180717' ffmpeg=4.0.2 -c conda-forge

echo "恭喜安装成功，接下来进行验证安装测试"

wget -c --content-disposition https://user-images.githubusercontent.com/48054808/130388598-1e2b27e7-be66-49df-84d5-57b4dc7730d6.png 
wget -c --content-disposition https://user-images.githubusercontent.com/79366697/118655415-1ec8c000-b81c-11eb-8002-90bf8d477860.png 

python applications/tools/lapstyle.py --content_img_path 130388598-1e2b27e7-be66-49df-84d5-57b4dc7730d6.png\
 --style_image_path 118655415-1ec8c000-b81c-11eb-8002-90bf8d477860.png

echo " "
echo "查看是否生成转换后图片：output_dir/LapStyle/"
ls output_dir/LapStyle/
echo "❀ 若上面出现stylized.png，则恭喜你完成 PaddleGAN 的安装！开始你的快乐使用吧 ❀"
