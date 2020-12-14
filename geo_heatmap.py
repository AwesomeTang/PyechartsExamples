#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : geo_heatmap.py
# @Version : Python 3.7
# @Time    : 2020-11-15 14:19


from pyecharts.charts import *
from pyecharts import options as opts


def geo_heatmap():
    geo = Geo(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))

    geo.add_schema(maptype="china")

    geo.add("",
            [("广州", 150), ("北京", 70), ("深圳", 64), ("上海", 74),  ("杭州", 63)],
            type_='heatmap')
    # 热点图必须配置visualmap_opts
    geo.set_global_opts(visualmap_opts=opts.VisualMapOpts())
    return geo


if __name__ == '__main__':
    chart = geo_heatmap()
    chart.render(path='chart_output/geo_heatmap.html')
