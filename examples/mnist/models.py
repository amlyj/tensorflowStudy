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
    Y = w*x+b
    :param x:
    :return: w*x+b, [w, b]
    """
    w = tf.Variable(tf.zeros([28 * 28, 10]), name='w')
    b = tf.Variable(tf.zeros([10]), name='b')
    y = tf.nn.softmax(tf.matmul(x, w) + b)
    return y, [w, b]
