# README



### intuition

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

#### google cloud 的 XSHELL 使用方法

- intuition
  - vim无法鼠标抓取

- [参考](<https://blog.csdn.net/datadev_sh/article/details/79593360>)

  - 这里我直接使用了它的root方式登录法

  - ```
    vi /etc/ssh/sshd_config
    
    # Authentication:
    PermitRootLogin yes //默认为no，需要开启root用户访问改为yes
    
    # Change to no to disable tunnelled clear text passwords
    PasswordAuthentication yes //默认为no，改为yes开启密码登陆
    
    passwd root
    
    /etc/init.d/ssh restart
    --------------------- 
    作者：datadev_sh 
    来源：CSDN 
    原文：https://blog.csdn.net/datadev_sh/article/details/79593360 
    版权声明：本文为博主原创文章，转载请附上博文链接！
    ```

  - root的法方便，但是很有风险，==找时间使用第二种方法==

  - ==注意登录的用户是root==

- ==vim中的内容无法使用鼠标选取(云端复制到当前环境)==

  - [参考](<https://blog.csdn.net/sbqakqux/article/details/38085603>)

    - 推荐使用方法1 

    - ```
      vim 下  :set mouse -=a
      ```

### 记录事件

- 貌似谷歌云关掉以后重新登后的外网ip地址是不对外开放的。只有通过gcp之间的ssh方式才能够登录，登录后外网ip就自动开放了
- ==yum的安装==
  - 直接apt-get install yum 最方便

### python 虚拟环境（==待==）

- 在flask的地方，我觉得在每个工程上添加venv的习惯是真滴棒，因此我决定以后都会这样做一下
  - gensim
  - jieba

#### 等待

- 等待总是漫长的，但是确实可以发现Google 天下无敌!



#### 出现错误

- 貌似是因为下载的问题 我在执行01py文件的时候出现的错误
  - Compressed file ended before the end-of-stream marker was reached
  - 解决方式：
    - 删了重新下载



### gensim模块的学习(==待==)

- 引入
  - gensim的训练的==多线程==是如何实现的
  - 训练函数的参数貌似有work参数，添加python-module-multiprocessing？
  
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

- multiprocessing
  - ==引入下一步大规模并行爬取？==



### github

- ==gitignore==

- 新的环境下的git使用配置

  - 见本地或者远端的个人每人笔记 github小结
  - 主要是 现在本地使用ssh-keygen -t rsa -C "812126839@qq.com"，然后就是复制生成的文件中的内容到github上的ssh秘钥粘贴一下(setting中)，然后就算是配置好了，注意下vim 使用 :set mouse-=a 才能使用鼠标法复制粘贴的习惯

- ==传输大文件==

- ```
  # 1、安装git-lfs
  brew install git-lfs   # 换成apt-get install 
  
  # 2、没有特别说明的情况下，LFS 不会处理大文件问题，因此，我们必须明确告诉 LFS 该处理哪些文件。将 FrameworkFold/XXXFramework/xxx的文件设置成大文件标示。
  git lfs track "FrameworkFold/XXXFramework/xxx"
  
  # 3、常规的push操作（忽略一下具体，按照自己）
  git add .
  git commit -m "add large file"
  git push
  --------------------- 
  作者：兵临城下也 
  来源：CSDN 
  原文：https://blog.csdn.net/u012390519/article/details/79441706 
  版权声明：本文为博主原创文章，转载请附上博文链接！
  ```

  - ==intuition==
  - 从云环境下载文件实在是太慢了，我发现谷歌和github之间传输很快，因此选用了谷歌云传github然后在本地git下github的内容



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
- 具体方案应该是在新的云环境下先试一下上述的参考方法git，然后安装相关的包再cmake cmake install，当然到目前为止，我不知道怎么卸载



### 疑问

- 如何解决程序跑完后检查其效果
- ==暂未解决==
  - 有个可行的方法是log的日志记录

### 离线训练的方法（断开ssh）

- [参考](<https://zhuanlan.zhihu.com/p/31457591>)
- ==screen的使用==
- -r
- ctrl + a + D
- 注意记录 python-log模块的用法



#### 程序跑完后的提醒

- 邮箱提醒
- 代码写log的习惯(机器写)



###  意外的收获

##### ==抽取正文文本==

- 使用 [Wikipedia Extractor](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor) 抽取正文文本
- Gensim里自带了提取wiki内容

#### 加密算法

- github-GPG 配置







### 程序设置提醒和logging

- ==邮箱提醒==

  - 邮箱:zlbnoj@163.com

  - 用的SMTP，密码是网吧hou+惯例

  - 参考

    - [sf-yagmail使用](<https://segmentfault.com/a/1190000014796660>)

      - 这个参考的贡献度在于
        - SMTP的密码登录不是通常的邮箱密码而是==授权码==

    - [yagmail使用详解](https://xin053.github.io/2016/12/17/yagmail邮件发送库使用详解/)

      - yagmial使用前可以设置==keyring==（密码预设值？） 避免在代码中暴露

        - ```
          # 使用前升级keyring
          pip install --upgrade setuptools
          ```

      - 这篇的端口号不要照着设置

        - [Hi, had the same issue
          change the port
          for example: port=465](<https://github.com/kootenpv/yagmail/issues/97>)

  - 注：由于要使用功能，因此绑定了手机号，需要后续的注意



### 待做

- venv的配置以及flask作者的想法



### further work

- 先掌握gensim的词向量的训练方法
  - 各种渠道，包括kaggle的 kernel
  - 当前的wiki中文百科其实不算是很好的语料库，而且我觉得一定要针对特定的领域问题或者任务去建立词向量才是有意义的否则效果很差，开放性任务和问题除外。
    - [有训练很多语料库的词向量](<https://www.jianshu.com/p/ae5b45e96dbf>)
- 大规模并行爬虫，spark及kerbuXXXX的部署(基于GCP),在github-中南的那个idea下进行
  - 完成相关论文的初始idea
- 非重点
  - git-淘沙
  - 

### 参考

- github
  - [基于 gensim 的 wiki 词向量](<https://github.com/dingdayu/word2vec>)
- 博文
  - [用word2vec分析中文维基语料库](<https://magicly.me/word2vec-first-try-md/>)
  - [我爱自然语言处理](http://www.52nlp.cn/中英文维基百科语料上的word2vec实验)
- 其他
  - python-logging的学习
    - [崔庆才](<https://cuiqingcai.com/6080.html>)