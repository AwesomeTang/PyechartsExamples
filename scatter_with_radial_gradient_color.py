#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : scatter_with_radial_gradient_color.py
# @Version : Python 3.7
# @Time    : 2020-11-28 12:28

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode

color_js = """new echarts.graphic.RadialGradient(
                    0.4, 0.3, 1,
                    [{offset: 0,
                      color: '#F8F8FF'},
                     {offset: 1,
                      color: '#00BFFF'}
                      ])"""


def scatter_with_radial_gradient_color():
    scatter = Scatter(init_opts=opts.InitOpts(theme='light',
                                              width='1000px',
                                              height='600px'))
    scatter.add_xaxis(Faker.choose())

    scatter.add_yaxis("", Faker.values(),
                      symbol_size=50,
                      # 渐变配色
                      itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_js)))
    return scatter


if __name__ == '__main__':
    chart = scatter_with_radial_gradient_color()
    chart.render(path='chart_output/scatter_with_radial_gradient_color.html')
