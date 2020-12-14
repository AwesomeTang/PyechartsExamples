#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : scatter_with_custom_bgColor.py
# @Version : Python 3.7
# @Time    : 2020-11-15 17:53

from pyecharts.charts import *
from pyecharts import options as opts
import random


x_data = [random.randint(0, 100) for _ in range(30)]
y_data = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for _ in range(30)]


def scatter_with_custom_bgColor():
    scatter = Scatter(
        init_opts=opts.InitOpts(theme='light',
                                width='1000px',
                                height='600px',
                                bg_color='#008B8B'))
    scatter.add_xaxis(x_data)
    scatter.add_yaxis('', y_data)
    # dimension制定数据维度
    scatter.set_global_opts(visualmap_opts=[opts.VisualMapOpts(is_show=True, type_='size', dimension=2),
                                            opts.VisualMapOpts(is_show=True, type_='color', dimension=3)],
                            xaxis_opts=opts.AxisOpts(type_="value"))
    return scatter


if __name__ == '__main__':
    chart = scatter_with_custom_bgColor()
    chart.render(path='chart_output/scatter_with_custom_bgColor.html')
