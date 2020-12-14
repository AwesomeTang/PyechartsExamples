#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : calendar_custom_cell.py
# @Version : Python 3.7
# @Time    : 2020-11-20 23:25

from pyecharts.charts import *
from pyecharts import options as opts
import datetime

# 美国covid确诊数据
data = [(datetime.datetime(2020, 1, 21, 0, 0), 1), (datetime.datetime(2020, 1, 22, 0, 0), 1),
        (datetime.datetime(2020, 1, 23, 0, 0), 1), (datetime.datetime(2020, 1, 24, 0, 0), 2),
        (datetime.datetime(2020, 1, 25, 0, 0), 2), (datetime.datetime(2020, 1, 26, 0, 0), 5),
        (datetime.datetime(2020, 1, 27, 0, 0), 5), (datetime.datetime(2020, 1, 28, 0, 0), 5),
        (datetime.datetime(2020, 1, 29, 0, 0), 5), (datetime.datetime(2020, 1, 30, 0, 0), 5),
        (datetime.datetime(2020, 1, 31, 0, 0), 7), (datetime.datetime(2020, 2, 1, 0, 0), 8),
        (datetime.datetime(2020, 2, 2, 0, 0), 8), (datetime.datetime(2020, 2, 3, 0, 0), 11),
        (datetime.datetime(2020, 2, 4, 0, 0), 11), (datetime.datetime(2020, 2, 5, 0, 0), 11),
        (datetime.datetime(2020, 2, 6, 0, 0), 11), (datetime.datetime(2020, 2, 7, 0, 0), 11),
        (datetime.datetime(2020, 2, 8, 0, 0), 11), (datetime.datetime(2020, 2, 9, 0, 0), 11),
        (datetime.datetime(2020, 2, 10, 0, 0), 11), (datetime.datetime(2020, 2, 11, 0, 0), 12),
        (datetime.datetime(2020, 2, 12, 0, 0), 12), (datetime.datetime(2020, 2, 13, 0, 0), 13),
        (datetime.datetime(2020, 2, 14, 0, 0), 13), (datetime.datetime(2020, 2, 15, 0, 0), 13),
        (datetime.datetime(2020, 2, 16, 0, 0), 13), (datetime.datetime(2020, 2, 17, 0, 0), 13),
        (datetime.datetime(2020, 2, 18, 0, 0), 13), (datetime.datetime(2020, 2, 19, 0, 0), 13),
        (datetime.datetime(2020, 2, 20, 0, 0), 13), (datetime.datetime(2020, 2, 21, 0, 0), 15),
        (datetime.datetime(2020, 2, 22, 0, 0), 15), (datetime.datetime(2020, 2, 23, 0, 0), 15),
        (datetime.datetime(2020, 2, 24, 0, 0), 15), (datetime.datetime(2020, 2, 25, 0, 0), 15),
        (datetime.datetime(2020, 2, 26, 0, 0), 15), (datetime.datetime(2020, 2, 27, 0, 0), 16),
        (datetime.datetime(2020, 2, 28, 0, 0), 16), (datetime.datetime(2020, 2, 29, 0, 0), 24),
        (datetime.datetime(2020, 3, 1, 0, 0), 30), (datetime.datetime(2020, 3, 2, 0, 0), 53),
        (datetime.datetime(2020, 3, 3, 0, 0), 73), (datetime.datetime(2020, 3, 4, 0, 0), 104),
        (datetime.datetime(2020, 3, 5, 0, 0), 174), (datetime.datetime(2020, 3, 6, 0, 0), 222),
        (datetime.datetime(2020, 3, 7, 0, 0), 337), (datetime.datetime(2020, 3, 8, 0, 0), 451),
        (datetime.datetime(2020, 3, 9, 0, 0), 519), (datetime.datetime(2020, 3, 10, 0, 0), 711),
        (datetime.datetime(2020, 3, 11, 0, 0), 1109), (datetime.datetime(2020, 3, 12, 0, 0), 1561),
        (datetime.datetime(2020, 3, 13, 0, 0), 2157), (datetime.datetime(2020, 3, 14, 0, 0), 2870),
        (datetime.datetime(2020, 3, 15, 0, 0), 2968), (datetime.datetime(2020, 3, 16, 0, 0), 4360),
        (datetime.datetime(2020, 3, 17, 0, 0), 6141), (datetime.datetime(2020, 3, 18, 0, 0), 8914),
        (datetime.datetime(2020, 3, 19, 0, 0), 14153), (datetime.datetime(2020, 3, 20, 0, 0), 19479),
        (datetime.datetime(2020, 3, 21, 0, 0), 25818), (datetime.datetime(2020, 3, 22, 0, 0), 33756),
        (datetime.datetime(2020, 3, 23, 0, 0), 43845), (datetime.datetime(2020, 3, 24, 0, 0), 54108),
        (datetime.datetime(2020, 3, 25, 0, 0), 66044), (datetime.datetime(2020, 3, 26, 0, 0), 84080),
        (datetime.datetime(2020, 3, 27, 0, 0), 102254), (datetime.datetime(2020, 3, 28, 0, 0), 122054),
        (datetime.datetime(2020, 3, 29, 0, 0), 141194), (datetime.datetime(2020, 3, 30, 0, 0), 162690),
        (datetime.datetime(2020, 3, 31, 0, 0), 188701), (datetime.datetime(2020, 4, 1, 0, 0), 214194),
        (datetime.datetime(2020, 4, 2, 0, 0), 244593), (datetime.datetime(2020, 4, 3, 0, 0), 276535),
        (datetime.datetime(2020, 4, 4, 0, 0), 309699), (datetime.datetime(2020, 4, 5, 0, 0), 337573),
        (datetime.datetime(2020, 4, 6, 0, 0), 367210), (datetime.datetime(2020, 4, 7, 0, 0), 397992),
        (datetime.datetime(2020, 4, 8, 0, 0), 429686), (datetime.datetime(2020, 4, 9, 0, 0), 464442),
        (datetime.datetime(2020, 4, 10, 0, 0), 497943), (datetime.datetime(2020, 4, 11, 0, 0), 527958),
        (datetime.datetime(2020, 4, 12, 0, 0), 556517), (datetime.datetime(2020, 4, 13, 0, 0), 581810),
        (datetime.datetime(2020, 4, 14, 0, 0), 608845), (datetime.datetime(2020, 4, 15, 0, 0), 637974),
        (datetime.datetime(2020, 4, 16, 0, 0), 669272), (datetime.datetime(2020, 4, 17, 0, 0), 701996),
        (datetime.datetime(2020, 4, 18, 0, 0), 730317), (datetime.datetime(2020, 4, 19, 0, 0), 756375),
        (datetime.datetime(2020, 4, 20, 0, 0), 783716), (datetime.datetime(2020, 4, 21, 0, 0), 809213),
        (datetime.datetime(2020, 4, 22, 0, 0), 837414), (datetime.datetime(2020, 4, 23, 0, 0), 871617),
        (datetime.datetime(2020, 4, 24, 0, 0), 907908), (datetime.datetime(2020, 4, 25, 0, 0), 940829),
        (datetime.datetime(2020, 4, 26, 0, 0), 968517), (datetime.datetime(2020, 4, 27, 0, 0), 990993),
        (datetime.datetime(2020, 4, 28, 0, 0), 1015518), (datetime.datetime(2020, 4, 29, 0, 0), 1042926),
        (datetime.datetime(2020, 4, 30, 0, 0), 1072667)]


def calendar_custom_cell():
    calendar = Calendar(init_opts=opts.InitOpts(theme='light',
                                                width='1000px',
                                                height='600px'))
    calendar.add('确证人数',
                 yaxis_data=data,
                 label_opts=opts.LabelOpts(is_show=True),
                 calendar_opts=opts.CalendarOpts(
                     # 日历位置
                     pos_top='10%',
                     pos_left='10%',
                     # 日期范围
                     range_=['2020-01-21', '2020-04-30'],
                     # 日历单元格尺寸
                     cell_size=50,
                     # 年月日标签样式设置
                     yearlabel_opts=opts.CalendarYearLabelOpts(margin=40,
                                                               label_font_size=20,
                                                               label_color='rgba(130,134,112,0.8)'),
                     daylabel_opts=opts.CalendarDayLabelOpts(label_color='#778633', label_font_weight='bold'),
                     monthlabel_opts=opts.CalendarMonthLabelOpts(label_color='#778633', label_font_weight='bold')
                 )
                 )
    # 设置视觉组件
    calendar.set_global_opts(visualmap_opts=opts.VisualMapOpts(
        max_=1000000,
        is_piecewise=True,
        pieces=[{"min": 1000000},
                {"min": 10000, "max": 1000000},
                {"min": 100, "max": 10000},
                {"max": 100}],
        range_color=["#CCD3D9", "#E6B6C2", "#D4587A", "#DC364C"]
    ))
    return calendar


if __name__ == '__main__':
    chart = calendar_custom_cell()
    chart.render(path='chart_output/calendar_custom_cell.html')
