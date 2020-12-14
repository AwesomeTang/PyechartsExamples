#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : line_with_custom_mark_point.py
# @Version : Python 3.7
# @Time    : 2020-11-14 16:56

from pyecharts.charts import *
from pyecharts import options as opts
import random

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data = [i + random.randint(10, 20) for i in range(len(x_data))]


def line_with_custom_mark_point():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    line.add_yaxis('', y_data)
    # 自定义标记点
    line.set_series_opts(
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(name="自定义标记点", coord=[x_data[2], y_data[2]], value=y_data[2])]
        )
    )

    return line


if __name__ == '__main__':
    chart = line_with_custom_mark_point()
    chart.render(path='chart_output/line_with_custom_mark_point.html')
