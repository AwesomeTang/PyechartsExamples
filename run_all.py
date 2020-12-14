#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : run_all.py
# @Version : Python 3.7
# @Time    : 2020-11-29 19:08

import os
from tqdm import tqdm


root = os.getcwd()

# 建立文件夹
if not os.path.exists(os.path.join(root, 'chart_output')):
    os.mkdir(os.path.join(root, 'chart_output'))

# 排除文件
exclude_file = ['run_all.py']

for file in tqdm(os.listdir(root)):
    if file in exclude_file:
        break
    if file.split('.')[-1] == 'py':
        # noinspection PyBroadException
        try:
            os.system('python3 {}'.format(file))
        except Exception as info:
            print('execute file {} failed.'.format(file))
            print(info)
