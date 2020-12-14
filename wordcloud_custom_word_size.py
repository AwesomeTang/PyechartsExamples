#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : wordcloud_custom_word_size.py
# @Version : Python 3.7
# @Time    : 2020-11-15 02:09


from pyecharts.charts import *
from pyecharts import options as opts
import random

text = """
I used to rule the world
Seas would rise when I gave the word
Now in the morning I sleep alone
Sweep the streets I used to own
I used to roll the dice
Feel the fear in my enemy eyes
Listen as the crowd would sing
Now the old king is dead
Long live the king
One minute I held the key
Next the walls were closed on me
And I discovered that my castles stand
Upon pillars of salt and pillars of sand
I hear Jerusalem bells are ringing
Roman Cavalry choirs are singing
Be my mirror my sword and shield
My missionaries in a foreign field
For some reason I can't explain
Once you go there was never
Never an honest word
That was when I ruled the world
"""

word_list = set(text.split(' '))

words = [(word, random.randint(1, 100)) for word in word_list]


def wordcloud_custom_word_size():
    wordcloud = WordCloud(init_opts=opts.InitOpts(theme='light',
                                                  width='1000px',
                                                  height='600px'))
    wordcloud.add('',
                  words,
                  word_size_range=[10, 50])

    return wordcloud


if __name__ == '__main__':
    chart = wordcloud_custom_word_size()
    chart.render(path='chart_output/wordcloud_custom_word_size.html')
