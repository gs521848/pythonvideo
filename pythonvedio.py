__author__="Liuweihao"



import os, sys
import datetime

DATASET_ROOT='E:/抖音/ProxyApp/Debug/videos/'
OUTPUT_ROOT='E:/抖音/'
# 提取帧的命令
def get_cmd(file, frames = 1):
    # 获取最短的文件名
    basename = os.path.basename(file)
    name=str(basename).replace(".mp4","")
    output_path = OUTPUT_ROOT+'frames/'
    input_path = DATASET_ROOT+file
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    cmd='ffmpeg -i '+input_path+' -y -f image2 '+' -ss 00:00:01  -vframes 1 '+output_path+'/'+name+'.jpg'
    return cmd
starttime = datetime.datetime.now()
# 遍历DATASET_ROOT
dirs = os.listdir(DATASET_ROOT)

for file in os.listdir(DATASET_ROOT+'/'):
    # 如果不是.mp4后缀，忽略
    if not file.endswith('mp4'):
        print('ignore ',file)
    else:
            # 提取帧
        cmd = get_cmd(file)
        print(cmd)
        os.system(cmd)

endtime = datetime.datetime.now()
print((endtime-starttime).seconds)
