#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : line_with_smooth_connect.py
# @Version : Python 3.7
# @Time    : 2020-11-15 12:38


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def line_with_smooth_connect():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(Faker.choose())
    line.add_yaxis('平滑曲线', Faker.values(), is_smooth=True)
    line.add_yaxis('直线', Faker.values(), is_smooth=False)

    return line


if __name__ == '__main__':
    chart = line_with_smooth_connect()
    chart.render(path='chart_output/line_with_smooth_connect.html')
