# README



## Tutorial

- intuition
  - 由ida2vec引入主题模型的学习
  - ida huge-math basis， 入门到放弃
  - 当前主要了解
- LDA
  - 本文件夹下有具体的学习md
- Sentence







## Familia

- [github-wiki](<https://github.com/baidu/Familia/wiki>)

### 摘录

- “主题”通常被定义为一系列语义相关的词

- LDA中采用文档内的Bag-of-Words假设，词与词之间的位置信息是被忽略的。
- 主题模型在工业界的应用范式可以分为两类：语义表示和语义匹配

### 语义表示

- 主题模型产生的==主题分布==可看做文档的==语义表示==
- 









## 临时记录

- 计算文本相似度的方法
  - 在一个某github主的文本主题相似度计算方法？？==待==





## 整体思路

- 先完成工程上的事情，并注意要讲的内容，然后再挖掘出学术（吹水）的内容



## 个人思考

- 主题分布是文本处理的特征工程部分？
- 语义表示(文档级别，即主题分布)的方法
  - 文档的在主题上的多项分布(LDA, SentenceLDA等模型代表这类文档的表征学习)
    - LDA
      - 快速实现
        - kaggle
    - SentenceLDA
  - 联合使用主题向量和文档主题分布
    - Doc2vec
      - [论文]
      - 快速实现
        - gensim
    - LDA2vec
      - [论文]
    - TEWV
      - [论文]
    - Topic Word Embeddings
      - [论文](http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/download/9314/9535/)

## 项目安排

- 先执行LDA2vec的表示学习，进行基本的语义表示，直接fork好了
  - 语义表示的两种方法(放在lda或者说是方法的主题的主题分布)
  - 文档的主题分布可以看作是文档的语义表示
  - 做新闻质量分类，新闻聚类，新闻网页内容丰富度
    - 新闻质量分类使用XGboost做实验，新闻聚类使用K-means，内容丰富度(如何计算主题分布的信息熵？)