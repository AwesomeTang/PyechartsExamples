#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_with_dict_config.py
# @Version : Python 3.7
# @Time    : 2020-11-14 23:12


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_dict_config():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('', Faker.values())
    bar.set_series_opts(itemstyle_opts=dict(color='#008B8B', opacity=0.8))
    return bar


if __name__ == '__main__':
    chart = bar_with_dict_config()
    chart.render(path='chart_output/bar_with_dict_config.html')
