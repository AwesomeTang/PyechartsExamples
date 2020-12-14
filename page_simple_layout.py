#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : page_simple_layout.py
# @Version : Python 3.7
# @Time    : 2020-11-15 21:35

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def page_simple_layout():
    # 图表1
    bar_1 = Bar(init_opts=opts.InitOpts(theme='light',
                                        width='500px',
                                        height='300px'))
    bar_1.add_xaxis(Faker.choose())
    bar_1.add_yaxis('A', Faker.values())
    bar_1.add_yaxis('B', Faker.values())

    # 图表2
    bar_2 = Bar(init_opts=opts.InitOpts(theme='light',
                                        width='500px',
                                        height='300px'))
    bar_2.add_xaxis(Faker.choose())
    bar_2.add_yaxis('A', Faker.values())
    # x,y轴翻转
    bar_2.reversal_axis()

    # 图表3
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='500px',
                                        height='300px'))
    line.add_xaxis(Faker.choose())
    line.add_yaxis('A', Faker.values())
    line.add_yaxis('B', Faker.values())

    # 图表4
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='500px',
                                      height='300px'))
    pie.add("",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            radius=["40%", "75%"])

    page = Page(layout=Page.SimplePageLayout)
    # 需要自行调整每个 chart 的 height/width，布局会因为页面大小而不同
    page.add(bar_1, bar_2, line, pie)

    return page


if __name__ == '__main__':
    chart = page_simple_layout()
    chart.render(path='chart_output/page_simple_layout.html')
