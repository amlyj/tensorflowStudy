# 版本
> 1.1.0+

* [GitHub](https://github.com/tensorflow/tensorflow) | [tensorflow.org](https://www.tensorflow.org) | [tensorfly.cn](http://www.tensorfly.cn/)
* [windows install](https://www.tensorflow.org/install/install_windows)
* [linux install](https://www.tensorflow.org/install/install_linux)
* [mac os install](https://www.tensorflow.org/install/install_mac)
* [sources install](https://www.tensorflow.org/install/install_sources)

# Install

### Ubuntu
> Ubuntu 支持Python2.7x版本的Python环境，使用pip安装

    $ sudo pip install tensorflow==1.1.0
    $ sudo pip install protobuf==3.0.0


### windows
> windows 环境只支持3.5x和3.6x版本的Python环境
> Python3.x版本安装后，使用pip3来管理依赖包

* check env ：`$ python tensorflow_self_check.py`
* install **`msvcp140.dll`** ： https://www.microsoft.com/en-us/download/details.aspx?id=53587
* install **api-ms-win-crt-process-l1-1-0.dll**  ：
  * x64 ：https://www.microsoft.com/en-us/download/details.aspx?id=51161
  * x86 ：https://www.microsoft.com/en-us/download/details.aspx?id=51137
* install python3.6.5 ：https://www.python.org/downloads/release/python-365/
* upgrade pip3 ：`$ python -m pip install --upgrade pip`
* install tensorflow ：`$ pip3 install tensorflow==1.2.0`


## Link

* [机器学习新手入门](https://www.tensorflow.org/get_started/get_started_for_beginners)