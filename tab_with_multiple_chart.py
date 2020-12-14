#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : tab_with_multiple_chart.py
# @Version : Python 3.7
# @Time    : 2020-11-15 03:05

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def tab_with_multiple_chart():
    # 图表1
    bar = Bar()
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis("商家A", Faker.values())
    bar.add_yaxis("商家B", Faker.values())

    # 图表2
    line = Line()
    line.add_xaxis(Faker.choose())
    line.add_yaxis("商家A", Faker.values())
    line.add_yaxis("商家B", Faker.values())

    # 先通过Grid将图表1和图表2组合起来
    grid = Grid()
    grid.add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
    grid.add(line, grid_opts=opts.GridOpts(pos_top="60%"))

    # 再将Grid添加到Tab
    tab = Tab()
    tab.add(grid, '示例')

    return tab


if __name__ == '__main__':
    chart = tab_with_multiple_chart()
    chart.render(path='chart_output/tab_with_multiple_chart.html')
