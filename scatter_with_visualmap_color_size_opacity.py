#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : scatter_with_visualmap_color_size_opacity.py
# @Version : Python 3.7
# @Time    : 2020-11-15 17:59

from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = [random.randint(0, 100) for _ in range(30)]
y_data = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
          for _ in range(30)]


def scatter_with_visualmap_color_size_opacity():
    scatter = Scatter(init_opts=opts.InitOpts(theme='light',
                                              width='1000px',
                                              height='600px'))
    scatter.add_xaxis(x_data)
    scatter.add_yaxis('', y_data)
    # dimension制定数据维度
    scatter.set_global_opts(visualmap_opts=[opts.VisualMapOpts(is_show=True, type_='size', dimension=2, pos_top='10%'),
                                            opts.VisualMapOpts(is_show=True, type_='color', dimension=3, pos_top='40%'),
                                            opts.VisualMapOpts(is_show=True, type_='opacity', dimension=4,
                                                               # VisualMapOpt中对于range_opacity没给默认值，需要自行设定
                                                               range_opacity=[0.2, 1], pos_top='70%')],
                            xaxis_opts=opts.AxisOpts(type_="value"))
    return scatter


if __name__ == '__main__':
    chart = scatter_with_visualmap_color_size_opacity()
    chart.render(path='chart_output/scatter_with_visualmap_color_size_opacity.html')
