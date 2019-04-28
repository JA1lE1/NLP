# README

----

2019.4.28

------

## 代码分析

### python 文件

#### open 代开方式

```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明:
7
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式   "r"：读取，  “w”：写
buffering: 设置缓冲
encoding: 一般使用utf8   ## encoding = "utf-8"
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener:
```

#### 按行读取 fp.readlines()

```python
fileObject.readline(); 
参数
size -- 从文件中读取的字节数。
-----------------------------

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("runoob.txt", "rw+")
print "文件名为: ", fo.name

line = fo.readline()
print "读取第一行 %s" % (line)

line = fo.readline(5)
print "读取的字符串为: %s" % (line)

# 关闭文件
fo.close()
-----------------------------
文件名为:  runoob.txt
读取第一行 1:www.runoob.com
    
读取的字符串为: 2:www
```

#### 写入文件

- 只能是str不能是byte？

- 写入

  - **write()** 方法用于向文件中写入指定字符串。

    在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。

    如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错：TypeError: a bytes-like object is required, not 'str'。

  - ```
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-
    
    # 打开文件
    fo = open("test.txt", "w")
    print "文件名为: ", fo.name
    str = "菜鸟教程"
    fo.write( str )
    
    # 关闭文件
    fo.close()
    ```

  - 

### 正则表达式

#### python 字符串前加u,r,b的含义

> u/U:表示unicode字符串 
> 不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码。 
> 一般英文字符在使用各种编码下, 基本都可以正常解析, 所以一般不带u；但是中文, 必须表明所需编码, 否则一旦编码转换就会出现乱码。 
> 建议所有编码方式采用utf8
>
> r/R:非转义的原始字符串 
> 与普通字符相比，其他相对特殊的字符，其中可能包含转义字符，即那些，反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n”表示换行，”\t”表示Tab等。而如果是以r开头，那么说明后面的字符，都是普通的字符了，即如果是“\n”那么表示一个反斜杠字符，一个字母n，而不是表示换行了。 
> 以r开头的字符，常用于正则表达式，对应着re模块。
>
> b:bytes 
> python3.x里默认的str是(py2.x里的)unicode, bytes是(py2.x)的str, b”“前缀代表的就是bytes 
>
> python2.x里, b前缀没什么具体意义， 只是为了兼容python3.x的这种写法
>
> 作者：抖腿大刘 
> 来源：CSDN 
> 原文：https://blog.csdn.net/u010496169/article/details/70045895 
> 版权声明：本文为博主原创文章，转载请附上博文链接！

- ==regex1==包含中文可能就需要前面+u'XXXX'
  - ==regex1== 代表非汉字XXX期
  - 正则表达式[\u4e00-\u9fa5]表示匹配中文，则正则表达式 \[^\u4e00-\u9fa5]匹配非中文
- ==(?:...)== (.....)的不同分组版本，使用'|'或后接数量词，本代码是因为后接数量词=={1,5}期== 
  - 这个不分组，但是作为整体(分组表达式代表一个整体)，后可以接数量词。表达式中的|仅在该组中有效。
- 参考
  - [指南](<https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html>)

#### re.findall()

- ```python
  findall(pattern, string, flags``=``0``) 
  对 string 返回一个不重复的 pattern 的匹配列表， string 从左到右进行扫描，匹配按找到的顺序返回。如果样式里存在一到多个组，就返回一个组合列表；就是一个元组的列表（如果样式里有超过一个组合的话）。空匹配也会包含在结果里。
  ----------------------------------
  疑问：多个是返回元组的列表？
  ----------------------------------
  regular_v1 = re.findall(r"docs","https://docs.python.org/3/whatsnew/3.6.html")
  print (regular_v1)
  # ['docs']
  ```

#### re.sub()

```python
import re  
  
text = "JGood is a handsome boy, he is cool, clever, and so on..."  
print(re.sub(r'\s+', '-', text))
---------------------------------------------------------
#JGood-is-a-handsome-boy,-he-is-cool,-clever,-and-so-on...
```





### 整体思路

- 对一篇复杂的语料进行分词，有些词语难以分得准确，加入自己的词典，jieba直接通过jieba.load_userdict()
- 而hannlp在其对应的modeul下加入字典并修改对应的配置文件即可完成
- 而有些词语他们具有相同的规律但是原文本太过于粗糙，并没有形成很好的规格，所以需要进行正则匹配，自己写规则去分好词。
  - 对于

### 自己练习的思路

- 先不加字典，自己找语料库尽心分词
- 加字典分词
- 加正则匹配分词
- hannlp的分词联系



### 迭代器

- 对于Hanlp的分词 segment的结果是迭代器，但是需要对其每个元素使用toString方法再split()(注：其返回值是list)

### 生成器和迭代器

- ```
  # 判断迭代器
  from collections import Iterable
  isinstance(seg_out, Iterable)
  ```

- str.split()的返回值是list

- **xrange()** 函数用法与 [range](https://www.runoob.com/python/pytho-func-range.html) 完全相同，所不同的是生成的不是一个数组，而是一个生成器。

- 参考

  - [知乎](<https://www.zhihu.com/question/20829330>)
    - 生成器是python的一大特点，它对于大规模文本的处理尤为有效
  - [中文博文](<https://foofish.net/iterators-vs-generators.html>)

### Hanlp_tutorial_2

- [参考来源](<https://github.com/hankcs/pyhanlp/tree/master/tests/demos>)

```
    NLPTokenizer = JClass("com.hankcs.hanlp.tokenizer.NLPTokenizer")
    seg_out = NLPTokenizer.segment("我新造一个词叫幻想乡你能识别并正确标注词性吗？")
```

#### debug

```python
list_word= []
for i in seg_out:
    list_word.append(i.toString().split('/')[0])
--------------------------------------------------------
list_word
['我', '新', '造', '一个', '词', '叫', '幻想乡', '你', '能', '识别', '并', '正确', '标注', '词性', '吗', '？']

```

```python
# 在seg_out 下打断点
--------------------------------------------
gen_new= (seg.toString().split('/')[0] for seg in seg_out)  # seg 是jtype类型，使用其toString()方法，去掉'/' 生成list 再 取【0】 这里是否有好一点的办法，例如直接取字符串的某
print(" ".join(gen_new))
--------------------------------------------
#我 新 造 一个 词 叫 幻想乡 你 能 识别 并 正确 标注 词性 吗 ？
```

#### ==想法==

- ==这里是否可以使用字符串拼接，字符串剪裁等，没有build-in函数自己试着造一下？==

#### python split()

- Python **split()** 通过指定分隔符对字符串进行切片

- ```python
  str.split(str="", num=string.count(str)).
  ```

- 返回值是list



- 注释

  - NLPTokenizer.segment结果是可迭代对象

    - ```python
      from collections import Iterable
      isinstance(seg_out, Iterable)
      True
      ```

    - 分别是分词及词性标注，将每个元素i生成其str对应值，再用split的方法取每个listing的[0]值

    - 生成了list

### Tokenizer

```
 " ".join([word_pos_item.toString().split('/')[0] for word_pos_item in Tokenizer.segment(sentence)]   )
```

- 对于这段代码的理解
  - join()参数是生成器？
  - 参考
    - [知乎](<https://www.zhihu.com/question/20829330>)
      - 生成器是python的一大特点，它对于大规模文本的处理尤为有效
    - [中文博文](<https://foofish.net/iterators-vs-generators.html>)

#### str.join(iterable)

- Return a string which is the concatenation of the strings in *iterable*. A [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError) will be raised if there are any non-string values in *iterable*, including [`bytes`](https://docs.python.org/3/library/stdtypes.html?highlight=join#bytes) objects. The separator between elements is the string providing this method.
- **xrange()** 函数用法与 [range](https://www.runoob.com/python/pytho-func-range.html) 完全相同，所不同的是生成的不是一个数组，而是一个生成器。



##### 疑问

- ==只有生成器表达式才能使用next(),生成器函数就不可以？==





### 反思

- 在分析代码时候我貌似在重复造轮子了