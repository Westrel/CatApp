# 介绍
这是一个从零开始构建的深度学习小项目，提供猫癣的识别服务

# 代码结构
主要是通过tensorflow训练两组模型来执行分类任务
一组为猫癣一组为正常宠物猫

代码的结构如下
|--images               目录下用于存放数据集
|    |--data            目录用于存放爬取下来的图片
|    |--new_data        目录用于存放测试集（test）、训练集（train）和验证集（val）
|--models               用于存放CNN模型
|--temp_file            用于用户上传的文件
|--templates            使用Django创建的后端项目
|   |-- web             测试用页面
|   |-- __init__.py     一个空文件，告诉 Python 该目录是一个 Python 包
|   |-- asgi.py         一个 ASGI 兼容的 Web 服务器的入口，以便运行你的项目
|   |-- settings.py     该 Django 项目的设置/配置
|   |-- urls.py         url 配置
|   |-- views.py        添加的视图文件
|   |-- wsgi.py         一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目
|--manage.py            一个实用的命令行工具，在命令行输入python manage.py runserver 0.0.0.0:8000 启动服务器 
                        0.0.0.0 让其它电脑可连接到开发服务器，8000 为端口号。如果不说明，那么端口号默认为 8000。
|--data.py 数据预处理部分加迁移学习
|--data_split.py 将数据集划分为测试集（test）、训练集（train）和验证集（val）
|--eval.py 测试文件，主要是用于测试CNN模型在验证集上的准确率，这个信息在results的txt的输出中也能获取
|--get.py 爬虫程序，从百度爬取图片，构建训练用的数据集
|--models.py 构建CNN模型代码
|--models.png 构建出的模型图片
|--train.py 训练CNN模型的代码，最优的参数将被保存在settings.MODEL_PATH
|--settings.py 相关数值的设置
|--requirements.txt 是本项目需要的包


# 参考博文
[从零开始编写一个宠物识别系统（爬虫、模型训练和调优、模型部署、Web服务）](https://www.aaronjny.com/articles/2019/12/17/1576592367309.html) (https://www.aaronjny.com/articles/2019/12/17/1576592367309.html)

或

[从零开始编写一个宠物识别系统（爬虫、模型训练和调优、模型部署、Web服务）](https://blog.csdn.net/aaronjny/article/details/103605988) (https://blog.csdn.net/aaronjny/article/details/103605988)