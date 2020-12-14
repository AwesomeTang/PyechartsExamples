#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : line_with_shadow.py
# @Version : Python 3.7
# @Time    : 2020-11-01 13:05

from pyecharts.charts import *
from pyecharts import options as opts
import random

line_style = {
    'normal': {
        'width': 4,  # 设置线宽
        'shadowColor': 'rgba(155, 18, 184, .3)',  # 阴影颜色
        'shadowBlur': 10,  # 阴影大小
        'shadowOffsetY': 10,  # Y轴方向阴影偏移
        'shadowOffsetX': 10,  # x轴方向阴影偏移
        'curve': 0.5  # 线弯曲程度，1表示不弯曲
    }
}

x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

# 随机生成点数据
y_data_1 = [i + random.randint(10, 20) for i in range(len(x_data))]
y_data_2 = [i + random.randint(15, 25) for i in range(len(x_data))]


def line_with_shadow():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    line.add_yaxis("Android",
                   y_data_1,
                   is_symbol_show=False,
                   is_smooth=True,
                   # 传入线风格参数
                   linestyle_opts=line_style)
    line.add_yaxis("IOS",
                   y_data_2,
                   is_symbol_show=False,
                   is_smooth=True,
                   # 传入线风格参数
                   linestyle_opts=line_style)
    line.set_global_opts(title_opts=opts.TitleOpts(title="终端日活趋势"))
    return line


if __name__ == '__main__':
    chart = line_with_shadow()
    chart.render(path='chart_output/line_with_shadow.html')
