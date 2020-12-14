#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : pie_custom_radius.py
# @Version : Python 3.7
# @Time    : 2020-11-15 00:06


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def pie_custom_radius():
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    pie.add("",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            radius=["40%", "75%"])

    return pie


if __name__ == '__main__':
    chart = pie_custom_radius()
    chart.render(path='chart_output/pie_custom_radius.html')
