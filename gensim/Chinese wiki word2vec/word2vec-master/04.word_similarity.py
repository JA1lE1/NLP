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


def word_similarity(word, model):
    semi = ''
    try:
        semi = model.most_similar(word, topn=10)
    except KeyError:
        print('The word not in vocabulary!')
    for term in semi:
        print('%s,%s' % (term[0], term[1]))


if __name__ == '__main__':
    ## 配日志输出
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(logging.INFO)
    logging.info("running %s" % ' '.join(sys.argv))

    _config = Config()
    # 读取模型
    model = Word2Vec.load(_config.embedded_model_t2s)
    # model.save_word2vec_format('embedding_model_t2s/zhwiki_embedding_t2s.model.bin', binary=True)
    # 取相似的词
    print(model.vocab)
    word_similarity(['腾讯', '百度'], model)