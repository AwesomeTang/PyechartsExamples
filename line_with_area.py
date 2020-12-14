#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : line_with_area.py
# @Version : Python 3.7
# @Time    : 2020-11-15 12:29


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data = [i + random.randint(10, 20) for i in range(len(x_data))]


def line_with_area():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    line.add_yaxis('', y_data)
    # opacity 默认为0，即透明
    line.set_series_opts(areastyle_opts=opts.AreaStyleOpts(opacity=0.5))

    return line


if __name__ == '__main__':
    chart = line_with_area()
    chart.render(path='chart_output/line_with_area.html')
