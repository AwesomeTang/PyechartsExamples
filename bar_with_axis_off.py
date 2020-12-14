#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_with_axis_off.py
# @Version : Python 3.7
# @Time    : 2020-11-15 15:32


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def bar_with_axis_off():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('', Faker.values())
    # 碰上类目标签过长的时候，可以选择关闭坐标轴，直接显示在图形中
    bar.set_series_opts(label_opts=opts.LabelOpts(position='insideLeft', formatter='{b}:{c}'))
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=False),
                        yaxis_opts=opts.AxisOpts(is_show=False))
    bar.reversal_axis()
    return bar


if __name__ == '__main__':
    chart = bar_with_axis_off()
    chart.render(path='chart_output/bar_with_axis_off.html')
