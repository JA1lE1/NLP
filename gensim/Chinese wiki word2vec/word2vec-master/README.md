# word2vec
基于 gensim 的 wiki 词向量


### 步骤
#### 下载基于文本

```
curl -o data/zhwiki/zhwiki-latest-pages-articles.xml.bz2 https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
```

#### WikiCorpus获取原始文本数据

```
python 01.xml2string.py
```

#### 使用OpenCC将繁体字转换为简体字

```
$ cd /data/zhwiki/
$ opencc -i zhwiki_raw.txt -o zhwiki_t2s.txt -c t2s.json
```

#### 文本数据分词

```
python 02.word_segment.py
```

#### gensim word2vec训练

```
python 03.word2vec.py
```

#### 加载模型预览效果

```
python 04.word_similarity.py
```

#### 附：tensorboard 可视化

生成可视化

```
python w2v_visualizer.py embedding_model_t2s/zhwiki_embedding_t2s.model visualize_result
```

运行结果
```
Using TensorFlow backend.
2017-09-02 23:15:04.010950: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-09-02 23:15:04.010973: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-09-02 23:15:04.010978: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-09-02 23:15:04.010982: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
Run `tensorboard --logdir=visualize_result` to run visualize result on tensorboard
```

运行可视化

```
tensorboard --logdir=visualize_result
```

### 链接

http://www.52nlp.cn/%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91%E8%AF%AD%E6%96%99%E4%B8%8A%E7%9A%84word2vec%E5%AE%9E%E9%AA%8C

https://segmentfault.com/a/1190000008173404?from=timeline

https://segmentfault.com/a/1190000010129248