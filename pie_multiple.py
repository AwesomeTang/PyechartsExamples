#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : pie_multiple.py
# @Version : Python 3.7
# @Time    : 2020-11-15 00:08


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def pie_multiple():
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='800px'))
    pie.add("",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            center=["25%", "50%"])

    pie.add("",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            center=["75%", "50%"])

    return pie


if __name__ == '__main__':
    chart = pie_multiple()
    chart.render(path='chart_output/pie_multiple.html')
