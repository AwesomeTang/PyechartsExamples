#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : geo_add_custom_coordinate.py
# @Version : Python 3.7
# @Time    : 2020-11-15 13:27


from pyecharts.charts import *
from pyecharts import options as opts


def geo_add_custom_coordinate():
    geo = Geo(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    # 添加自定义坐标点
    geo.add_coordinate('x', 116.397428, 39.90923)
    geo.add_coordinate('y', 112.398615, 29.91659)

    geo.add_schema(maptype="china")
    geo.add("", [('x', 1), ('y', 2)])

    return geo


if __name__ == '__main__':
    chart = geo_add_custom_coordinate()
    chart.render(path='chart_output/geo_add_custom_coordinate.html')
