#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-9-5 上午9:35
# @Author         : Tom.Lee
# @File           : tensor_test.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :

from __future__ import absolute_import, division, print_function

import os

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == '__main__':
    print("TensorFlow version: {}".format(tf.VERSION))
    hello = tf.constant('TensorFlow Say  : Hello World!')
    with tf.Session() as sess:
        print(sess.run(hello))
        a = tf.constant(10)
        b = tf.constant(32)
        print(sess.run(a + b))
