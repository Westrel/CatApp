# -*- coding: utf-8 -*-
# @File    : settings.py
# @Author  : super_kun
# @File    : data_split.py
# @Software: PyCharm
# @Brief   : 相关参数

# ##########爬虫############

# 图片类别和搜索关键词的映射关系
IMAGE_CLASS_KEYWORD_MAP = {
    'ringworm': '猫癣',
    'health_cats': '正常宠物猫'
}
# 图片保存根目录
IMAGES_ROOT = './images/data'
IMAGES_NEW_ROOT = './images/new_data'
# 爬虫每个类别下载多少页图片
SPIDER_DOWNLOAD_PAGES = 1

# #########数据###########

# 每个类别选取的图片数量
SAMPLES_PER_CLASS = 345
# 参与训练的类别
CLASSES = ['ringworm', 'health_cats']
# 参与训练的类别数量
CLASS_NUM = len(CLASSES)
# 类别->编号的映射
CLASS_CODE_MAP = {
    'ringworm': 0,
    'health_cats': 1
}
# 编号->类别的映射
CODE_CLASS_MAP = {
    0: '检测结果为猫癣的概率：',
    1: '检测结果为正常宠物猫的概率：'
}
# 随机数种子
# RANDOM_SEED = 13  # 四个类别时样本较为均衡的随机数种子
RANDOM_SEED = 19  # 三个类别时样本较为均衡的随机数种子

# 训练集比例
TRAIN_SCALE = 0.8
# 验证集比例
VAL_SCALE = 0.1
# 测试集比例
TEST_SCALE = 0.1

# mini_batch大小
BATCH_SIZE = 32

# 在训练Imagenet数据集时通常设置：mean=(0.485, 0.456, 0.406)，std=(0.229, 0.224, 0.225)
# imagenet数据集均值
IMAGE_MEAN = [0.485, 0.456, 0.406]
# imagenet数据集标准差
IMAGE_STD = [0.299, 0.224, 0.225]

# #########训练#########

# 学习率
LEARNING_RATE = 0.001
# 训练epoch数
TRAIN_EPOCHS = 30
# 保存训练模型的路径
MODEL_PATH = './models/model.h5'

# ########后端#########
# 端口号 8081
