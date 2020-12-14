#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : pie_with_custom_label.py
# @Version : Python 3.7
# @Time    : 2020-11-14 16:21

from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


def pie_with_custom_label():
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    pie.add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    pie.set_series_opts(
        label_opts=opts.LabelOpts(position='top',
                                  color='red',
                                  font_family='Arial',
                                  font_size=12,
                                  font_style='italic',
                                  interval=1,
                                  formatter='{b}:{d}%'
                                  )
    )

    return pie


if __name__ == '__main__':
    chart = pie_with_custom_label()
    chart.render(path='chart_output/pie_with_custom_label.html')
