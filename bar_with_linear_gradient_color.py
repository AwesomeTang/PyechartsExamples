#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_with_linear_gradient_color.py
# @Version : Python 3.7
# @Time    : 2020-11-01 13:32

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode

color_js = """
            new echarts.graphic.LinearGradient(
                                0, 
                                1, 
                                0, 
                                0,
                                [{offset: 0, color: '#008B8B'}, 
                                 {offset: 1, color: '#FF6347'}], 
                                false)
           """


def bar_with_linear_gradient_color():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('', Faker.values(),
                  itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_js)))

    return bar


if __name__ == '__main__':
    chart = bar_with_linear_gradient_color()
    chart.render(path='chart_output/bar_with_linear_gradient_color.html')
