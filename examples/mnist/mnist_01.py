#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-5-18 下午3:46
# @Author         : Tom.Lee
# @Description    : 加载测试数据
# @File           : mnist_01.py
# @Product        : PyCharm
from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 导入数据,并创建mnist类
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# 通过操作符号变量来描述这些可交互的操作单元
x = tf.placeholder("float", [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder("float", [None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
