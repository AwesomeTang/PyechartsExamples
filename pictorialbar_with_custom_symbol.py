#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : pictorialbar_with_custom_symbol.py
# @Version : Python 3.7
# @Time    : 2020-11-15 01:37


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def pictorialbar_with_custom_symbol():
    pictorialbar = PictorialBar(init_opts=opts.InitOpts(theme='light',
                                                        width='1000px',
                                                        height='600px'))
    pictorialbar.add_xaxis(Faker.choose())
    pictorialbar.add_yaxis('A',
                           Faker.values(),
                           symbol_size=20,
                           symbol='path://M100,0 L41.22,180.90 L195.10,69.09 L4.89,69.09 L158.77,180.90 z',
                           symbol_repeat="fixed",
                           is_symbol_clip=True
                           )

    return pictorialbar


if __name__ == '__main__':
    chart = pictorialbar_with_custom_symbol()
    chart.render(path='chart_output/pictorialbar_with_custom_symbol.html')
