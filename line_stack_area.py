#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : line_stack_area.py
# @Version : Python 3.7
# @Time    : 2020-11-15 13:04


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def line_stack_area():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(Faker.choose())
    line.add_yaxis('A',
                   Faker.values(),
                   stack='stack')
    line.add_yaxis('B',
                   Faker.values(),
                   stack='stack')
    line.add_yaxis('C',
                   Faker.values(),
                   stack='stack')
    # opacity 默认为0，即透明
    line.set_series_opts(areastyle_opts=opts.AreaStyleOpts(opacity=0.5))

    return line


if __name__ == '__main__':
    chart = line_stack_area()
    chart.render(path='chart_output/line_stack_area.html')
