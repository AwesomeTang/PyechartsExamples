#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_with_visualmap_color.py
# @Version : Python 3.7
# @Time    : 2020-11-14 23:55


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_visualmap_color():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    bar.set_global_opts(visualmap_opts=opts.VisualMapOpts())
    return bar


if __name__ == '__main__':
    chart = bar_with_visualmap_color()
    chart.render(path='chart_output/bar_with_visualmap_color.html')
