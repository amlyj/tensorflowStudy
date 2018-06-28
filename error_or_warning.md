# 错误及警告处理

### 运行tensorflow出现以下警告:
```
2018-06-28 09:27:24.024275: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
2018-06-28 09:27:24.024297: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2018-06-28 09:27:24.024302: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2018-06-28 09:27:24.024306: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2018-06-28 09:27:24.024310: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
```
* simple.py： https://stackoverflow.com/questions/43134753/tensorflow-wasnt-compiled-to-use-sse-etc-instructions-but-these-are-availab
```python

from __future__ import absolute_import, division, print_function
import os
import tensorflow as tf

# set tf log level
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


print("TensorFlow version: {}".format(tf.VERSION))
```

