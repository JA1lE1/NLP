# README

## 最新内容（每次更新删除上一版的最新）

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