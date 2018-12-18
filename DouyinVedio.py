__author__="Liuweihao"


import json
from io import StringIO
from urllib import request

import requests
import cv2
path='E:/pic/frames/'
image = cv2.imread(path+'v0200f000000bdv0f5c0gfkji5fqgi30.jpg')
cropImg = image[0:300,0:200]
cv2.imwrite(path+'douyintest.jpg',cropImg)
from Anaconda.Lib import os


# path="F:/抖音/tuwei1/"
# videopath="C:/Users/Administrator/Downloads/逍遥安卓下载/Camera/"
#
# l=os.listdir(path)
# dir_list=os.listdir(videopath)
#
# # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
# # os.path.getmtime() 函数是获取文件最后修改时间
# # os.path.getctime() 函数是获取文件最后创建时间
# dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(videopath, x)))
# l= sorted(l,  key=lambda x: os.path.getctime(os.path.join(path, x)))
# # print(dir_list)
# num =0
# filtout=StringIO()
#
# for i in range(0,len(l)):
#     file = open(r"F:/抖音/tuwei1/post/" + l[i], encoding="utf-8")
#     js = json.load(file)
#     list_aweme = list(js["aweme_list"])
#     for n in range(0, len(list_aweme)):
#         filtout.write(str(num)+":"+dir_list[num]+"\n"+list_aweme[n]['desc']+"\n")
#         print(dir_list[num])
#         print(list_aweme[n]['desc'])
#         num += 1
# f=open("E:/123.txt","w")
# f.write(filtout.getvalue())
# print(num)









# s = requests.Session()
# headers = {'video_id': 'v0200ffb0000bfl9n1o9lr7csq8gi190',
#                'line': '0',
#                'ratio': '540p',
#                'media_type': '4',
#                'vr_type': '0',
#                'test_cdn': 'None',
#                'improve_bitrate': '0',
#             'device_platform': 'android',
#            'device_type':'LG-H990DS',
#            'version_code':'182',
#            'device_id':'59707021162',
#            'channel':'yinyueshouce'}
#
# header={''}
#
# url="https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f910000bfi2conu9qb1rg29l9ng&line=0&ratio=540p&media_type=4&vr_type=0&test_cdn=None&improve_bitrate=0"
#
# html = s.get(url, allow_redirects=False)
#
# print(html.headers['Location'])