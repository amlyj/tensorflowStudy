#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 22:18
# @Author  : TOM.LEE
# @Site    : https://github.com/amlyj/tensorflowStudy
# @File    : mnist_regression.py
# @Software: PyCharm
from __future__ import absolute_import, division, print_function

import os

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import models

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == '__main__':
    # 导入数据,并创建mnist类
    print('导入训练数据,并创建mnist类')
    mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

    # 创建模型
    print('创建regression模型')
    with tf.variable_scope("regression"):
        x = tf.placeholder("float", [None, 28 * 28])
        y, variables = models.regression(x)

    # 训练模型
    print("训练regression模型")
    y_ = tf.placeholder("float", [None, 10])
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    # 创建预测函数
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

    # 初始化变量
    init = tf.global_variables_initializer()
    # 保存变量
    saver = tf.train.Saver(var_list=variables)
    with tf.Session() as sess:
        sess.run(init)
        for i in xrange(1000):
            batch_xs, batch_ys = mnist.train.next_batch(100)
            sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

        # 计算精度
        precision = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
        print('训练精度： %.2f%%' % (precision * 100))

        # 保存训练模型
        path = saver.save(sess=sess, save_path='data/regression.train', write_meta_graph=False, write_state=False)
        print("saved train model path: {}".format(path))
