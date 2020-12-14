#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : bar_with_animation.py
# @Version : Python 3.7
# @Time    : 2020-11-15 16:08

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker

"""
更多动画效果可参见：https://echarts.apache.org/examples/zh/editor.html?c=line-easing
"""


def bar_with_animation():
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px',
                                      animation_opts=opts.AnimationOpts(animation_delay=1000,   # 动画延时
                                                                        animation_easing='bounceIn')
                                      )
              )
    bar.add_xaxis(Faker.choose())
    bar.add_yaxis('A', Faker.values())
    bar.add_yaxis('B', Faker.values())
    return bar


if __name__ == '__main__':
    chart = bar_with_animation()
    chart.render(path='chart_output/bar_with_animation.html')
