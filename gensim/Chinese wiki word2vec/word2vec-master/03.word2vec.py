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

from gensim.models.word2vec import Word2Vec, LineSentence
import sys, logging, os.path
import multiprocessing
from config import Config


if __name__ == '__main__':
    ## 配日志输出
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(logging.INFO)
    logging.info("running %s" % ' '.join(sys.argv))

    _config = Config()
    input_file = os.path.join(_config.data_path, _config.zhwiki_seg_t2s)
    output_file = os.path.join(_config.embedded_model_t2s)
    # LineSentence 复制读取，并按照前面的分词进行读取
    # 计算词向量模型
    model = Word2Vec(LineSentence(input_file), size=100, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.save(output_file)
    print(model.wv.index2word)


