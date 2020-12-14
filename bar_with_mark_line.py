#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_with_mark_line.py
# @Version : Python 3.7
# @Time    : 2020-11-13 22:23


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_guide_line():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    bar.set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="min", name="最小值"),
                opts.MarkLineItem(type_="max", name="最大值"),
                opts.MarkLineItem(type_="average", name="平均值"),
            ]
        )
    )

    return bar


if __name__ == '__main__':
    chart = bar_with_guide_line()
    chart.render(path='chart_output/bar_with_guide_line.html')
