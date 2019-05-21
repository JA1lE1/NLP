# README

## 5.21 代码理解

### 代码块（explore）

- 以最新的new_explore.py为主

#### 导入模块

#### 主函数

- 定义超参数

  - 这里需要==后期维护更新==

- 变量==tokenized_docs== 

  - ==data_prepare的返回值处理结果==

    - ```python
      tokenized_docs = [(i, doc) for i, doc in enumerate(data_prepare())]
      #type(tokenized_docs)
      <class 'list'>
      # tokenized_docs[0]  (有省略)
      (0, ['欧几里得', '西元前', '世纪', '古希腊', '数学家', '几何', '父', '此画', '拉斐尔', '作品', '雅典', '学院', '数学', '利用', '符号语言', '研究', '数量', '结构', '变化', '空间', '概念', '一门', '学科', '某种''究生', '中学老师', '学生', '数学', '学习', '资源', '互联网', '数学', '学习', '资源', '教学', '视频', '英汉', '对照', '数学', '用语', '英汉', '对照', '数学', '用语'])
      ```

- remove short documents

  - 删除短的文章 （开头设置超参数）

  - ==疑问==

    - ```python
      # 计算较短文章的个数
      n_short_docs = sum(1 for i, doc in tokenized_docs if len(doc) < min_length)
      ```

    - 测试

      - ```python
        sum(1 for i_ in range(3) if i_ > 1)
        1
        sum(2 for i_ in range(3) if i_ > 1)
        2
        sum(3 for i_ in range(3) if i_ > 1)
        3
        ```

- remove some tokens

  - 删掉出现次数过多的token 和次数过少的token

- 生成数据

  - 以encoded_docs 来生成 具体看==变量==部分的==data== 
    - 使用==get_windows 函数==
  - 生成gensim训练所需要的text 这里是将encoded_docs 的doc（以数字组成的doc）转成‘645’，‘234’ 这种格式的doc

- word2vec预训练

- 将训练好的词（这里是‘234’ 这种词形式）向量 用numpy格式保存

  - ```python
    word_vectors = np.zeros((vocab_size, embedding_dim)).astype('float32')
    for i in decoder:
        word_vectors[i] = model.wv[str(i)]
    ```

- 为训练LDA做准备（==这个需要结合官方和其他的lda实验加深理解==）

  - 这次输入的corpus是真是的txt，然后应该是用方法的训练方法 用到了

    - ```python
      dictionary = corpora.Dictionary(texts)
      ```

    - 可能是为了更好地Interprete

  - texts 格式

    - ```python
      ['世纪', '古希腊', '数学', '研究', '结构', '概念', '形式', '科学', '一种', '数学', '计算', '概念', '数学', '古希腊', '数学',  '哲学', '数学', '数学', '数学', '数学', '一个', '数学', '数学', '一个', '数学', '一个', '数学', '一个', '研究', '数学', '文化', '数学', '数学', '数学', '数学']
      ```

  - dictionary

    - ```python
      dictionary = corpora.Dictionary(texts)
      corpus = [dictionary.doc2bow(text) for text in texts]
      #Convert `document` into the bag-of-words (BoW) format = list of `(token_id, token_count)
      #eg
      >>> from gensim.corpora import Dictionary
                  >>> dct = Dictionary(["máma mele maso".split(), "ema má máma".split()])
                  >>> dct.doc2bow(["this", "is", "máma"])
                  [(2, 1)]
                  >>> dct.doc2bow(["this", "is", "máma"], return_missing=True)
                  ([(2, 1)], {u'this': 1, u'is': 1})
      
      ```

    - 注意Dictionary是一个class类 有很多的Attribute 具体见。。。以上是doc2bow的方法返回的词袋模型

- LDA

  - ```python
    lda = models.LdaModel(corpus, alpha=0.9, id2word=dictionary, num_topics=n_topics)
    corpus_lda = lda[corpus]
    # lda 的训练 并且显示各个文章的主题分布 主题个数是超参数 可以设置
    # 这里要注意的是第二句 是否可以用于和训练数据无关的数据
    # 参数alpha的意义是？？？
    ## debug
    corpus_lda[1]
    [(5, 0.015422589), (19, 0.09541435), (22, 0.8042764)]
    corpus_lda[0]
    [(8, 0.8839177), (18, 0.010522466)]
    #  以 第二篇文章 下标为1 这里表示第五个主题 0.00xxx 第22个主题占得最多
    # 但是主题是否需要将word显示出来一下呢 不然我怎么标记主题的名字
    lda.show_topics貌似可以
    ```

  - ==变量== doc_weights_init

    - 存储的是每篇文章的主题分布

    - ```
      doc_weights_init[i, j] = prob
      # i 代表的是 第i篇文章 j代表的是第j个主题 prob代表的是响应的概率
      ```

##### 保存的变量

- data
- word_vectors
- unigram_distribution
- decoder
- doc_weights_init

##### 可能出现的隐患

- 我把 *np.save('doc_decoder.npy', doc_decoder)* 这个注释了 代码中的响应处理也注释了 不过貌似有问题的 ==待==
- 

####  辅助函数

##### ==data_prepare==

- 使用WikiCorpous 处理wiki语料 xml的压缩文件(==这里可以作为下一步工作的入手点==)

- 载入停用词词典

- 使用wikicorpus生成器载入text数据节省内存，每次读入一篇文章

  - ```
    for text in wiki.get_texts():
            text = ' '.join(text)
            text = HanziConv.toSimplified(text)
            #re.sub('[：·•’!\"#$%&\'()*+，,-./:：;；<=>?@，。?★、…【】《》？“”〞‘’！[\\]^_`{}（）~]+', "", text)
            text = text.strip()
            seg_list = list(jieba.cut(text))
            # ['歐幾里', '得', ' ', '西元前', '三世', '紀的', '古希臘', '數學家', ' ', '現在', '被', '認
            #  '是', '幾何', '之父', ' ', '此畫', '為拉斐爾', '的', '作品', ' ', '雅典', '學院']
            new_text = [x for x in seg_list  if  (re.compile(u'[\u4e00-\u9fa5]+').search(x) or \
                            re.compile("[\"”“，？?\,\.。,0-9]+").search(x)) and (x not in stopwords)]
    ```

  - text 是list 变量 将其转成字符串 用 '  '.join(text)的方法转成str的格式方便分词

    - ```
      '歐幾里得 西元前三世紀的古希臘數學家 現在被認為是幾何之父 此畫為拉斐爾的作品 雅典學院 数学 是利用符号语言研究數量 结构 变化以及空间等概念和研究生 以及中学老师和学生 数学学习资源 互联网上数学学习资源和教学视频 英漢對照數學用語 archive 英漢對照數學用語 albany bureau of bilingual education see profile at archive'
      ```

  - 繁体化成简体

  - 使用str.strip()删掉空格的等？？

  - 转成seg_list分词后的list形式的txt数据

    - ```
      ['欧几里得', ' ', '西元前', '三', '世纪', '的', '古希腊', '数学家', ' ', '现在', '被', '认为', '是', '几何', '之', '父', ' ', '此画', '为', '拉斐尔', '的', '作品', ' ', '雅典', '学院', ' ', '数学', ' ', '是', '利用', '符号语言', '研究', '数量', ', '其', '形容词', ' ', '意思', '为', ', ' ', '秦九韶', '的', ' ', '数学', '九章', ' ', '永乐'' ', '英汉', '对照', '数学', '用语', ' ', 'archive', ' ', '英汉', '对照', '数学', '用语', ' ', 'albany', ' ', 'bureau', ' ', 'of', ' ', 'bilingual', ' ', 'education', ' ', 'see', ' ', 'profile', ' ', 'at', ' ', 'archive']
      ```

    - 可以看到有空格和英文，因此使用正则保存只有中文的字符

  - 使用正则后 返回 单个文档的text （list形式） ==使用yield== 的方法节省内存的使用

##### _count_unique_tokens

- ```python
  # 数据形式
  ['欧几里得', '西元前', '世纪', '古希腊', '数学家', '几何', '父', '此画', '拉斐尔', '作品', '雅典', '学院', '数学', '利用', '符号语言', '研究', '数量', '结构', '变化', '空间', '概念', '一门', '学科', '某种', '角度看', '形式', '科学', '一种', '数学', '透过', '抽象化', '逻辑推理', '计数', '计算', '数学家', '拓展', '概念', '数学', '基本概念', '完善', '早', '古埃及', '古希腊', '严谨', '数学', '发展', '持续', '小幅', '方哲学', '论题', '张汝伦', '哲学', '出路', '在于', '智慧', '张汝伦', '张汝伦', '哲学', '无用', '之用', '扩展', '阅读', '艾伦', '布洛克', '艾伦', '布洛克', '入门', '专题', '介绍', '选集', '陈荣捷', '参考', '作', '陈荣捷']
  ```

- 目的

  - 将所有的文档转成所有的token组成的doc 如上所示（有删减）

- 返回值 

  - Counter 格式

    - ```python
      #count elements from a string
      c = Counter('abcdeabcdabcaba')  # count elements from a string
      
      c.most_common(3)                # three most common elements
          [('a', 5), ('b', 4), ('c', 3)]
      sorted(c)                       # list all unique elements
          ['a', 'b', 'c', 'd', 'e']
      ''.join(sorted(c.elements()))   # list elements with repetitions
          'aaaaabbbbcccdde'
      sum(c.values())                 # total of all counts
      ```

    - 

##### _remove_tokens

- 输入 
  - 

- total_tokens_count
  - 计算所有的token的数量
- unknown_tokens_count
  - 计算所有的**过大出现次数**的token和**过少出现次数**的token的数量之和
- 返回值
  - 返回值依然是所有token组成的list，这次加了删掉上述的unknown token

##### _create_token_encoder

- 输入
  - counts
  - _count_unique_tokens的输出结果 Counter的形式

- total_tokens_count
  - 计算所有的token的数量

- 返回值

  - encoder， decoder， word_counts

  - ```python
    encoder[token] = i
    decoder[i] = token
    word_counts.append(count)
    # 注：这个word_counts 是为了后面的Negative Sampling 按照token的出现次数多寡进行排序组成list，元素是token出现的次数
    ```

##### _encode

- 使用encoder将txt转为数字

- 返回的格式和tokenized_docs 的格式一致

  - ```
    # encoded_docs[0]
    (0, [13, 39, 3, 6, 37, 25, 22, 18, 20, 3, 19, 25, 3, 39, 3, 16, 13, 27, 3, 16, 3, 28, 7, 21, 18, 32, 3, 16, 6, 3, 6, 7, 38, 26, 7, 3, 39, 18, 3, 6, 3, 7, 22, 7, 22, 25, 3, 10, 27, 3, 3, 3, 3, 3, 3, 10, 3,12, 3, 12, 6, 3, 45, 3, 3, 3, 3])
    ```

  - 

### 变量

- data

  - ```python
    data = np.load('data.npy')
    #这个data是数据预处理是get_windows后的数据结果，它旨在生成数据集(),注意数值是text decode 后的数值型数据
    data = begining + inside + end
    #三个格式都是list，
    #eg. inside 
    inside[0] = (145, [687, 1649, 15, 46, 113, 963, 1650, 964, 67, 688])
    inside_txt= (decoder[inside[0][0]],[decoder[context] for context in inside[0][1]])
    inside_txt
    ('几何', ['欧几里得', '西元前', '世纪', '古希腊', '数学家', '父', '此画', '拉斐尔', '作品', '雅典'])
    # 这个地方一方面我们看到分词的时候把 三世纪 的三 给删掉了（stop words） 一方面还把是删掉了 可见这个stopwords需要整改
    # begining
    beginning_txt
    ('欧几里得', ['西元前', '世纪', '古希腊', '数学家', '几何', '父', '此画', '拉斐尔', '作品', '雅典'])
    
    
    ## 原因
    #txt的前后的字符在5个(window_size)以内的中间的字符数据生成的训练数据是不一样的
    ##最终格式
    tes = (1,[1,2,3]) + (2,[3,4,5])
    tes
    (1, [1, 2, 3], 2, [3, 4, 5])
    #最后的形式应该是[[1,2,3,4.....],[[1,2,3],[3,4,5],[xxx],....[xxx]]
    
    [0, 687] + [1649, 15, 46, 113, 145, 963, 1650, 964, 67, 688]
    = [0, 687, 1649, 15, 46, 113, 145, 963, 1650, 964, 67, 688]
    
    # data 没有转成numpy的最后的形式，转成numpy可以理解为 为pytorch的dataloader服务
    # 下面是data的element的基本的形式
    data[0]
    [0, 687, 1649, 15, 46, 113, 145, 963, 1650, 964, 67, 688]
    data[-1]
    [9, 850, 4410, 714, 34, 2, 904, 848, 591, 259, 4411, 907]
    # 这里我只有测试10篇doc 因此最后的是doc序号是9(以下标1开始)
    # 而我们可以看出是data这里是将所有的语料库转为每个word(pivotol)的形式的数据(基于skgram模型)但是 这样做会有一个问题 内存爆炸！！！（因此python如何释放内存呢？）
    ```

- unigram_distribution

  - ```python
    # 目的应该是为了negative sampling
    # 来源
    word_counts = np.array(word_counts)
    unigram_distribution = word_counts/sum(word_counts)
    # word_counts 来源
    def _create_token_encoder(counts):
    
        total_tokens_count = sum(
            count for token, count in counts.most_common()
        )
        print('total number of tokens:', total_tokens_count)
    
        encoder = {}
        decoder = {}
        word_counts = []
        i = 0
    
        for token, count in counts.most_common():
            # counts.most_common() is in decreasing count order
            #def most_common(n=None)
            #List the n most common elements and their counts from the most common to 		  #the least. If n is None, then list all element counts.
    		#Counter('abcdeabcdabcaba').most_common(3) [('a', 5), ('b', 4), ('c', 3)]
            encoder[token] = i
            decoder[i] = token
            word_counts.append(count)
            i += 1
    
        return encoder, decoder, word_counts
    
    ##
    ```

### 代码块（train）

- 开头

  - > ​    *# transform to logits*
    >
    > ​    doc_weights_init **=** np.log(doc_weights_init **+** 1e-4)
    >
    > ​    *# make distribution softer*
    >
    > ​    temperature **=** 7.0
    >
    > ​    doc_weights_init **/=** temperature
    >
    > ​    *# if you want to train the model like in the original paper*
    >
    > ​    *# set doc_weights_init=None*
    >
    > ///   这个是神马意思呢？？

#### 变量

- doc_ids



#### 代码句

```python
unique_docs, counts = np.unique(doc_ids, return_counts=True)
# np.unique 的使用见下面的调试过程
xy = [2,3,2,33,2,3,4,1]
a, s = np.unique(xy, return_counts=True)
a
array([ 1,  2,  3,  4, 33])
s
array([1, 3, 2, 1, 1], dtype=int64)
# s返回的是xy 中元素的出现的次数 对应的是a的元素
```



#### pytorch

- unsqueeze

  - ```
    >>> a = torch.tensor([1,2])
    >>> a.unsqueeze(0)
    tensor([[1, 2]])
    >>> a.unsqueeze(1)
    tensor([[1],
            [2]])
    ```

  - 就是0 是最外面的元素套一个[], 1是倒数第二层的元素套一个【】，以此类推



## 5.20 代码理解

- intuition
  - 上次exp1预训练完lda 和 word2vec貌似有问题在train上都出现了问题，毫无疑问的是代码需要理解一下



## 5.19 整理exp1的经验，exp2 遇到的问题

- exp2

  - debug

    - ```
      number of documents: 313241
      number of windows: 41679315
      number of topics: 25
      vocabulary size: 267969
      word embedding dim: 50
      /home/jupyter/explore_chinese_lda2vec/utils/lda2vec_loss.py:47: UserWarning: nn.init.normal is now deprecated in favor of nn.init.normal_.
        init.normal(self.doc_weights.weight, std=DOC_WEIGHTS_INIT)
      number of batches: 5815
      epoch 1
        0%|                                                                                                                                                             | 0/5815 [00:00<?, ?it/s]
      /home/jupyter/explore_chinese_lda2vec/utils/lda2vec_loss.py:196: UserWarning: Implicit dimension choice for softmax has been deprecated. Change the call to include dim=X as an argument.
        doc_probs = F.softmax(doc_weights)
        
      Traceback (most recent call last):
        File "train.py", line 36, in <module>
          main()
        File "train.py", line 32, in main
          save_every=20, grad_clip=5.0
        File "/home/jupyter/explore_chinese_lda2vec/utils/training.py", line 127, in train
          neg_loss, dirichlet_loss = model(doc_indices, pivot_words, target_words)
        File "/usr/local/lib/python3.5/dist-packages/torch/nn/modules/module.py", line 493, in __call__
          result = self.forward(*input, **kwargs)
        File "/home/jupyter/explore_chinese_lda2vec/utils/lda2vec_loss.py", line 70, in forward
          doc_vectors = self.topics(doc_weights)
        File "/usr/local/lib/python3.5/dist-packages/torch/nn/modules/module.py", line 493, in __call__
          result = self.forward(*input, **kwargs)
        File "/home/jupyter/explore_chinese_lda2vec/utils/lda2vec_loss.py", line 206, in forward
          doc_vectors = (unsqueezed_doc_probs*unsqueezed_topic_vectors).sum(1)
      RuntimeError: The size of tensor a (35) must match the size of tensor b (25) at non-singleton dimension 1
      ```

    - 

## 5.17

- 先行进行gensim的官方tutorial 然后对比与之区别，现在版本更新很快需要及时更新代码的version 

###  新的想法

- 尝试一下最新的gensim的训练方法和存储方式
- 写下原来的程序的思路
- 在gensim官方上查看最新的方法进行更新

#### 训练方法

- 直接开始尝试

### 原来的思路

##### 数据准备

- wiki.get_text() 获得yield返回的list，因其含有繁体且是list 没法分词，因此先转成str 再化成简体再分词，分完词后转成list类型
  - 这相当于训练的数据准备，==附加产品有encoder，decoder genism 现在肯定有对应的可以找一下== 至于word_counts 记录字典中每个token出现的个数，是一个==debug== ，用于后面算==算unigram distribution==
  - preprocess 的最后返回值 encoded_docs 是 文档的编码换成字典中对应的数字代码，decoder就是id-》token ，word_counts就是list，中含有每个字典中的token的个数降序排序，只保留有数值
  - ==以上内容需要debug，并给出example==

##### Get unigram distribution

==这个还不知道是干嘛用==

##### 词向量预训练

- ```python
  texts = [[str(j) for j in doc] for i, doc in encoded_docs]
  # 最骚的是忙活了半天 又换一个格式
  model.init_sims(replace=True)
  # 这个是干嘛用的
  # 参数
  workers=4, sg=1, negative=15, iter=70  # 这几个参数是干嘛用的
  ```

- 最后词向量训练完成后它使用numpy去保存此项来那个 word_vectors 这里相当于\i    vecotr \ i 就是decoder的序号， vector就是训练的向量

- 导入的参数 texts 是encoded_docs 我感觉有点不妥 也没必要 ==可以但没必要==

- ==参数==

  - ==worker==
    - The `workers` parameter only has an effect if you have [Cython](http://cython.org/) installed. Without Cython, you’ll only be able to use one core because of the [GIL](https://wiki.python.org/moin/GlobalInterpreterLock) (and `word2vec` training will be [miserably slow](http://rare-technologies.com/word2vec-in-python-part-two-optimizing/)).
  - ==sg==
    - 0 for CBOW , 1 for skip-gram
  - iter
    - 训练扫描语料库的次数

- ==训练出来有bug啊==

  - print(model)
    ''''   Word2Vec(vocab=518, size=50, alpha=0.025)  ''''
  - 分析可能是因为版本的原因
  - ==原因==
    - 是mini_count 的原因 mini_count de

 #### Prepare initialization for document weights

- ==使用gensim做lda的实验==

### gensim 

- 

### 新python module

- smart_open

## 5.16

- intuition
  - 做物理实验，从小到大，电梯的建造不是直接建一个很大的模型直接开始重复实验
  - 做庞大的语料库实验，应该也是sample的方式进行实验
- 而这个在本地的wing ide的实验正是我要做的
- 后记
  - 看来还是有压力才能去做好一件事情，昨天的我在人工智能课的压力下，其实发掘出蛮多东西的

### 实验内容

- 参考[中大的博客](<https://www.cnblogs.com/chenbjin/p/5638904.html>)
  - 做一下wiki语料，做一下sougou新闻，做一下xml型的数据(fork中南git)，做一下自己爬的语料库信息
- 实验预计future work
  - 数据表示的topic model 的类型，进一步看ACL NAACL的最新论文
  - 下一步是多线程并行爬取实验，spark hadoop实验
  - 这些完事可以了解知识表示，知识工程的做法



### Debug 记录

####  cn-explore

```python
len(doc)
3
doc
[12, 14, 16]
new_text
['經濟學', '一門', '产品', '服务', '生产', '分配', '以及', '消费', '进行', '研究', '社會', '科學', '西方', '语言', '经, '首要', '規範', '經濟學', '獲得', '答案', '不僅', '如此', '微觀', '經濟', '學還', '分析', '市場', '失靈', '描述', '市場', '理論', '應當', '狀況', '信息', '市場', '經濟', '發展', '經濟', '發展', '一種', '個體', '經濟學', '概念', '並且', ', '經濟學', '資源', '網站', '麻省理f', 'social', 'production', 'springer', 'berlin', 'fabian', 'lindner', 'investment', 'accounting', 'as', 'an', 'indispensable', 'guide', 'to', 'economic', 'theory', 'institut', 'makro', 'konomie', 'und']
#这里发现这里的new_text 很符合要求，但是有问题它值保存了一篇article 具体见代码
#这里我是删掉字符个数<2的token， 还需要扫描停用词字典吗？？？（未） 但是读起来 我自己都不知道它是个什么鸟
#上面这个删掉len(t) < xx 的方法是 英文的做法， 中文不能这样做  可能 英文单词中 字母个数 2个及 2个一下的 和中文停用词差不多
# 我发现这里面确实
# 所以 我需要参考在gensim中文wiki词训练的时候 的一些正则 并且去除停用词 参考中大lda实验 并且进行繁简转换
# 还有关于分词 如何在不加字典的情况下更好地进行分词
len(new_text)
3848
' '.join(new_text)
'歐幾里 西元前 三世 紀的 古希臘 數學家 現在 認為 幾何 之父 此畫 為拉斐爾 作品 雅典 學院 数学 利用 符号语言 研究 數量 结构 变化 以atical香港科技大学 数学网 一个 数学史 为主 网站 怎樣 研習 純數學 或統 計學 本科 基礎 研究 課程 參考 書目 数学 文化 主要 面向 大学生 大学老师 研究生 以及 中学老师 学生 数学 学习 资源 互联网 数学 学习 资源 教学 视频 英漢 對照 數學 用語 archive 英漢 對照 數學 用語 albany bureau of bilingual education see profile at archive'
# 注：这里为了方便查看 删了很多的东西
# 这里发现分完词后并没有像在en-explore 中一样 或者说是
doc_de= ' '.join(new_text)
' '.join(doc_de.split())
'歐幾里 西元前 三世 紀的 古希臘 數學家 現在 認為 幾何 之父 此畫 為拉斐爾 作品 雅典 學院 数学 利用 符号语言 研究 數量 结构 变化 以及 空间 概念 一門 学科 某种 角度看 形式 科學 一種 數學 透過 抽象化 邏 團體 一份 數值 分析 研究 有什麼 計算 方法 file gravitation space source png 數學 物理 file svg 數學 流體 力學 file composite trapezoidal rule illustration small svg 數值 分析 file maximum boxed png 最佳化 file two red dice svg 概率论 file oldfaithful png 統計學 file market data index nya on utc png 計量 金融 file arbitrary gametree solved响 参见 數學 哲學 數學遊戲 數學家 列表 教育 算經十書 數學 競賽 数学题 参考书目 benson donald the moment of proof mathematical epiphanies oxford university press usa new ed edition december isbn boyer car oxford univertics wide world publishing revised edition june isbn peterson ivars mathematical tourist new and updated snapshots of modern mathematics owl books isbn 参考 网址 rusin dave the mathematical atlas 英文版 现代 数語 archive 英漢 對照 數學 用語 albany bureau of bilingual education see profile at archive'
texe_de= ' '.join(doc_de.split())
lis_de = [t for t in texe_de if len(texe_de) > 1] 
lis_de
['歐', '幾', '里', '', ' ', '非', '歐', ' ', '幾', '里', ' ', '幾', '何', ' ', '及', '拓', ' ', '撲', '學', ' ', '數', '和', '空', '間', ' ', '解', '析', ' ', '幾', '何', ' ', '結', '合', ' ', '數', '和', '空', '間', ' ', '概', '念', ' ', '著', '拓', ' ', '研', '究', ' ', '結', '合', ' ', '結', '構', ' ', '空', '間', ' ', '李', '群', ' ', '研', '究', ' ', '空', '間', ' ', '結', '構', ' ', '變', '化', ' ', '許', '多', ' ', '分', '支', ' ', '包', '含', ' ', '存', '在', ' ', '已', '久', ' ', '龐', '加'相', '信', ' ', '問', '題', ' ', '解', '答', ' ', '否', '定', ' ', 'p', 'x', ' ', 'p', 'x', ' ', 'p', 'x', ' ', '組', '合', ' ', '數', '學', ' ', '計', '算', '理', '論', ' ', '密', '碼', '學', ' ', '圖', '論', ' ', '應', '用', ' ', '數', '學', ' ', '工', '商', ' ', '及', '其', ' ', '領', '域', ' ', '現', '實', ' ', m', ' ', 'b', 'o', 'x', 'e', 'd', ' ', 'p', 'n', 'g', ' ', '最', '佳', '化', ' ', 'f', 'i', 'l', 'e', ' ', 't', 'w', 'o', ' ', 'r', 'e' 'l', ' ', 'e', 'd', 'u', 'c', 'a', 't', 'i', 'o', 'n', ' ', 's', 'e', 'e', ' ', 'p', 'r', 'o', 'f', 'i', 'l', 'e', ' ', 'a', 't', ' ', 'a', 'r', 'c', 'h', 'i', 'v', 'e']
## 可以发现这里的话 token被限制在了一个字
```

en-explore

```python

texe_de_en = "\n\nI am sure some bashers of Pens fans are pretty confused about the lack\nof any kind of posts about the recent Pens massacre of the Devils. Actually,\nI am  bit puzzled too and a bit relieved. However, I am going to put an end\nto non-PIttsburghers' relief with a bit of praise for the Pens. Man, they\nare killing those Devils worse than I thought. Jagr just showed you why\nhe is much better than his regular season stats. He is also a lot\nfo fun to watch in the playoffs. Bowman should let JAgr have a lot of\nfun in the next couple of games since the Pens are going to beat the pulp out of Jersey anyway. I was 
import spacy
# 少了导入模型
text_en_de =  nlp(text_en_de)
resu_de = [t.lemma_ for t in text_en_de if len(t) >2]
resu_de
['sure', 'some', 'basher', 'Pens', 'fan', 'be', 'pretty', 'confused', 'about', 'the', 'lack', 'any', 'kind', 'post', 'about', 'the', 'recent', 'Pens', 'massacre', 'the', 'Devils', 'actually', 'bit', 'puzzled', 'too', 'and', 'bit', 'relieved', 'however', 'go', 'put', 'end', 'non', 'PIttsburghers', 'relief', 'with', 'bit', 'praise', 'for', 'the', 'Pens', 'man', '-PRON-', 'be', 'kill', 'those', 'devil', 'bad', 'than', 'think', 'Jagr', 'just', 'show', '-PRON-', 'why', 'much', 'well', 'than', '-PRON-', 'regular', 'season', 'stat', 'also', 'lot', 'fun', 'watch', 'the', 'playoff', 'Bowman', 'should', 'let', 'JAgr', 'have', 'lot', 'fun', 'the', 'next', 'couple', 'game', 'since', 'the', 'Pens', 'be', 'go', 'beat', 'the', 'pulp', 'out', 'Jersey', 'anyway', 'be', 'very', 'disappointed', 'not', 'see', 'the', 'Islanders', 'lose', 'the', 'final', 'regular', 'season', 'game', 'pens', 'RULE']
# 可以发现 这里token很完美是一个 单词
```

#### 新功能debug

- 正则 删除英文和空格

  - ```
    (0, ['歐幾里', '得', '西元前', '三世', '紀的', '古希臘', '數學家', '現在', '被', '認為', '是', '幾何', '之父', '此畫', '為拉斐爾', '的', '作品', '雅典', '學院', '数学', '是', '利用', '符号语言', '研究', '數量', '结构', '变化', '以及', '空间', '等', '概念', '的', '一門', '学科', '从', '某种', '角度看', '屬', '於', '形式', '科學', '的', '一種', '數學', '透過', '抽象化', '學', '本身', '的', '实质性', '內容', '而', '不以', '任何', '實際', '應用', '為', '目標', '雖然', ', '数学', '学习', '资源', '和', '教学', '视频', '英漢', '對照', '數學', '用語', '英漢', '對照', '數學', '用語'])
    
    ```

- 繁简转换

  - ```
    (0, ['欧几里得', '西元前', '三', '世纪', '的', '古希腊', '数学家', '现在', '被', '认为', '是', '几何', '之', '父', '此画', '为', '拉斐尔', '的', '作品', '雅典', '学院', '数学', '是', '利用', '符号语言', '研究', '数量', '结构', '变化', '以及', '空间', '等', '概念', '的', '一门', '学科', '从', '某种', '角度看', '属于', '形式', '科学', '的', '一种', '数学', '透过', '抽象化', '和', '逻辑推理', '的', '使用', '由', '计数', '计算', '数学家', '们', '拓展', '这些', '概念', '对', '数学', '基本概念', '的', '完善', '早', '在', '古埃及', '而', '在', '古希腊', '那里', '有', '更为', '严谨', '的', '处理', '从', '那时', '开始', '数学', '的', '发展', '便', '持续', '不断', '地', '小幅', '进展', '世纪', '的', '文艺复兴', '时期', '致使', '数学', '的', '加速', '发展', '直至', '今日', '今日', '数学', '使用', '在', '不同', '的', '领域', '中', '包括', '科学', '工程', '医学', '经济学', '和', '金融学', '等', '有时', '亦', '会', '激起', '新', '的', '数学', '发现', '并', '导致', '全新', '学科', '的', '发展', '数学家', '也', '研究', '纯数学', '数学', '竞赛', '数学题', '註', '记', '参考书目', '数学', '百科全书', '牛津', '英语词典', '参考', '网址', '英文版', '现代', '数学', '漫游', '一个', '在线', '的', '数学', '百科全书', '数学', '另', '一个', '在线', '的', '数学', '百科全书', '一个', '包含', '数学', '物理', '数学知识', '香港科技大学', '数学网', '一个', '以', '数学史', '为主', '的', '网站', '怎样', '研习', '纯数学', '或', '统计学', '本科', '与', '基础', '研究', '课程', '参考书目', '数学', '文化', '主要', '面向', '大学生', '大学老师', '和', '研究生', '以及', '中学老师', '和', '学生', '数学', '学习', '资源', '互联网', '上', '数学', '学习', '资源', '和', '教学', '视频', '英汉', '对照', '数学', '用语', '英汉', '对照', '数学', '用语'])
    
    ```

  - 转为简体后地分词和没有转换成简体地分词效果差好多！！！！不知道hanlp 或者是
  
- 加 停用词

  - ==读取停用词文本txt文件，需要用notepad++打开txt文件将其转码为utf-8==

  - ```
    (0, ['欧几里得', '西元前', '世纪', '古希腊', '数学家', '几何', '父', '此画', '拉斐尔', '作品', '雅典', '学院', '数学', '利用', '符号语言', '研究', '数量', '结构', '变化', '空间', '概念', '一门', '学科', '某种', '角度看', '形式', '科学', '一种', '数学', '透过', '抽象化', '逻辑推理', '计数', '计算', '数学家', '拓展', '概念', '数学', '基本概念', '完善', '早', '古埃及', '古希腊', '严谨', '数学', '发展', '持续', '小幅', '进展', '世纪', '文艺复兴', '时期', '致使', '数学', '加速', '发本科', '基础', '研究', '课程', '参考书目', '数学', '文化', '面向', '大学生', '大学老师', '研究生', '中学老师', '学生', '数学', '学习', '资源', '互联网', '数学', '学习', '资源', '教学', '视频', '英汉', '对照', '数学', '用语', '英汉', '对照', '数学', '用语'])
    
    ```

  - 

#### 本地bebug

- 问题： The "freeze_support()" line can be omitted if the program is not going to be frozen to produce an executable.
  - 解决方案： 把代码改在  if main 下面 具体 [参考](<https://blog.csdn.net/xiemanR/article/details/71700531>)
- 问题：wing ide 中文乱码
  - 在editor 中邮件选中properties 修改endoing utf-8

==待解决debug==

- 174行
- gensim官方文档查看

#### 程序复杂度预控

- 工具
- time.time() 记录
- enumerate 会不会增加时间用量

### 新的 python module

#### tqdm

- 问题

  - ```
      0%|          | 0/10 [00:00<?, ?it/s]
    100%|██████████| 10/10 [00:00<00:00, 10543.75it/s]
    # 为什么会有第一行 0%到的出现
    ```



### 代码更改

-  ```python
  doc_decoder = {i: doc_id for i, (doc_id, doc) in enumerate(encoded_docs)}    # 由于我没有删除任何文本 所以我觉得这个毫无意义
  ```

- 

### 新的功能实现（自己的）

#### 删除英文

- 使用正则，使得只保留中文信息，因为这里我通过采样发现文本中基本只有英文和中文没有其他的内容

- 因此只用正则寻找正则英文再取反

- ```python
   if re.compile(u'[\u4e00-\u9fa5]+').search(item) or \
                          re.compile("[\"”“，？?\,\.。,0-9]+").search(item):
                      new_line.append(item)
  # 修改
   if re.compile('[\W]+').search(item)    寻找非单词字符
  ```

- ````python
  # 这是我地方法
  new_text = [x for x in seg_list if re.compile('[^a-zA-Z]+').search(x) and x != ' ']
  # 这是gensim实验中wiki词向量训练地参考方法
  new_text = [x for x in seg_list if  re.compile(u'[\u4e00-\u9fa5]+').search(x) or \
                          re.compile("[\"”“，？?\,\.。,0-9]+").search(x)] 
  # 我地是匹配除了空格和英文之外地内容
  ````

- 

#### 繁简转换

- 上次我使用地OpenCC 说实话 有点难受 

- 工具

  - hanziconv 

  - ```
    pip install hanziconv
    >>> from hanziconv import HanziConv
    >>> print(HanziConv.toSimplified('繁簡轉換器'))
    繁简转换器
    >>> print(HanziConv.toTraditional('繁简转换器'))
    繁簡轉換器
    >>> HanziConv.same('繁簡轉換器', '繁简转换器')
    True
    ```

  - 

- 转为简体后地分词和没有转换成简体地分词效果差好多！！！！不知道hanlp 或者是 stanford nlp 的效果是怎样的

#### 去除停用词

- 这里==为什么需要删除停用词==

- ```
  
  ```

- ==分词工具可以加载停用词词典==

  - 这里貌似8行

- 这里我使用的是百度的停用词表 只启用了中文的部分，因为英文的部分都被我删了

#### 分词工具多线程并行处理



#### python 并行处理



#### python 对超大文件的读取访问

- 这里  wiki.get_texts(): 的函数 就是使用了 yield 的方法

#### Counter

- [参考](<http://www.pythoner.com/205.html>)

### 环境

- 使用 conda install -c conda-forge gensim 安装gensim 

### ==新 get==

- 既然gensim 给了如何处理wiki预料的xml文件的方法 那我直接看包是怎么写的不就可以知道如何对xml文件处理了
- wikipedia Extractor 好像也可以 都可以试一下

## intuition

- 当前是人工智能课程的结课报告

- 使用基于lda2vec的pytorch实现和原作者进行功能的复现

- 当前准备使用前期在gensim训练中文wiki语料的word2vec来进行训练

  - ==教训==
    - 因：觉得可能会堆积在github占容量 因此删了 是否可以 存储在cloud 上 镜像的 存储disk

- 目录在 /home/jupyter

  





## LDA

- 做中文LDA 需要删除停用词吗
  - [参考](<https://www.cnblogs.com/chenbjin/p/5638904.html>)





## 中文文本

- 应该有python的繁简转化

## GOOGLE CLOUD

### 笔记本实例

- 常常遇到的问题

  - [No module named google_compute_engine](https://stackoverflow.com/questions/38783140/importerror-no-module-named-google-compute-engine)

    - ```
          sudo rm -f /etc/boto.cfg
      ```

### opencc

'/home/g812126839qq/OpenCC/build/rel'



### 环境

- 只能使用Anaconda？ 不知道是为什么 看后面是否能够调整

### 问题

- 如何对云环境程序断点调试



## LDA2VEC

- 代码分析
  - 英文也是token之后变成了['  xxx  ' , '  xxx ' ]





## PPT

- 概述
  - 表征学习在自然语言处理的方向的工作
  - 语义表示
    - 文档级别的语义表示
      - 我们知道主题模型产生的主题分布可看做文档的语义表示，该表示能够用于文档分类、聚类、内容丰富度分析、CTR预估等多种任务。基于主题模型的文档特征表示可以分为两类，如图1所示：一类是经过主题模型降维，得到文档在主题上的多项分布，LDA、SentenceLDA等模型支持这一类的文档特征表示；另一类是联合使用主题向量和文档主题分布，生成的文档向量表示，TWE等融合了词向量的主题模型可以支持这一类的文档特征表示。
      - dense 和sparse的优缺点
        - 最经典方式的对比 Ida 和word2vec
          - 简要介绍一下word2vec的训练方法
            - 要介绍的新的方法的训练方法主要基于这个
          - 在语义表示上的级别体现
        - 深度学习和最传统的统计学习方法的比较
      - 作为表征学习的方式，他们在工程上，==传统的特征工程所选取的特征，因加入较多的先验知识，专家知识，可解释性较强，或者说例如今天要讲的主题模型中的LDA，因其学习到的特征具有较为稀疏的数据表示，维度不会很高，因此更容易让人能够去判断，而深度学习的方法做特征工程最大的好处就是能够挖掘出更多不为人所知的知识特征，在具体的任务中能够得到更好的效果，但是其可解释性较差，使得模型似乎千里之外，盲人摸象，==
- ==突出重点 more intereterable model for humans and not for machine==
- word2vec 可以直接用于计算例如词语级别的语义相似度，更加细粒度的任务应用，但是没有能够更加细粒度地为人所知
- ==语言模型==

- 工程上的事情不是静态的不是一成不变的，但是所训练的模型不可能实时更新，

  - ==[参考作者最后的post should I use lda2vec]== 例如你在做推荐系统 例如你在做舆情监督，不是一成不变的，与EMLMO的不同，对于刻画用户画像有较好的帮助（==结合语义匹配==）

    - > when:
      >
      > But if you want to rework your own topic models that, say, jointly correlate an article’s topics with votes or predict topics over users then you might be interested in [lda2vec](https://github.com/cemoody/lda2vec).
      >
      > why:
      >
      > Deep learning approaches have spectacular performance on supervised tasks, but their data products are usually not designed with humans in mind. I think that makes it difficult to understand your system, to move science forward, and to communicate your results. What lda2vec demonstrates is that you can at least try to build models with interpretable results very simply – building a sparse mixture isn’t very much work in today’s frameworks. **Build models for humans!**

  - ==过拟合 加上了regularizer==

- embedding 能够实现更加细粒度的语义关系    

- LDA产生的主题往往被高频词占据，这种现象导致低频词在实际应用中的作用非常有限 ，LDA2vec 依然有这个==问题== 

  - > Topical Word Embedding (TWE) 利用LDA训练获得的主题为词向量的训练提供补充信息，进而得到词和主题的向量表示。有鉴于向量表示可以较好地建模低频词的语义信息，通过利用词和主题的向量表示，我们可以更好地捕捉每个主题下的低频词的语义信息，提升下游应用的效果。

- 短文本和短文本的比配需要更加细粒度的语义关系表示，因此使用embedding的语义表示方式更加可行
- 而短文本和长文本的语义匹配中，lda2vec可以是一种较好的选择方式==？？？？？== 用户画像的雕刻可能更好一点，对推荐系统是一种好的选择
- 传统的主题模型不能够捕捉到例如当前深度学习的特征表示方式在单词语义相关性上的表现





## 经验

- 分词 并行处理 python的multipleprocess



## post 总结

- 由于我们现在做的是表征学习，它往往是其他任务的先行，因此模型会根据具体的任务而调整