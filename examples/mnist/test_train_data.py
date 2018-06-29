#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 23:10
# @Author  : TOM.LEE
# @Site    : https://github.com/amlyj/tensorflowStudy
# @File    : test_train_data.py
# @Software: PyCharm
from __future__ import absolute_import, division, print_function

import os

import models
import load_image
import numpy as np
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def regression_train(sess, x_):
    """
    线性模型调用
    :param sess: tf.Session()
    :param x_: 输入
    :return:
    """
    x = tf.placeholder("float", [None, 28 * 28])
    # 调用线性模型
    with tf.variable_scope("regression"):
        y, variables = models.regression(x)
    # 创建saver对象
    saver = tf.train.Saver(var_list=variables)
    # 调用训练数据
    saver.restore(sess=sess, save_path='data/regression.train')
    return sess.run(y, feed_dict={x: x_}).flatten().tolist()


if __name__ == '__main__':
    data = load_image.image_to_array('png/1.png')
    session = tf.Session()
    # print(var_3.__len__())
    input_data = ((255 - np.array(data, dtype=np.int8)) / 255.0).reshape(1, 28 * 28)
    data = regression_train(sess=session, x_=input_data)
    session.close()
    for i, j in enumerate(data, start=0):
        print('%d : %.3f%%' % (i, j * 100))
