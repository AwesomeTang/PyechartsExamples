#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_with_datazoom_slider.py
# @Version : Python 3.7
# @Time    : 2020-11-14 17:10

from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data = [random.randint(10, 20) for i in range(len(x_data))]


def bar_with_datazoom_slider():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    bar.add_yaxis('', y_data)
    bar.set_global_opts(datazoom_opts=opts.DataZoomOpts(range_start=50,   # 设置起止位置，50%-100%
                                                        range_end=100))
    return bar


if __name__ == '__main__':
    chart = bar_with_datazoom_slider()
    chart.render(path='chart_output/bar_with_datazoom_slider.html')
