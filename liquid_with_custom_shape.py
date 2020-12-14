#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : liquid_with_custom_shape.py
# @Version : Python 3.7
# @Time    : 2020-11-22 10:23


from pyecharts.charts import *
from pyecharts import options as opts

ios_icon = 'path://M24.734 17.003c-0.040-4.053 3.305-5.996 3.454-6.093-1.88-2.751-4.808-3.127-5.851-3.171-2.492-0.252-4.862 1.467-6.127 1.467-1.261 0-3.213-1.43-5.28-1.392-2.716 0.040-5.221 1.579-6.619 4.012-2.822 4.897-0.723 12.151 2.028 16.123 1.344 1.944 2.947 4.127 5.051 4.049 2.026-0.081 2.793-1.311 5.242-1.311s3.138 1.311 5.283 1.271c2.18-0.041 3.562-1.981 4.897-3.931 1.543-2.255 2.179-4.439 2.216-4.551-0.048-0.022-4.252-1.632-4.294-6.473zM20.705 5.11c1.117-1.355 1.871-3.235 1.665-5.11-1.609 0.066-3.559 1.072-4.713 2.423-1.036 1.199-1.942 3.113-1.699 4.951 1.796 0.14 3.629-0.913 4.747-2.264z'


def liquid_with_custom_shape():
    liquid = Liquid(init_opts=opts.InitOpts(theme='light',
                                            width='1000px',
                                            height='600px'))
    liquid.add('', [0.4, 0.5], shape=ios_icon)

    return liquid


if __name__ == '__main__':
    chart = liquid_with_custom_shape()
    chart.render(path='chart_output/liquid_with_custom_shape.html')
