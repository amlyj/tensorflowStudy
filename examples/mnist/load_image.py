#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-29 下午3:31
# @Author         : Tom.Lee
# @File           : load_image.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from __future__ import print_function, division, absolute_import

import numpy as np
from PIL import Image


def image_to_array(file_path):
    """
    图片转数组
    Args:
        file_path:

    Returns: 数组
    """
    image = Image.open(file_path).convert('L')
    image_array = np.asarray(image)
    s = []
    for i in list(image_array):
        s += list(i)
    return s