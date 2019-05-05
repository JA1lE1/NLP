#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: dingdayu
@contact: 614422099@qq.com
@blog: http://blog.dingxiaoyu.com
@version: 1.0
@license: Apache Licence
@file: w2v_visualizer.py
@time: 2017-08-28 19:59:21
"""

from __future__ import print_function
from gensim.corpora import WikiCorpus
from config import Config
import os


if __name__ == '__main__':
    i = 0
    output = open(os.path.join(Config().data_path, Config().zhwiki_raw), 'w', encoding='utf8')
    # lemmatize=False: 不使用pattern模块来进行英文单词的词干化处理
    wiki = WikiCorpus(os.path.join(Config().data_path, Config().zhwiki_bz2).replace('\\', '/'), lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(' '.join(text) + '\n')
        i += 1
        if i % 10000 == 0:
            print('Saved ' + str(i) + ' articles')

    output.close()
    print('Finished Saved ' + str(i) + ' articles')
