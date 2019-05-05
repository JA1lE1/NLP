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

class Config:
    data_path = 'data/zhwiki'
    zhwiki_bz2 = 'zhwiki-latest-pages-articles.xml.bz2'
    zhwiki_raw = 'zhwiki_raw.txt'
    zhwiki_t2s = 'zhwiki_t2s.txt'
    zhwiki_raw_t2s = 'zhwiki_raw_t2s.txt'   ### 更改
    zhwiki_seg_t2s = 'zhwiki_seg.txt'
    embedded_model_t2s = 'embedding_model_t2s/zhwiki_embedding_t2s.model'
    embedded_vector_t2s = 'embedding_model_t2s/vector_t2s'
