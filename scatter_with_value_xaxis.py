#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : scatter_with_value_xaxis.py
# @Version : Python 3.7
# @Time    : 2020-11-14 23:59


from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = [random.randint(0, 20) for _ in range(100)]
y_data = [random.randint(0, 50) for _ in range(100)]


def scatter_with_value_xaxis():
    scatter = Scatter(init_opts=opts.InitOpts(theme='light',
                                              width='1000px',
                                              height='600px'))
    scatter.add_xaxis(x_data)
    scatter.add_yaxis('', y_data)
    scatter.set_global_opts(xaxis_opts=opts.AxisOpts(type_="value"))
    return scatter


if __name__ == '__main__':
    chart = scatter_with_value_xaxis()
    chart.render(path='chart_output/scatter_with_value_xaxis.html')
