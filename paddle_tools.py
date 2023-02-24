"""TODO：之后可以考虑分发的形式，具体安装由下游实现，上层规定一些常用接口。"""
import sys
import os
my_python_exe = sys.executable
pwd = os.getcwd()

def PaddleSlim():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    print(f"暂未支持{sys._getframe().f_code.co_name} ，请等待！")

def FastDeploy():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    print(f"暂未支持{sys._getframe().f_code.co_name} ，请等待！")

def PaddleSpeech():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    print(f"暂未支持{sys._getframe().f_code.co_name} ，请等待！")

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
    infer_test = f"{cd_dst_dir}{my_python_exe} tools/predict.py \
                        --config configs/quick_start/pp_liteseg_optic_disc_512x512_1k.yml \
                        --model_path https://paddleseg.bj.bcebos.com/dygraph/optic_disc/pp_liteseg_optic_disc_512x512_1k/model.pdparams \
                        --image_path docs/images/optic_test_image.jpg \
                        --save_dir output/result"
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
    print(f"暂未支持{sys._getframe().f_code.co_name} ，请等待！")

def PaddleVideo():
    cd_dst_dir = f"cd {pwd}\{sys._getframe().f_code.co_name} && "
    print(f"暂未支持{sys._getframe().f_code.co_name} ，请等待！")

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
