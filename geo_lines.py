#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : geo_lines.py
# @Version : Python 3.7
# @Time    : 2020-11-15 14:16


from pyecharts.charts import *
from pyecharts import options as opts


def geo_lines():
    geo = Geo(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))

    geo.add_schema(maptype="china")

    geo.add("广州出发",
            # 数据格式（from， to）
            [("广州", "上海"), ("广州", "北京"), ("广州", "西宁"), ("广州", "重庆")],
            type_='lines')
    geo.add("成都出发",
            # 数据格式（from， to）
            [("成都", '长沙'), ("成都", "武汉"), ("成都", "长春"), ("成都", "南京")],
            type_='lines')

    return geo


if __name__ == '__main__':
    chart = geo_lines()
    chart.render(path='chart_output/geo_lines.html')
