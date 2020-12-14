#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_reverse_axis.py
# @Version : Python 3.7
# @Time    : 2020-11-14 23:48

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_reverse_axis():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    # x,y轴翻转
    bar.reversal_axis()
    return bar


if __name__ == '__main__':
    chart = bar_reverse_axis()
    chart.render(path='chart_output/bar_reverse_axis.html')
