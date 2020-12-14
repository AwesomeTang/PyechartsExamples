#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : scatter_with_visualmap_size.py
# @Version : Python 3.7
# @Time    : 2020-11-14 23:58


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def scatter_with_visualmap_size():
    scatter = Scatter(init_opts=opts.InitOpts(theme='light',
                                              width='1000px',
                                              height='600px'))
    scatter.add_xaxis(Faker.choose())
    scatter.add_yaxis('', Faker.values())
    scatter.set_global_opts(visualmap_opts=opts.VisualMapOpts(type_='size'))
    return scatter


if __name__ == '__main__':
    chart = scatter_with_visualmap_size()
    chart.render(path='chart_output/scatter_with_visualmap_size.html')
