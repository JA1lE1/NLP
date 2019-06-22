# README



## Intuition

- 洪老师汇报的时候，提到上次学习的lda2vec的事情，和新闻挖掘开发平台的事情。那老师希望有开发实际的展示在群贤平台上
- 洪老师提供了开发人员和产品经理的交流机会可以借此彻底完成上次未完成的lda2vec的任务





## 思路

- 先行解决上次训练结果的处理在pyLDAvis上的使用，仔细理解并解决相应的使用(与开发人员进行交流，这个**花费长时间**)
- 前端展示的需求与设计（与产品经理，这个这两天可以基于当前的理解，先行完成一个粗糙地版本）
- 使用lda2vec的pytorch 版的20news的实验(做起来不麻烦，而且我貌似已经有昨晚了的保存)结合新的fork的pyLDAvis的可视化方法先行尝试





## pyLDAvis

- 又到了这个收悉的版块
- 方法
  - lda2vec的原作者的方法查看
  - pyLDAvis的demo查看

### 官方Notebook Demo

- [地址](<https://nbviewer.jupyter.org/github/bmabey/pyLDAvis/blob/master/notebooks/pyLDAvis_overview.ipynb>)

#### BYOM

> ## BYOM - Bring your own model
>
> `pyLDAvis` is agnostic to how your model was trained. To visualize it you need to provide the **topic-term distributions**, **document-topic distributions**, and basic information about the corpus which the model was trained on. The main function is the [`prepare`](https://pyldavis.readthedocs.org/en/latest/modules/API.html#pyLDAvis.prepare) function that will transform your data into the format needed for the visualization.
>
> Below we load a model trained in R and then visualize it. The model was trained on a corpus of 2000 movie reviews parsed by [Pang and Lee (ACL, 2004)](http://www.cs.cornell.edu/people/pabo/movie-review-data/), originally gathered from the IMDB archive of the rec.arts.movies.reviews newsgroup.

- 这里关键是需要提供**主题词分布**情况，还有**文档-话题分布**





### LDA2VEC 的20news的demo

- [地址](<https://nbviewer.jupyter.org/github/cemoody/lda2vec/blob/master/examples/twenty_newsgroups/lda2vec/lda2vec.ipynb>)

#### Reading in the saved model topics

- > `topics.pyldavis.npz` will be created that contains the **topic-to-word probabilities and frequencies**

- [模型存储的代码地址](<https://github.com/cemoody/lda2vec/blob/master/examples/twenty_newsgroups/lda2vec/lda2vec_run.py>)

- ```python
     # 在20news下的lda2vec下的lda2vec_run.py
      data = prepare_topics(cuda.to_cpu(model.mixture.weights.W.data).copy(),
                            cuda.to_cpu(model.mixture.factors.W.data).copy(),
                            cuda.to_cpu(model.sampler.W.data).copy(),
                            words)
      data['doc_lengths'] = doc_lengths
      data['term_frequency'] = term_frequency
      np.savez('topics.pyldavis', **data)
      
      ## 对比pyLDAvis 官方的dict
      data = {'topic_term_dists': data_input['phi'], 
              'doc_topic_dists': data_input['theta'],
              'doc_lengths': data_input['doc.length'],
              'vocab': data_input['vocab'],
              'term_frequency': data_input['term.frequency']}
      ## 关键是找prepare_topics的source ，但是好像找不到
      ### 解决防范
      ####  新的fork https://github.com/whcjimmy/lda2vec 这个修改了20news的方法，希望可以参考一下
     ```
```
  
- [新的fork](https://github.com/whcjimmy/lda2vec)

  - preprare的source--  [lda2vec](https://github.com/whcjimmy/lda2vec)/[lda2vec](https://github.com/whcjimmy/lda2vec/tree/master/lda2vec)/**topics.py**
- 已经fork到本地了

#### 20news 下

- lda2vec_run 
  - 重要的变量--**data** 
  - prepare_topics 其函数在lda2vec 下的topics.py
    - 原作者使用的方法训练的模型的weight的权重网络？ == document-topic?
    - factors == topic2vec
    - 还有网络中的word2vec
  - 也就是要找到原网络中的三个网络权重？分别是document-to-topic  weights topic2vec word2vec





## 网络结构学习

- 原作者的lda2vec的网络

  - 在utils 中 的training的params 有三个？？ 如何去理解 ？

  - ```python
    params = [
            {'params': [model.topics.topic_vectors],
             'lr': topics_lr, 'weight_decay': topics_weight_decay},
            {'params': [model.doc_weights.weight],
             'lr': doc_weights_lr},
            {'params': [model.neg.embedding.weight],
             'lr': word_vecs_lr}
        ]
    #不同的网络 不同的学习率 和权重衰减
```

  - 

- lda2vec-pytorch版

- lda2vec-tf版





## prepare_topics





## 待做

- 找一下最新的做的实验的120epoch的结果

- 新的20news_explore 找到

  - ```python
    data['doc_lengths'] = doc_lengths
    data['term_frequency'] = term_frequency
    # 就是每篇文章的长度
    # 至于词频应该在counts那个地方就有保存成np的格式就可以
    ```

- ==完成中南的xml数据的处理，并完成对应的实验==

- ==实验主文件夹在群贤平台 查看各个文件好了==

### 老师要求

- 项目设计书
- ==找老师借一下大牛写的项目设计书==



### 存在的问题

- 是否使用==预训练的word2vec==会好一些，查看==原作者==的方法(ta貌似是导入google的预训练的数据)，我可以网上找，也可以使用我自己训练的
- 文本存在的时间信息如何取舍，需要考虑一下
- 文本似乎过短的在lda2vec-pytorch版本是无法训练，现在问题来了，如何解决这个问题
- 如何加载预训练的word2vec
- ==这也是对加载模型如何适应自身模型的一个很重要的实践==
  - 可以使用预训练的，都是gensim训练有神马不行的，把格式进行调整就可以达到了
  - 就是讲最后的结果存储成已有的字典模型
  - ==这个不是优化的过程如果我要使用短文本==
  - ==这个算是优化的过程，如果我使用长文本==
  - ==plan==
    - 先使用长文本，也就是先删掉Nan值，并且还是使用原先有的东西:heavy_check_mark:
    
    - 记录这个事情，再产品**正式开发阶段**进行先关的实验，当前是**模型测试实验**
    
      - [ ] 实验数据有问题，需要重新爬取
    
      - [ ] 模型的词向量使用预加载词向量，具体参看原作者的Hacker_news的使用
    
      



### 爬虫

- selenium 的使用 即用法



## HAcker_news

### lda2vec.ipynb

- story_topics

  - ```python
    story_topics = pd.DataFrame(dict(story_id_codes=np.arange(dat['doc_topic_dists'].shape[0])))
    #也就是这个dists 是以story_id来排序的？代表总的语料数目？
    story_topics[labels[idx]] = dat['doc_topic_dists'][:, idx]
    ```



### 大体思想

- 应该是将原始语料进行lda2vec的实验(语料处理方法还不得而知)
- 训练后的模型的doc_topic_dists应该是以文本id排序（这里需要注意原数据的处理方式）
- 然后将原始文本经过一定的处理，原始文本带有时间信息，lda是sparse的，当文本带有某个主题，记录其个数再除以总的文本个数就是当前文本的topic_占比，而文本本身包含有时间信息，这样处理后再groupby（time）就能够以时间序列的信息进行可视化的展示。



### model

- 好像就多了对author的训练（待验证）





## 爬虫部分

- 方式在子目录web-extract的部分

  - 应该是参考

  - > Python+selenium+chrome的web自动化

- 知识弥补
  
  - ==线程与进程的区别==

### Multiprocessing 总结

- [莫凡python](<https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/7-lock/>)
  - 粗略总结





#### 原作者的问题

- 中南fork作者的爬取的数据是有问题的
  - eg 经济类新闻突然出现例如有关吴亦凡的娱乐新闻信息
- ==解决方案==
  - 独立地（仿照例如北理工的）进行爬取在Mysql下，并生成类似XML或者json
    - 还可以进行数据的转移
    - 从获取数据的角度讲，甚至是否可以直接使用newpaper3k去完成任务  
    - 应该是可以的，后期可以再装修，结合线程和进程去解决这些问题
  - 如何将爬取的资料写成xml或者是json更方便地可以进行数据的处理呢？

### 当前的问题

- 如何获取基于时间序列分文本数据

  - [爬取过去某个时间段的新闻](<https://github.com/Heaven-zhw/SinaOldNews>)

  - 研究原作者对于时间戳和爬取参数的设置

  - > url = <http://search.sina.com.cn/?c=news&q=%D3%A2%B9%FA%CD%D1%C5%B7&range=all&time=custom&stime=2016-10-13&etime=2016-12-10&num=20&page=3>

  - ```python
    url = 'http://search.sina.com.cn/?c=news&q=%D3%A2%B9%FA%CD%D1%C5%B7&range=all&time=custom&stime=' + str(a) + '&etime=' + str(b) + '&num=20&page=' + str(m)
    
    # 这里a 代表的是时间戳(年-月-日) b和 a一致的格式 （eg. 2016-10-13:2016-12-10） m代表的是页数
    ```

  - 以上可以作为爬取的主要依据，具体可以模仿中南工程 再进行装饰

  - 

### 解决方法

- 一步一步蚕食，不需要太过于紧张
- 先行具体执行所需的步骤，然后再来看代码，甚至也不一定要每一步都很细，需要才了解好了，毕竟要对最后结果有所作用再去做。
- ==自己模仿着着数据需求自己爬 使用mongodb 转成json的格式==



### python module

- pymysql
- fake_useragent
- ==selenium==

### 当前进度

- 依据作者在sql.txt留下的执行方案
  - [参考链接](<https://blog.csdn.net/qq_38779421/article/details/78347185>)
  - 完成自动化测试
  - ==已经完成第二步骤-selenum的安装==
- 下一步执行pymysql 链接程序



### 数据库

- 这里全部使用docker的方式进行一遍

#### Mysql

- 应该是版本的问题 现在的配置文件是 /etc/mysql/my.conf

  - ```
    # 对应的加载文件夹
    !includedir /etc/mysql/conf.d/
    !includedir /etc/mysql/mariadb.conf.d
    ```

  - 具体的配置文件在  /etc/mysql/mariadb.conf.d# vim 50-server.cnf

  - ```
    #
    # * Basic Settings
    #
    user            = mysql
    pid-file        = /var/run/mysqld/mysqld.pid
    socket          = /var/run/mysqld/mysqld.sock
    port            = 3306
    basedir         = /usr
    datadir         = /var/lib/mysql
    tmpdir          = /tmp
    lc-messages-dir = /usr/share/mysql
    skip-external-locking
    # Instead of skip-networking the default is now to listen only on
    # localhost which is more compatible and is not less secure.
    bind-address            = 127.0.0.1
    #
    # * Fine Tuning 
    #        
    key_buffer_size         = 16M
    max_allowed_packet      = 16M
    thread_stack            = 192K
    thread_cache_size       = 8
    # This replaces the startup script and checks MyISAM tables if needed
    # the first time they are touched
    myisam_recover_options  = BACKUP
    #max_connections        = 100
    #table_cache            = 64
    #thread_concurrency     = 10 
        
    #   
    # * Query Cache Configuration
    #   
    query_cache_limit       = 1M
    query_cache_size        = 16M
    ```



##### 待做

- 在服务器上 授予mysql 下的新用户的 某个数据库的权限 方便其在pymysql下使用
- 不知道怎么回事 我在pymysql 下一直不能使用root命令
- 参考
  - [youtube-python-mysql-hello-world](<https://www.youtube.com/watch?v=nEJFpuTrC9s&t=199s>)
  - [csdn](<https://blog.csdn.net/shouwangcc/article/details/47758901>)
  - [用户授权](<https://www.cnblogs.com/chanshuyi/p/mysql_user_mng.html>)

##### 当前创立的数据库

```
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| pythonDB           |
+--------------------+
2 rows in set (0.00 sec)

MariaDB [(none)]>
```



#### GreenPlum

- [参考链接](<https://blog.csdn.net/qq547276542/article/details/79058299>)
  - 暂停施工



#### MongoDB

- python +

- **docker** 方式 去 使用 Docker

  - > 1.官方的命令 docker pull mongo
    >
    > 2.docker images 查看当前系统的所用docker images
    >
    > 3.docker run -d -p 27017:27017 -v mongo_configdb:/data/configdb -v mongo_db:/data/db --name mongo docker.io/mongo
    >
    > ​	3.1==这句话的意思==
    >
    > ​			3.1.1

  - 4.0.4

  - docker

    - ==[主要参考链接](<https://www.youtube.com/watch?v=D5Q5WhGT0w8>)==

    - 对应的笔记

      - > 1.d0cker pull mongo
        >
        > 2.docker pull mongo:4.04 (最新版的往往有一堆bug）
        >
        > 3.docker images （查看当前docker  images 列表）
        >
        > 4.docker run --name mongodb（deploy image）(running 不是在backgroud  不是在 detach mode)
        >
        > 5.docker run -d -p 27017-27019:27017-17019 --name mongodb mongo：4.0.4 
        >
        > 6.docker ps -a （查看当前运行的 docker container？）
        >
        > 7.docker stop mongodb      
        >
        > 8.docker rm mongodb
        >
        > 9.docker exec -it mongodb bash (相当于进入container？)
        >
        > 10.mongo（进入shell client）
        >
        > 11.use thepolyglotdeveloper（直接是创建数据库）
        >
        > 12.db.people.save({firstname:"NICK"， lastname："Raboy"})
        >
        > 13.db.people.save({firstname:"Maria", lastname:"Raboy"})
        >
        > 14.db.people.find({})
        >
        > 15.db.people.find({firstname:"Maria"})
        >
        > 16.exit
        >
        > 17.still run in detach mode
        >
        > 18.docker stop mongodb
        >
        > 19.docker rm mongodb

      - >1.show dbs
        >
        >2.use python
        >
        >3.db
        >
        >4.db.news.insert({title:"hello-world",content:"today is not so good!"})
        >
        >5.db.news.find({})
        >
        >6.db.news.find().pretty()      # 相当于对jsonpretty

- python-mongo

  - python3 -m install pymongo

  - ```
    Python 3.7.3 (default, Mar 27 2019, 22:11:17)
    [GCC 7.3.0] :: Anaconda, Inc. on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pymongo
    >>> clinet = pymongo.MongoClient(host='localhost', port=27017)
    >>> db = client.python
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'client' is not defined
    >>> db = clinet.python
    >>> collection = db.news
    >>> result = collection.find()
    >>> print(result)
    <pymongo.cursor.Cursor object at 0x7f39fe276278>
    >>> result = collection.find_one({'title':'hello-world'})
    >>> print(result)
    {'_id': ObjectId('5d0a2c2658c5023a08fe2ec9'), 'title': 'hello-world', 'content': 'today is not so good!'}
    ```

  - [参考链接](<https://juejin.im/post/5addbd0e518825671f2f62ee>)

## 解决方案

- 貌似上次做的实验结果model 找不到了 不过问题不大

  - 直接去做中南实验的复现

- 就是把lda2vec-pytorch版的在pyLDAvis使用一下看能不能使用

- 执行一下群贤平台中新fork的topics和lda2vec_run的prepare-topics 结合

  pytorch版的[explore_trained_model](<https://github.com/TropComplique/lda2vec-pytorch/blob/master/20newsgroups/explore_trained_model.ipynb>)

- ==查看中南的xml是时间序列的数据？待研究==

- 如何处理XML文件的数据处理？

### 方法论

- 应该是主要大概的做一个很粗的流水线
- 因此先行完成还没有进行过的主题分布pyLDAvis的部分和主题演化的可视化展示
  - 注意，这里需要注意的是数据至少不多，效果不在意
  - 参考Hacker news的主题演化在最新的fork下（已经fork到github的lda2vec）
- 三个数据预处理的对比 原作者的两个 + pytorch版的一个







## 当前进度

- 完成了pytorch版的模型结果展示向原作者版本的结果展示的pyLDA可视化的进程
  - 可能是因为sklearn---20news的语料库有修改当前测试的时候多删了两篇导致最后的结果与以前的训练结果不匹配，不过这影响不大。

### 当前需要做的事情

- 新建数据库，赋予权力，修改代码，跑一个实验试一下数据是否可用
- 数据有后先行测试一份小数据的主题演化，主题演化，实现之后（基本就算完成了）
  - 看能否在原作者的hacknews找到主题演化的曙光
- 实现数据的拓展，增加不同领域的文本的爬取
- 前端的设计实现
- 项目说明书的撰写，WIki的撰写
- （修改使用GP 的Gtext 来使用）
- 与群贤平台的项目进行兼容
- ==以快为主，后期再进行装修==



### 6.21

- 进行Hacker news的复现的实验的时候在tokenize的点遇到了问题打开jupyterlab可看到
- 研究一下作者的tokenize的思路，修改一下代码，看能不能运行，不行的话，另行它法
  - 不一定要莽到底
- Hacker_news
  - 运行的三个步骤
    - 1.preprocess
      - 



## 主题演化的学习

- 中南的主题表示学习的展示平台

  - ==新闻滑动平均百分比== 是神马意思？

    - > 对中美贸易战每篇新闻进行主题划分，绘制给定主题下新闻滑动平均百分比随时间演化图
      >
      > 这句话是神马意思呢？

  - 这个应该是每个预定的新闻类型下（数据的前期分类甚至可以使用GBM+LDA的方式）下各个主题的百分比随时间的演化图(这里使用的应该是滑动平均模型)。（注意这个主题百分比加起来不一定等于100 应该是取top-k的主题）

  - 这里关键就是如何获取这个随时间演化的**百分比数据**

  - 



## 内容概述

- 主要的基础测试(20news)在lda2vec-pytorch中，中文的文本后期处理在上次的explore_chinese_lda2vec中有具体的测试。
- 当前是xml格式的文件处理，应该是对粗爬虫的数据处理，在news-comment-spider中







## 参考内容

- [lda2vec作者的post](<https://multithreaded.stitchfix.com/blog/2016/05/27/lda2vec/#topic=38&lambda=1&term=>)



