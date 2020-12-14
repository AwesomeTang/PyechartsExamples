#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : timeline_auto_play.py
# @Version : Python 3.7
# @Time    : 2020-11-15 02:53

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def timeline_auto_play():
    timeline = Timeline(init_opts=opts.InitOpts(theme='light',
                                                width='1000px',
                                                height='600px'))
    timeline.add_schema(is_auto_play=True,  # 自动播放
                        is_loop_play=True  # 循环播放
                        )
    for year in range(2000, 2020):
        bar = Bar()
        bar.add_xaxis(['香蕉', '梨子', '水蜜桃', '核桃', '西瓜', '苹果', '菠萝'])
        bar.add_yaxis('A', Faker.values())
        bar.add_yaxis('B', Faker.values())
        timeline.add(bar, '{}年'.format(year))
    return timeline


if __name__ == '__main__':
    chart = timeline_auto_play()
    chart.render(path='chart_output/timeline_auto_play.html')
