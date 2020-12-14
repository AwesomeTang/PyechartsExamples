#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_with_default_selected_series.py
# @Version : Python 3.7
# @Time    : 2020-11-14 16:52


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_default_selected_series():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    # 默认选中A C
    bar.add_yaxis('A', Faker.values(), is_selected=True)
    bar.add_yaxis('B', Faker.values(), is_selected=False)
    bar.add_yaxis('C', Faker.values(), is_selected=True)
    return bar


if __name__ == '__main__':
    chart = bar_with_default_selected_series()
    chart.render(path='chart_output/bar_with_default_selected_series.html')
