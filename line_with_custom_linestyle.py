#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : line_with_custom_linestyle.py
# @Version : Python 3.7
# @Time    : 2020-11-15 20:01

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def line_with_custom_linestyle():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(Faker.choose())
    line.add_yaxis('样式1',
                   Faker.values(),
                   linestyle_opts=opts.LineStyleOpts(width=5,
                                                     curve=0,
                                                     opacity=0.7,
                                                     type_='solid',
                                                     color='red')
                   )
    line.add_yaxis('样式2',
                   Faker.values(),
                   linestyle_opts=opts.LineStyleOpts(width=3,
                                                     curve=0.5,
                                                     opacity=0.9,
                                                     type_='dashed',
                                                     color='yellow')
                   )
    line.add_yaxis('样式3',
                   Faker.values(),
                   linestyle_opts=opts.LineStyleOpts(width=1,
                                                     curve=1,
                                                     opacity=0.5,
                                                     type_='dotted',
                                                     color='green')
                   )
    return line


if __name__ == '__main__':
    chart = line_with_custom_linestyle()
    chart.render(path='chart_output/line_with_custom_linestyle.html')
