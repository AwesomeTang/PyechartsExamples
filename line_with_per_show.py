#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : line_with_per_show.py
# @Version : Python 3.7
# @Time    : 2020-11-27 22:23


from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode


x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [0.98, 0.89, 0.92, 1.07, 0.81, 1.23]

js = """function (param) {return param.name +':'+ Math.floor(param.value[1])+'%';}"""


def line_with_per_show():
    line = Line(init_opts=opts.InitOpts(theme='light',
                                        width='1000px',
                                        height='600px'))
    line.add_xaxis(x_data)
    # 传入数据时先乘以100
    line.add_yaxis('', [round(v * 100, 0) for v in y_data])
    #
    line.set_series_opts(label_opts=opts.LabelOpts(is_show=True,
                                                   formatter=JsCode(js)))

    return line


if __name__ == '__main__':
    chart = line_with_per_show()
    chart.render(path='chart_output/line_with_per_show.html')
