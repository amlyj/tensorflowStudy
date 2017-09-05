#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-5-18 下午3:44
# @Author         : Tom.Lee
# @Description    : 下载用于训练和测试的MNIST数据集
# @File           : mnist_download.py
# @Product        : PyCharm

from tensorflow.examples.tutorials.mnist import input_data

# 下载用于训练和测试的MNIST数据集
input_data.read_data_sets("MNIST_data/", one_hot=True)
