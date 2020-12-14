#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : map_with_viusalmap.py
# @Version : Python 3.7
# @Time    : 2020-11-21 01:02


from pyecharts.charts import *
from pyecharts import options as opts

data = [('广东', 10430),
        ('山东', 9579),
        ('河南', 9402),
        ('四川', 8041),
        ('江苏', 7866),
        ('河北', 7185),
        ('湖南', 6568),
        ('安徽', 5950),
        ('湖北', 5724),
        ('浙江', 5442),
        ('广西', 4603),
        ('云南', 4597),
        ('江西', 4457),
        ('辽宁', 4375),
        ('黑龙江', 3831),
        ('陕西', 3733),
        ('山西', 3571),
        ('福建', 3552),
        ('贵州', 3477),
        ('重庆', 2884),
        ('吉林', 2746),
        ('甘肃省', 2557),
        ('内蒙古', 2471),
        ('台湾', 2316),
        ('上海', 2301),
        ('新疆', 2181),
        ('北京', 1961),
        ('天津', 1294),
        ('海南', 867),
        ('香港', 710),
        ('宁夏', 630),
        ('青海', 562),
        ('西藏', 300),
        ('澳门', 55)]


def map_with_viusalmap():
    map_chart = Map(init_opts=opts.InitOpts(theme='light',
                                            width='1000px',
                                            height='600px'))
    map_chart.add('人口（万人）',
                  data_pair=data,
                  maptype='china',
                  # 关闭symbol的显示
                  is_map_symbol_show=False)

    map_chart.set_global_opts(visualmap_opts=opts.VisualMapOpts(
        max_=10430,  # visualmap默认映射数据范围是【0，100】，需调整
        is_piecewise=True,
        range_color=["#CCD3D9", "#E6B6C2", "#D4587A", "#DC364C"]
    ))
    return map_chart


if __name__ == '__main__':
    chart = map_with_viusalmap()
    chart.render(path='chart_output/map_with_viusalmap.html')
