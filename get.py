# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 15:28
# @Author  : super_kun
# @File    : spider.py
# @Software: PyCharm
# @Desc    : 从百度爬取图片
from gevent import monkey

monkey.patch_all()
import functools
import logging
import os
from bs4 import BeautifulSoup
from gevent.pool import Pool
import requests
import settings
import re

# 设置日志输出格式
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)

# 搜索关键词字典
keywords_map = settings.IMAGE_CLASS_KEYWORD_MAP
# 图片保存根目录
images_root = settings.IMAGES_ROOT
# 每个类别下载多少页图片
download_pages = settings.SPIDER_DOWNLOAD_PAGES
# 图片编号字典，每种图片都从0开始编号，然后递增
images_index_map = dict(zip(keywords_map.keys(), [0 for _ in keywords_map]))
# 图片去重器
duplication_filter = set()

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
# name = input('您要爬取什么图片')
num = 0
num_1 = 0
num_2 = 0
x = input('您要爬取几张呢?，输入1等于60张图片。')
list_1 = []

# 搜索关键词字典
keywords_map = settings.IMAGE_CLASS_KEYWORD_MAP
# 图片保存根目录
images_root = settings.IMAGES_ROOT
# 图片编号字典，每种图片都从0开始编号，然后递增
images_index_map = dict(zip(keywords_map.keys(), [0 for _ in keywords_map]))

# 首先，创建数据文件夹
if not os.path.exists(images_root):
    os.mkdir(images_root)
for sub_images_dir in keywords_map.keys():# 对于每个图片类别都创建一个单独的文件夹保存
    sub_path = os.path.join(images_root, sub_images_dir)
    if not os.path.exists(sub_path):
        os.mkdir(sub_path)

for img_class, keyword in keywords_map.items():
    for i in range(int(x)):
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword + '&pn=' + str(i * 30)
        res = requests.get(url, headers=headers)
        htlm_1 = res.content.decode()
        a = re.findall('"objURL":"(.*?)",', htlm_1)# 先利用正则表达式找到图片url

        for b in a:
            try:
                b_1 = re.findall('https:(.*?)&', b)
                b_2 = ''.join(b_1)
                if b_2 not in list_1:
                    num = num + 1
                    img = requests.get(b)

                    print('---------正在下载第' + str(num) + '张图片----------')
                    # 分配一个图片编号
                    image_index = images_index_map.get(img_class, 0)
                    # 更新待分配编号
                    images_index_map[img_class] = image_index + 1
                    # 拼接图片路径
                    image_path = os.path.join(images_root, img_class, '{}.jpg'.format(image_index))
                    # 保存图片
                    with open(image_path, 'wb') as f:
                        f.write(img.content)
                    list_1.append(b_2)
                elif b_2 in list_1:
                    num_1 = num_1 + 1
                    continue
            except Exception as e:
                print('---------第' + str(num) + '张图片无法下载----------')
                num_2 = num_2 + 1
                continue
print('下载完成,总共下载{}张,成功下载:{}张,重复下载:{}张,下载失败:{}张'.format(num + num_1 + num_2, num, num_1, num_2))