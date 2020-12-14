#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : geo_effect_scatter.py
# @Version : Python 3.7
# @Time    : 2020-11-15 14:24

from pyecharts.charts import *
from pyecharts import options as opts


def geo_effect_scatter():
    geo = Geo(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))

    geo.add_schema(maptype="china")

    geo.add("",
            [("广州", 150), ("北京", 70), ("长沙", 64), ("上海", 74),  ("厦门", 63)],
            type_='effectScatter')

    return geo


if __name__ == '__main__':
    chart = geo_effect_scatter()
    chart.render(path='chart_output/geo_effect_scatter.html')
