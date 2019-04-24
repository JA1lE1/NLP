# README

## js-dnl

- 读取文件出现\ufeff

  - 使用notepad+进行转码 转成纯的utf-8
  - [参考](<https://blog.csdn.net/shuihupo/article/details/85039845>)

- ```python
  import string
  string.punctuation()
  ```

### 胖子车神

- Sometimes text data may contain non-printable characters.  We can use a similar approach tofilter out all non-printable characters by selecting the inverse of thestring.printableconstant

### 买GTR吧

- 遇到NLTK的时候貌似spaCy比NLTK好用很多
- spaCy
- NLTK
- Gensim



### spaCy tutorial

- spaCy的停用词在

  - ```
    import spacy
    
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
    
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)
    ```

  - 



### 停用词

- [github-中文停用词](<https://github.com/goto456/stopwords>)

- stop word主要是两类

  一种是虚词、没什么意思，留在里面没有什么预测能力

  一种是太常见的词，你有我有全都有，留在里面也没有什么差异性

  就中文来说，常见的stop word：

  **"的", "了", "在", "是", "我", "有", "和", "就",  "人", "都", "一", "一个", "上", "也", "很", "到", "说", "要", "去", "你",   "会", "着", "好", "自己", "这"**