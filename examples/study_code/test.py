#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/18 23:21
# @Author  : Tom.lee
# @Docs    : http://www.tensorfly.cn/tfdoc/get_started/introduction.html
# @File    : test.py
# @Software: PyCharm

"""
这段很短的 Python 程序生成了一些三维数据, 然后用一个平面拟合它
"""

from __future__ import absolute_import, division, print_function

import os

import numpy as np
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
x_data = np.float32(np.random.rand(2, 100))  # 随机输入
y_data = np.dot([0.100, 0.200], x_data) + 0.300

# 构造一个线性模型
#
b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
# init = tf.initialize_all_variables() # initialize_all_variables is deprecated
init = tf.global_variables_initializer()

# 启动图 (graph)
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in xrange(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))
