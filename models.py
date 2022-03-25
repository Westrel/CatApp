# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 15:28
# @Author  : super_kun
# @File    : models.py
# @Software: PyCharm
# @Desc    : 构建模型
import tensorflow as tf
import settings
# CBAPD

def my_densenet():
    """
    创建并返回一个基于densenet的Model对象
    """
    # 获取densenet网络，使用在imagenet上训练的参数值，移除头部的全连接网络，池化层使用max_pooling
    densenet = tf.keras.applications.DenseNet121(include_top=False, weights='imagenet', pooling='max')
    # 冻结预训练的参数，在之后的模型训练中不会改变它们
    densenet.trainable = False
    # 构建模型，使用Sequential
    model = tf.keras.Sequential([
        # 输入层 模型接收的输入格式shape为(None,224,224,3)
        tf.keras.layers.Input((224, 224, 3)),
        # 输入到DenseNet121中
        densenet,
        # Flatten层，将DenseNet121的输出展平，以作为全连接层的输入 形状转换，将输入特征拉直变成一维数组
        tf.keras.layers.Flatten(),
        # 添加BN层 批标准化
        tf.keras.layers.BatchNormalization(),
        # 随机失活 概率rate = 0.5
        tf.keras.layers.Dropout(0.5),
        # 第一个全连接层，激活函数relu
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        # BN层
        tf.keras.layers.BatchNormalization(),
        # 随机失活 舍弃
        tf.keras.layers.Dropout(0.5),
        # 第二个全连接层，激活函数relu
        tf.keras.layers.Dense(64, activation=tf.nn.relu),
        # BN层
        tf.keras.layers.BatchNormalization(),
        # 输出层，为了保证输出结果的稳定，这里就不添加Dropout层了
        tf.keras.layers.Dense(settings.CLASS_NUM, activation=tf.nn.softmax)
    ])

    return model
# 测试代码，检查模型是否符合要求
# from tensorflow.keras.utils import plot_model
# model = my_densenet()
# plot_model(model,
#            to_file='model.png',
#            dpi=100,
#            show_shapes=True,
#            show_layer_names=True)
#
if __name__ == '__main__':
    model = my_densenet()
    model.summary()
#     查看模型结构信息
