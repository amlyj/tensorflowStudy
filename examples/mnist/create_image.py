#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-29 下午3:43
# @Author         : Tom.Lee
# @File           : create_image.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from __future__ import absolute_import, division, print_function
from tensorflow.examples.tutorials.mnist import input_data
import scipy.misc
import os

# 读取MNIST数据集。如果不存在会事先下载。
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 原始图片保存
save_dir = 'png/'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

# 保存前20张图片
for i in range(5):
    # 请注意，mnist.train.images[i, :]就表示第i张图片（序号从0开始）
    image_array = mnist.train.images[i, :]
    # TensorFlow中的MNIST图片是一个784维的向量，我们重新把它还原为28x28维的图像。
    image_array = image_array.reshape(28, 28)
    # 保存文件
    filename = 'png/{}.png'.format(i)
    # 将image_array保存为图片
    # 先用scipy.misc.toimage转换为图像，再调用save直接保存。
    scipy.misc.toimage(image_array, cmin=0.0, cmax=1.0).save(filename)

print('Please check: %s ' % save_dir)
