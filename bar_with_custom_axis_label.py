#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_with_custom_axis_label.py
# @Version : Python 3.7
# @Time    : 2020-11-15 15:55

from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = list(range(2010, 2020))
y_data = [random.randint(20, 200) for _ in range(len(x_data))]


def bar_with_custom_axis_label():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    bar.add_yaxis('', y_data)

    bar.set_global_opts(xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(formatter='{value}年')))
    return bar


if __name__ == '__main__':
    chart = bar_with_custom_axis_label()
    chart.render(path='chart_output/bar_with_custom_axis_label.html')
