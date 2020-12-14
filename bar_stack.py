#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_stack.py
# @Version : Python 3.7
# @Time    : 2020-11-14 23:36


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_stack():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    # stack值一样的系列会堆叠在一起
    bar.add_yaxis('A', Faker.values(), stack='stack1')
    bar.add_yaxis('B', Faker.values(), stack='stack1')
    bar.add_yaxis('C', Faker.values(), stack='stack2')
    return bar


if __name__ == '__main__':
    chart = bar_stack()
    chart.render(path='chart_output/bar_stack.html')
