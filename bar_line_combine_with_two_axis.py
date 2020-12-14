#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_line_combine_with_two_axis.py
# @Version : Python 3.7
# @Time    : 2020-11-15 15:20

from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ['香蕉', '梨子', '水蜜桃', '核桃', '西瓜', '苹果']
y_data_1 = [random.randint(10, 50) for _ in range(len(x_data))]
y_data_2 = [random.randint(100, 500) for _ in range(len(x_data))]


def bar_line_combine_with_two_axis():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    # 添加一个Y轴
    bar.extend_axis(yaxis=opts.AxisOpts())
    bar.add_yaxis('左边Y轴', y_data_1, yaxis_index=0)

    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    line.add_yaxis('左边Y轴', y_data_2, yaxis_index=1)

    bar.overlap(line)
    return bar


if __name__ == '__main__':
    chart = bar_line_combine_with_two_axis()
    chart.render(path='chart_output/bar_line_combine_with_two_axis.html')
