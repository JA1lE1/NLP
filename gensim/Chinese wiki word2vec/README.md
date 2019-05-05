# README

这是我在做[python_full_stack_developer 的fork内容](<https://github.com/jasonhavenD/DJH-NLPIE>) 时遇到的gensim 词向量预训练模型的需求



### wget下载到Drive的指定的目录  

```
!wget -P content/gdrive/My Drive/Python_Full_Stack/gensim  https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
```





### 新的fork

- [github 新 word2vec](<https://github.com/dingdayu/word2vec>)
  - 正在训练
- [参考2](<https://github.com/datadevsh/wiki-gensim-word2vector>)
  - 貌似我可以直接拿来用

- 它的coding 思路和在flask开发的思路一致写config的class类，但是在path的地方出了问题

  - ==处理方法==

  - ```python
        wiki = WikiCorpus(os.path.join(Config().data_path, Config().zhwiki_bz2).replace('\\', '/'), lemmatize=False, dictionary={})
    ```

  - 

### 云环境

- 我使用Goole cloud（下载速度贼jb快!）
  - ==它的image我还是不太会用==

- 我使用了两个instance去跑测试对比效果
- gensim不支持GPU因此用8核的跑吧 ，新开一个
  - 另外:[google GPU说明文档](<https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=zh-cn>)
  - 以后可能有用！



### python 虚拟环境（==等待还是离开==）

- 在flask的地方，我觉得在每个工程上添加venv的习惯是真滴棒，因此我决定以后都会这样做一下
  - gensim
  - jieba

#### 等待

- 等待总是漫长的，但是确实可以发现Google 天下无敌!



#### 出现错误

- 貌似是因为下载的问题 我在执行01py文件的时候出现的错误
  - Compressed file ended before the end-of-stream marker was reached



### gensim模块的学习

- 引入
  - gensim的训练的==多线程==是如何实现的

- [Apache 组织的中文tutorial](<https://github.com/apachecn/gensim-doc-zh/tree/master/blog/tutorial>)

#### 疑难

```python
from collections import defaultdict
frequency = defaultdict(int)


```



### python 疑难

```
import logging     ## 引入日志配置？？
```





### github

- ==gitignore==



### OpenCC

- 某大牛很小的时候开发的中文繁简体转换工具

#### 使用OpenCC将繁体字转换为简体字

```linux
$ cd /data/zhwiki/
$ opencc -i zhwiki_raw.txt -o zhwiki_t2s.txt -c t2s.json
```

##### 安装

```linux
sudo apt-get install opencc
```

#### 官方

- [github](https://github.com/BYVoid/OpenCC#installation-安裝)

- debian 系统下的doc

  - ```
    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA256
    
    Format: 3.0 (quilt)
    Source: opencc
    Binary: opencc, libopencc2, libopencc-dev, libopencc2-data
    Architecture: any all
    Version: 1.0.4-5
    Maintainer: IME Packaging Team <pkg-ime-devel@lists.alioth.debian.org>
    Uploaders: LI Daobing <lidaobing@debian.org>, Asias He <asias@debian.org>, YunQiang Su <wzssyqa@gmail.com>, Osamu Aoki <osamu@debian.org>, Aron Xu <aron@debian.org>
    Homepage: https://github.com/BYVoid/OpenCC
    Standards-Version: 3.9.8
    Vcs-Browser: https://anonscm.debian.org/gitweb/?p=pkg-ime/opencc.git
    Vcs-Git: git://anonscm.debian.org/pkg-ime/opencc.git
    Build-Depends: cmake, darts, debhelper (>= 9), doxygen, libjs-jquery, libtclap-dev, python, rapidjson-dev
    Package-List:
     libopencc-dev deb libdevel optional arch=any
     libopencc2 deb libs optional arch=any
     libopencc2-data deb libs optional arch=all
     opencc deb utils optional arch=any
    Checksums-Sha1:
     af97a84d8bf1b0f955d146aef55fbbbaf1eaf6b1 1597309 opencc_1.0.4.orig.tar.gz
     e00623580ad085d5bccba53654ccba458822834a 5900 opencc_1.0.4-5.debian.tar.xz
    Checksums-Sha256:
     0553b7461ebd379d118d45d7f40f8a6e272750115bdbc49267595a05ee3481ac 1597309 opencc_1.0.4.orig.tar.gz
     ab9b5f468003acd646fca377b3124d7188273f58864428a12869f81cc74ac372 5900 opencc_1.0.4-5.debian.tar.xz
    Files:
     673e00170bacc7a2f92ab327a7a2549b 1597309 opencc_1.0.4.orig.tar.gz
     fbe1204883f7cbb50b9413b3f76cea3e 5900 opencc_1.0.4-5.debian.tar.xz
    
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1
    
    iQEcBAEBCAAGBQJYgbnZAAoJEPbsVcVkKA0esb4H+wcjVXEU8T0k3nbnRk9GsCCT
    GfIG2zMTPnqXGukf9Dl8onUDknBNbWvTWT3HExmfQDMOyzOLjmuSyhg3QfoTW52x
    shqzsTX/Tzj5MGb32nPX2pGGp847zO2kH3SxsjEkgY+wwNAXNNmk1c7ab7FV/1AO
    QZgoxHhB7QigrOiBLJDiYA0G3LwTi5V08dWW5+JSbZQTObQrW5zpBBGrLYokLTkz
    5GeeWjseHCwROohCoA8TBi3bRTC85ZUxgwscU/UdCqlWX+bEUJHHSslsDl55GmuM
    jO9qxeh5ZWMZV4vwhr/eCuau+ebokZY8IMlNArzKI7AEB7kaaTTthugEPPjw/WE=
    =Gre+
    -----END PGP SIGNATURE-----
    ```

    - ==这里注意到 Build-Depends: cmake, darts, debhelper (>= 9), doxygen, libjs-jquery, libtclap-dev, python,==

#### 卸载

- 

#### 解决方法

- [参考链接](<https://my.oschina.net/dingdayu/blog/1524340>)
- 其实没有解决一些问题 （segment fault）我直接把原来云删了 再建一个 确认opencc没有问题再进一步动作，感觉才40分钟就到了python 02的步骤，好了谷歌牛逼





### 离线训练的方法（断开ssh）

- [参考](<https://zhuanlan.zhihu.com/p/31457591>)
- ==screen的使用==
- -r
- ctrl + a + D

###  意外的收获

##### ==抽取正文文本==

- 使用 [Wikipedia Extractor](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor) 抽取正文文本
- Gensim里自带了提取wiki内容