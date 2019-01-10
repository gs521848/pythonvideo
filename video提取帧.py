import os, sys
import datetime
from PIL import Image
from images2gif import writeGif
import imageio
from urllib import request,error
#imageio制作gif https://www.cnblogs.com/dcb3688/p/4608048.html

# import matplotlib.pyplot as plt
# imagetogif 教程https://blog.csdn.net/monotonomo/article/details/80586194
import numpy as np

DATASET_ROOT='E:/pvideo/'
OUTPUT_ROOT='E:/pic1229/'
if not os.path.exists(OUTPUT_ROOT):
    os.makedirs(OUTPUT_ROOT)
# 提取帧的命令
def get_cmd(file, frame,vframes=1):
    # 获取最短的文件名
    basename = os.path.basename(file)
    name=str(basename).replace(".mp4","")
    output_path = OUTPUT_ROOT+'frames/'+basename+'/'
    input_path = DATASET_ROOT+file
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    cmd='ffmpeg -i '+input_path+' -y -f image2 '+' -ss 00:00:0'+frame+'  -vframes '+str(vframes)+' '+output_path+'/'+basename+frame+'.png'
    return cmd
starttime = datetime.datetime.now()
# 遍历DATASET_ROOT
dirs = os.listdir(DATASET_ROOT)
# 做成gif
def begif(file):
    basename = os.path.basename(file)
    outfilename=OUTPUT_ROOT+'gif/'+basename+'.gif'
    pressfilename=OUTPUT_ROOT+'pressgif/'+basename+'.gif'
    if not os.path.exists(OUTPUT_ROOT+'gif/'):
        os.makedirs(OUTPUT_ROOT+'gif/')
    filenames=[]

    for file in os.listdir(OUTPUT_ROOT+'frames/'+basename+'/'):
        filenames.append(OUTPUT_ROOT+'frames/'+basename+'/'+file)

    frames = []
    for image_name in filenames:
        # im = Image.open(image_name)
        # mypalette = im.getpalette()
        # # 通过convert将RGBA格式转化为RGB格式，以便后续处理
        # im = im.convert("RGB")
        # im = np.array(im)  # im还不是数组格式，通过此方法将im转化为数组

        frames.append(imageio.imread(image_name))
    imageio.mimsave(outfilename, frames, duration=1)
    #通过减少色位 压缩gif图的大小
    Stringcmd="E:/gifsicle/gifsicle -O3 "+outfilename+" -o "+pressfilename+" --colors 32"
    os.system(Stringcmd)
    # writeGif(outfilename, frames, duration=0.1, subRectangles=False)
def downloadandsave(url,name):
    video_url=url
    #request下载
    request.urlretrieve(url=video_url,filename=DATASET_ROOT+name)
    print(name+':success')


#下载视频
# v=open('./video.txt','r')
# videoline=v.read().splitlines()
# print(videoline)
# errorurl=[]
# for url in videoline:
#     if not url.startswith('http://v.bjyzbx'):
#         print('ignore:'+url)
#     else:
#         name=url[-36:]
#         try:
#             downloadandsave(url,name)
#         except error.HTTPError as v:
#             print(url+": "+str(v))
#             errorurl.append(url)
# print(errorurl)

def resizeImg(file,outfile):
    if not os.path.exists(outfile):
        os.mkdir(outfile)
    for files in os.listdir(file):
        img=Image.open(files)
        w,h=img.size
        img.resize((w/2, h/2)).save(os.path.join(outfile, file), "png")

for file in os.listdir(DATASET_ROOT+'/'):


    # 如果不是.mp4后缀，忽略
    if not file.endswith('mp4'):
        print('ignore ',file)
    else:
            # 提取帧
        cmd1 = get_cmd(file,'1')
        cmd2 = get_cmd(file,'2')
        cmd3 = get_cmd(file,'3')

        # print(cmd1)
        # print(cmd2)
        # print(cmd3)
        # try:
        #     os.system(cmd1)
        #     os.system(cmd2)
        #     os.system(cmd3)
        # except FileNotFoundError as f:
        #     print("Filenofond")
        # except RuntimeError as r:
        #     print(r)
    begif(file)


