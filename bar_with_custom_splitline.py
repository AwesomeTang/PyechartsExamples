#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_with_custom_splitline.py
# @Version : Python 3.7
# @Time    : 2020-11-15 20:45

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_custom_splitline():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    # x,y轴翻转
    bar.set_global_opts(yaxis_opts=opts.AxisOpts(
        splitline_opts=opts.SplitLineOpts(is_show=True,
                                          linestyle_opts=opts.LineStyleOpts(type_='dotted'))))
    return bar


if __name__ == '__main__':
    chart = bar_with_custom_splitline()
    chart.render(path='chart_output/bar_with_custom_splitline.html')
