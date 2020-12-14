#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_custom_legend_symbol.py
# @Version : Python 3.7
# @Time    : 2020-11-21 01:16

from pyecharts.charts import *
from pyecharts import options as opts
import random

ios_icon = 'path://M24.734 17.003c-0.040-4.053 3.305-5.996 3.454-6.093-1.88-2.751-4.808-3.127-5.851-3.171-2.492-0.252-4.862 1.467-6.127 1.467-1.261 0-3.213-1.43-5.28-1.392-2.716 0.040-5.221 1.579-6.619 4.012-2.822 4.897-0.723 12.151 2.028 16.123 1.344 1.944 2.947 4.127 5.051 4.049 2.026-0.081 2.793-1.311 5.242-1.311s3.138 1.311 5.283 1.271c2.18-0.041 3.562-1.981 4.897-3.931 1.543-2.255 2.179-4.439 2.216-4.551-0.048-0.022-4.252-1.632-4.294-6.473zM20.705 5.11c1.117-1.355 1.871-3.235 1.665-5.11-1.609 0.066-3.559 1.072-4.713 2.423-1.036 1.199-1.942 3.113-1.699 4.951 1.796 0.14 3.629-0.913 4.747-2.264z'
android_icon = 'path://M28 12c-1.1 0-2 0.9-2 2v8c0 1.1 0.9 2 2 2s2-0.9 2-2v-8c0-1.1-0.9-2-2-2zM4 12c-1.1 0-2 0.9-2 2v8c0 1.1 0.9 2 2 2s2-0.9 2-2v-8c0-1.1-0.9-2-2-2zM7 23c0 1.657 1.343 3 3 3v0 4c0 1.1 0.9 2 2 2s2-0.9 2-2v-4h4v4c0 1.1 0.9 2 2 2s2-0.9 2-2v-4c1.657 0 3-1.343 3-3v-11h-18v11zM24.944 10c-0.304-2.746-1.844-5.119-4.051-6.551l1.001-2.001c0.247-0.494 0.047-1.095-0.447-1.342s-1.095-0.047-1.342 0.447l-1.004 2.009-0.261-0.104c-0.893-0.297-1.848-0.458-2.84-0.458s-1.947 0.161-2.84 0.458l-0.261 0.104-1.004-2.009c-0.247-0.494-0.848-0.694-1.342-0.447s-0.694 0.848-0.447 1.342l1.001 2.001c-2.207 1.433-3.747 3.805-4.051 6.551v1h17.944v-1h-0.056zM13 8c-0.552 0-1-0.448-1-1s0.447-0.999 0.998-1c0.001 0 0.002 0 0.003 0s0.001-0 0.002-0c0.551 0.001 0.998 0.448 0.998 1s-0.448 1-1 1zM19 8c-0.552 0-1-0.448-1-1s0.446-0.999 0.998-1c0 0 0.001 0 0.002 0s0.002-0 0.003-0c0.551 0.001 0.998 0.448 0.998 1s-0.448 1-1 1z'

x_data = ["2020/7/{}".format(i + 1) for i in range(10)]

# 随机生成点数据
y_data_1 = [random.randint(10, 20) for i in range(len(x_data))]
y_data_2 = [random.randint(15, 25) for i in range(len(x_data))]


def bar_custom_legend_symbol():
    # 当前并不支持同一个图表针对不同的系列设置不同的icon
    # 方案是将多个系列的数据拆分到多个图表设置各自的icon，最后通过grid将图表组合起来
    ios_bar = Bar()
    ios_bar.add_xaxis(x_data)
    ios_bar.add_yaxis('IOS', y_data_1)
    ios_bar.set_global_opts(legend_opts=opts.LegendOpts(legend_icon=ios_icon,
                                                        pos_right='15%'))

    az_bar = Bar()
    az_bar.add_xaxis(x_data)
    az_bar.add_yaxis('Android', y_data_2)
    az_bar.set_global_opts(legend_opts=opts.LegendOpts(legend_icon=android_icon,
                                                       pos_right='5%'))

    # 将az_bar和ios_bar组合起来
    grid = Grid(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    grid.add(ios_bar, is_control_axis_index=True, grid_opts=opts.GridOpts())
    grid.add(az_bar, is_control_axis_index=True, grid_opts=opts.GridOpts())
    return grid


if __name__ == '__main__':
    chart = bar_custom_legend_symbol()
    chart.render(path='chart_output/bar_custom_legend_symbol.html')
