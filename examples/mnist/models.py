#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 22:12
# @Author  : TOM.LEE
# @Site    : https://github.com/amlyj/tensorflowStudy
# @File    : models.py
# @Software: PyCharm
"""
训练模型
"""

import tensorflow as tf


def regression(x):
    """
    线性回归
    Y = W*x+b
    :param x:
    :return: W*x+b
    """
    W = tf.Variable(tf.zeros([784, 10]), name='W')
    b = tf.Variable(tf.zeros([10]), name='b')
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    return y, [W, b]
