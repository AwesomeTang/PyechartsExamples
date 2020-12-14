#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : line_with_two_xaxis.py
# @Version : Python 3.7
# @Time    : 2020-11-22 10:00


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data_1 = ["2020/10/{}".format(i + 1) for i in range(30)]
x_data_2 = ["2019/10/{}".format(i + 1) for i in range(30)]
y_data_1 = [random.randint(10, 50) for _ in range(30)]
y_data_2 = [random.randint(20, 60) for _ in range(30)]


def line_with_two_xaxis():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data_1)
    # 添加一个x轴
    line.extend_axis(xaxis_data=x_data_2, xaxis=opts.AxisOpts())
    line.add_yaxis('下面X轴', y_data_1)
    line.add_yaxis('上面X轴', y_data_2)
    return line


if __name__ == '__main__':
    chart = line_with_two_xaxis()
    chart.render(path='chart_output/line_with_two_xaxis.html')
