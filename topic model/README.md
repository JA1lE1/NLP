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
    - Word2vec
    - Doc2vec
      - [论文]
      - 快速实现
        - gensim
    - LDA2vec
      - [论文]
      - [DataCamp参考](<https://www.datacamp.com/community/tutorials/lda2vec-topic-model>)
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
- 先爬数据吧
  - 过程中接着模型的学习





## 杂货铺

- 对于整个的研究环境还不是很了解
- **fastText >> GloVe > word2vec** ？？？？
  - 对于语言模型
    - [掘进post](<https://juejin.im/entry/5a6af990f265da3e283a3b42>)
    - 图书馆借的书
  - 对于文本分类
    - [参考](<https://zhuanlan.zhihu.com/p/46331902>)

- 我的理解是topic model 作为NLP的表征学习部分，它能够被用于作为很多种NLP任务的前期工程，就像语言模型一样

  - 属于Social Science Applications 社会学应用？

- 知乎参考

  - > 作者：王政
    >
    > 链接：https://www.zhihu.com/question/298517764/answer/539556869
    >
    > 来源：知乎
    >
    > 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    >
    > 对于模型本身来说，只有对于特定任务的适用或者不适用，而没有先进不先进只说。
    >
    > 我看到的这个问题是“目前有比主题模型（topic model）更先进的 文本分类/聚类方式么？”——我的理解是，主题模型在哪些任务上适用，哪些不适用。
    >
    > ------
    >
    > 首先是以文本表示为基础的文本相似度分析，我认为这个可以代表不同文本表示在一般文本分类任务上的能力水平。众所周知，TF-IDF、LDA、word embedding是三种主流文本表示方式。根据Topical Word Embeddings 的报告可知，在文本相似度的评测中结合LDA和word embedding的TWE-1能够取得最好效果。
    >
    > 作者的方法是，先训练LDA，然后将每个词和词对应的topic一起作为中心词进行训练。从结论可以看出，适当的结合topic model的稀疏性，能够得到state-of-the-art的文本表示方法。特别要注意的是，“适当”在这里不是一句空话，因为这个文章还提出了TWE-2，TWE-3两个模型。这两个模型更深的结合了topic model的稀疏性，但是效果并不理想。
    >
    > ------
    >
    > 然后是文本聚类任务，这点请首先看楼上霍华德博士的观点。主题模型的主要优点是不会像判别模型一样，由于labels太多导致性能迅速下降。因为在判别模型中，labels判别的基础是二分类模型。而labels对于documents，符合齐普夫定律，即大量的labels只被赋予了很少数的documents。这样，二分类模型面对的情况就是阴性数据和阳性数据数量极端不平衡，导致性能下降。

- 了解一下Fastext



## 查阅文献的方法

- 谷歌各大顶会
  - 然后在对应的网址ctrl+f 查topic
    - eg 在[ACL2018](<https://acl2018.org/programme/papers/>) 查 topic
    - 然后稀里糊涂找了一篇Combining Deep Learning and Topic Modeling for Review Understandingin Context-Aware Recommendation （这篇可在NAACL 2018 中找到）
- 顶会ACL、EMNLP、NAACL