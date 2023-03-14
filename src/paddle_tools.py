"""TODO：之后可以考虑OOP分发的形式，具体安装由下游实现，上层规定一些常用接口。"""
import sys
import os
my_python_exe = sys.executable
pwd = os.getcwd()

def PaddleSlim():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    os.system(f"{cd_dst_dir}{my_python_exe} -m pip install paddleslim")
    import paddle
    import paddle.fluid as fluid
    try:
        import paddleslim as slim
    except:
        print("错误，paddleslim安装失败，请重试若还不行请联系工作人员")
    paddle.enable_static()
    exe, train_program, val_program, inputs, outputs =slim.models.image_classification("MobileNet", [1, 28, 28], 10, use_gpu=True)
    FLOPs = slim.analysis.flops(train_program)
    print("FLOPs: {}".format(FLOPs))
    pruner = slim.prune.Pruner()
    pruned_program, _, _ = pruner.prune(
            train_program,
            fluid.global_scope(),
            params=["conv2_1_sep_weights","conv2_2_sep_weights"],
            ratios=[0.33] * 2,
            place=fluid.CPUPlace())
    FLOPs = slim.analysis.flops(pruned_program)
    print("FLOPs: {}".format(FLOPs))
    import paddle.dataset.mnist as reader
    train_reader = paddle.fluid.io.batch(
            reader.train(), batch_size=256, drop_last=True)
    train_feeder = fluid.DataFeeder(inputs, fluid.CPUPlace())
    count = 0 
    for data in train_reader():
        count +=1 
        if count > 6:
            break
        acc1, acc5, loss, _ = exe.run(pruned_program, feed=train_feeder.feed(data), fetch_list=outputs)
        print("acc1：",acc1, "acc5：",acc5,"loss：", loss)

    print("❀ 若成功看到acc和loss信息，则恭喜你完成 PaddleSlim 的安装！开始你的快乐使用吧 ❀") 

def FastDeploy():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    print(f"暂未支持{sys._getframe().f_code.co_name} ，请等待！")

def PaddleSpeech():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    print("开始安装依赖，请等待")
    os.system(f"{cd_dst_dir}{my_python_exe} -m pip install pytest-runner")
    os.system(f"{cd_dst_dir}{my_python_exe} -m pip install .")
    print("恭喜安装成功，接下来进行验证安装测试")
    os.system(f"{cd_dst_dir}powershell wget -c https://paddlespeech.bj.bcebos.com/PaddleAudio/zh.wav")
    print ("-> 运行语音识别测试验证")
    print ("若出现'我认为跑步最重要的就是给我带来了身体健康'则表示成功")
    os.system(f"{cd_dst_dir}paddlespeech asr --lang zh --input zh.wav")

    print ("-> 进行标点符号补全验证")
    print ("输入：今天的天气真不错啊你下午有空吗我想约你一起去吃饭")
    os.system(f"{cd_dst_dir}paddlespeech text --task punc --input\
               今天的天气真不错啊你下午有空吗我想约你一起去吃饭")
    print ("-> 进行声音分类验证")
    print ("若出现置信度则表示成功")
    os.system(f"{cd_dst_dir}paddlespeech cls --input zh.wav")

    print ("若上面测试都能出现预期结果，则通过测试")
    print ("❀ 恭喜你完成  PaddleSpeech 的安装与验证，开始愉快的使用吧！")

def PaddleClas():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    print("开始安装依赖，请等待")
    os.system(f"{cd_dst_dir}{my_python_exe} -m pip install paddleclas -i https://pypi.tuna.tsinghua.edu.cn/simple")
    print("恭喜安装成功，接下来进行验证安装测试")
    os.system(f"{cd_dst_dir} paddleclas --model_name=person_exists --infer_imgs=docs/images/inference_deployment/whl_demo.jpg")
    print("❀ 若出现识别结果，则恭喜你完成  PaddleClas 的安装！开始你的快乐使用吧 ❀")

def PaddleDetection():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    print("开始安装依赖，请等待")
    print("注意！在安装ppdet之前，你需要安装c++生成工具，你是否需要安装？[y/Y] 选择其他默认安装了")
    print("若未安装完成，你将遇到 building 'pycocotools._mask' extension 编译问题！")
    if_cpp = input("")
    if if_cpp in ["Y","y","yes","YES"]:
        print("开始下载并安装：")
        url = "https://aka.ms/vs/17/release/vs_BuildTools.exe"
        filePath = "vs_BuildTools.exe"
        command = f"powershell Invoke-WebRequest -Uri {url} -OutFile {filePath}"
        os.system(command)    
        print("请选择安装界面左上角的C++桌面程序，然后一路安装等待完毕即可~")
        os.system("vs_BuildTools.exe")
        while True:
            if_install = input("你是否已经安装完毕？[y/Y] 请安装完成再选择！")
            if if_install in ["Y","y","yes","YES"]:
                break
            else:
                print("输入错误！")

    os.system(f"{cd_dst_dir}{my_python_exe} -m pip install pyyaml")
    os.system(f"{cd_dst_dir}{my_python_exe} -m pip install -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple")
    print("开始编译安装paddledet")
    os.system(f"{cd_dst_dir}{my_python_exe} setup.py install")
    print("恭喜安装成功，接下来进行验证安装测试（出现OK即可）")
    os.system(f"{cd_dst_dir}{my_python_exe} ppdet/modeling/tests/test_architectures.py")

    if_gpu = input("接下来要进行安装测试，请问你是否选择在CPU上测试？[Y/y],选择其他则在GPU上执行")
    if if_gpu in ["Y","y","yes","YES"]:
        use_gpu = "False"
    else:
        use_gpu = "True"

    infer_test = f"{cd_dst_dir}{my_python_exe} tools/infer.py -c configs/ppyolo/ppyolo_r50vd_dcn_1x_coco.yml \
                      -o use_gpu={use_gpu} weights=https://paddledet.bj.bcebos.com/models/ppyolo_r50vd_dcn_1x_coco.pdparams \
                      --infer_img=demo/000000014439.jpg"
    os.system(infer_test)

    print("❀ 恭喜你完成 PaddleDetection 的安装，请前往 output 文件夹下查看 000000014439.jpg文件是否包含预测框 ❀")

def PaddleSeg():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    os.system(f'{cd_dst_dir}{my_python_exe} -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple')
    os.system(f'{cd_dst_dir}{my_python_exe} -m pip install -v -e .')
    print("恭喜安装成功，接下来进行验证安装测试")
    infer_test = fr"{cd_dst_dir}{my_python_exe} tools\predict.py \
                        --config configs\quick_start\pp_liteseg_optic_disc_512x512_1k.yml \
                        --model_path https://paddleseg.bj.bcebos.com/dygraph/optic_disc/pp_liteseg_optic_disc_512x512_1k/model.pdparams \
                        --image_path docs\images\optic_test_image.jpg \
                        --save_dir output\result"
    os.system(infer_test)
    print("❀ 若没有报错，则恭喜你完成  PaddleSeg 的安装！开始你的快乐使用吧 ❀")
    pass

def PaddleOCR():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    os.system(f'{cd_dst_dir}{my_python_exe} -m pip install "paddleocr>=2.0.1" -i https://pypi.tuna.tsinghua.edu.cn/simple')
    print("恭喜安装成功，接下来进行验证安装测试")
    print("是否选择使用 GPU 验证？[Y/N]，若选择N则使用 CPU 验证")
    
    if_gpu = input("接下来要进行安装测试，请问你是否选择在CPU上测试？[Y/y],选择其他则在GPU上执行")
    if if_gpu in ["Y","y","yes","YES"]:
        use_gpu = "False"
    else:
        use_gpu = "True"

    infer_test = f"{cd_dst_dir}{my_python_exe} paddleocr --image_dir ./doc/imgs/11.jpg --use_angle_cls true --use_gpu {use_gpu}"
    os.system(infer_test)

def PaddleNLP():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    os.system(f'{cd_dst_dir}{my_python_exe} -m pip install setuptools_scm')
    os.system(f'{cd_dst_dir}{my_python_exe} -m pip install --upgrade paddlenlp -i https://pypi.tuna.tsinghua.edu.cn/simple')
    print("恭喜安装成功，接下来进行验证安装测试")
    from paddlenlp import Taskflow
    schema = ['时间', '选手', '赛事名称']
    ie = Taskflow('information_extraction', schema=schema)
    print(ie('2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌!'))
    print("❀ 若出现识别结果，则恭喜你完成 PaddleNLP 的安装！开始你的快乐使用吧 ❀")

def PaddleVideo():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    print ("开始安装依赖，请等待")
    os.system(f'{cd_dst_dir}{my_python_exe} -m pip install ppvideo -i https://pypi.tuna.tsinghua.edu.cn/simple')
    if_gpu = input("接下来要进行安装测试，请问你是否选择在CPU上测试？[Y/y],选择其他则在GPU上执行")
    if if_gpu in ["Y","y","yes","YES"]:
        use_gpu = "False"
    else:
        use_gpu = "True"
    os.system(f'{cd_dst_dir}ppvideo --model_name="ppTSM_v2" --use_gpu={use_gpu} --video_file="data/example.avi"')
    print("❀ 若出现'archery'识别结果，则恭喜你完成  PaddleVideo 的安装！开始你的快乐使用吧 ❀")

def PaddleGAN():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    print(f"暂未支持{sys._getframe().f_code.co_name} ，请等待！")

def _do_install(pkgs):
    try:
        from pip import main
    except Exception:
        from pip._internal import main
    return main(['install'] + [pkgs]+["-i"]+["https://pypi.tuna.tsinghua.edu.cn/simple"])


if __name__ == "__main__":
    pass
