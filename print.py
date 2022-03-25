# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 20:32
# @Author  : super_kun
# @File    : print.py.py
# @Software: PyCharm
# @Desc    :用户上传一张照片预测
# 导入模型

import tensorflow as tf
import settings
import json
from models import my_densenet

# 导入模型
model = my_densenet()
# 加载训练好的参数
model.load_weights(settings.MODEL_PATH)

# 上传一张图片，返回此图片上的宠物是那种类别，概率多少
def cats_classify(str):
    # 获取用户上传的图片
    img_str = tf.io.read_file(str)
    # img_str = tf.io.read_file("./temp_file/0.jpg")
    # 进行数据预处理
    x = tf.image.decode_image(img_str, channels=3)# 图片解码 解码图像的颜色通道数量为3
    x = tf.image.resize(x, (224, 224))
    x = x / 255.# 归一化
    x = (x - tf.constant(settings.IMAGE_MEAN)) / tf.constant(settings.IMAGE_STD)
    x = tf.reshape(x, (1, 224, 224, 3))


    # 将图片输入到模型预测
    y_pred = model(x)
    # 获取输出结果中最大概率的索引
    pet_cls_code = tf.argmax(y_pred, axis=1).numpy()[0]
    pet_cls_prob = float(y_pred.numpy()[0][pet_cls_code])
    pet_cls_prob = '{:.2f}%'.format(int(pet_cls_prob * 100))
    pet_class = '{}'.format(settings.CODE_CLASS_MAP.get(pet_cls_code))# 获得对应类名
    # print(pet_cls_prob)
    # print(pet_class)
    # return pet_class
    # 将预测结果组织成json数据
    # res = {
    #     'pet_cls': pet_class,
    #     'probability': pet_cls_prob
    # }
    # # 返回json数据
    # result = json.dumps(res)
    # text = '检测结果'.pet_cls_prob,pet_class
    return pet_class + pet_cls_prob
if __name__=="__main__":
    cats_classify()

