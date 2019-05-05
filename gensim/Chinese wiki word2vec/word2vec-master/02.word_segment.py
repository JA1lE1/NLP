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

import jieba
import re
import os
from config import Config


def str_filter(line):
    return re.sub('[：·•’!\"#$%&\'()*+，,-./:：;；<=>?@，。?★、…【】《》？“”〞‘’！[\\]^_`{}（）~]+', "", line)


if __name__ == '__main__':
    _config = Config()
    input_file = open(os.path.join(_config.data_path, _config.zhwiki_raw), "r", encoding='utf8')
    output_file = open(os.path.join(_config.data_path, _config.zhwiki_seg_t2s), "w", encoding='utf8')

    i = 0
    while True:
        line = input_file.readline()
        if line:
            line = str_filter(line.strip())
            seg_list = list(jieba.cut(line))
            new_line = []
            for item in seg_list:
                # 分词后得到中文或部分标点，才允许追加到行中
                if re.compile(u'[\u4e00-\u9fa5]+').search(item) or \
                        re.compile("[\"”“，？?\,\.。,0-9]+").search(item):
                    new_line.append(item)

            segments = ' '.join(new_line)
            output_file.write(segments)
            i += 1
            if i % 10000 == 0:
                print('segment: ' + str(i) + ' .')
        else:
            break
    output_file.close()



