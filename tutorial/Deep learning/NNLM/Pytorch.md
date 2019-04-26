# Pytorch

## pytorch

### Word Embedding

在自然语言处理中词向量是很重要的，首先介绍一下词向量。

之前做分类问题的时候大家应该都还记得我们会使用`one-hot`编码，比如一共有5类，那么属于第二类的话，它的编码就是(0, 1, 0, 0, 0)，对于分类问题，这样当然特别简明，但是对于单词，这样做就不行了，比如有1000个不同的词，那么使用one-hot这样的方法效率就很低了，所以我们必须要使用另外一种方式去定义每一个单词，这就引出了`word embedding`。

我们可以先举三个例子，比如

1. The cat likes playing ball.
2. The kitty likes playing wool.
3. The dog likes playing ball.
4. The boy likes playing ball.

假如我们使用一个二维向量(a, b)来定义一个词，其中a，b分别代表这个词的一种属性，比如a代表是否喜欢玩飞盘，b代表是否喜欢玩毛线，并且这个数值越大表示越喜欢，这样我们就可以区分这三个词了，为什么呢？

比如对于cat，它的词向量就是(-1, 4)，对于kitty，它的词向量就是(-2, 5)，对于dog，它的词向量就是(3, -2)，对于boy，它的词向量就是(-2, -3)，我们怎么去定义他们之间的相似度呢，我们可以通过他们之间的夹角来定义他们的相似度。 ![Word Embedding](https://ptorch.com/uploads/a7ba7e8078cbbaa4949b56df736586e7.png)

上面这张图就显示出了不同的词之间的夹角，我们可以发现kitty和cat是非常相似的，而dog和boy是不相似的。

而对于一个词，我们自己去想它的属性不是很困难吗，所以这个时候就可以交给神经网络了，我们只需要定义我们想要的维度，比如100，然后通过神经网络去学习它的每一个属性的大小，而我们并不用关心到底这个属性代表着什么，我们只需要知道词向量的夹角越小，表示他们之间的语义更加接近。

下面我们使用pytorch来实现一个word embedding

#### 代码

在pytorch里面实现`word embedding`是通过一个函数来实现的:`nn.Embedding`

```python
# -*- coding: utf-8 -*-
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

word_to_ix = {'hello': 0, 'world': 1}
embeds = nn.Embedding(2, 5)
hello_idx = torch.LongTensor([word_to_ix['hello']])
hello_idx = Variable(hello_idx)
hello_embed = embeds(hello_idx)
print(hello_embed)
```

这就是我们输出的hello这个词的word embedding，代码会输出如下内容，接下来我们解析一下代码：

```python
Variable containing:
 0.4606  0.6847 -1.9592  0.9434  0.2316
[torch.FloatTensor of size 1x5]
```

首先我们需要`word_to_ix = {'hello': 0, 'world': 1}`，每个单词我们需要用一个数字去表示他，这样我们需要hello的时候，就用0来表示它。

接着就是`word embedding`的定义`nn.Embedding(2, 5)`，这里的2表示有2个词，5表示5维度，其实也就是一个2x5的矩阵，所以如果你有1000个词，每个词希望是100维，你就可以这样建立一个`word embedding`，`nn.Embedding(1000, 100)`。如何访问每一个词的词向量是下面两行的代码，注意这里的词向量的建立只是初始的词向量，并没有经过任何修改优化，我们需要建立神经网络通过`learning`的办法修改`word embedding`里面的参数使得`word embedding`每一个词向量能够表示每一个不同的词。

```python
hello_idx = torch.LongTensor([word_to_ix['hello']])
hello_idx = Variable(hello_idx)
```

接着这两行代码表示得到一个`Variable`，它的值是`hello`这个词的`index`，也就是0。这里要特别注意一下我们需要Variable，因为我们需要访问`nn.Embedding`里面定义的元素，并且`word embeding`算是神经网络里面的参数，所以我们需要定义`Variable`。

`hello_embed = embeds(hello_idx)`这一行表示得到`word embedding`里面关于`hello`这个词的初始词向量，最后我们就可以print出来。



------

#### emdedding初始化

默认是随机初始化的

```
import torch
from torch import nn
from torch.autograd import Variable

定义词嵌入

embeds = nn.Embedding(2, 5) # 2 个单词，维度 5

得到词嵌入矩阵,开始是随机初始化的

torch.manual_seed(1)
embeds.weight

输出结果：

Parameter containing:
-0.8923 -0.0583 -0.1955 -0.9656  0.4224
 0.2673 -0.4212 -0.5107 -1.5727 -0.1232
[torch.FloatTensor of size 2x5]

```

如果从使用已经训练好的词向量，则采用

```
pretrained_weight = np.array(args.pretrained_weight)  # 已有词向量的numpy

self.embed.weight.data.copy_(torch.from_numpy(pretrained_weight))

```



作者：乐且有仪 
来源：CSDN 
原文：https://blog.csdn.net/david0611/article/details/81090371 
版权声明：本文为博主原创文章，转载请附上博文链接！

------

#### 详解整个过程

Embeding层：
输入shape:(batchsize, sequence_length)
输出shape:(batchsize,embedding_dim)

事实上，我们这里提到的Embedding层在我们之前介绍的word embedding中也只是一部分模块。

看下面例子：
[![Word_1](https://yifdu.github.io/2018/12/05/Embedding%E5%B1%82/Word_1.png)](https://yifdu.github.io/2018/12/05/Embedding层/Word_1.png)
上图的流程是把文章中的单词使用词向量来表示。
(1)提取文章所有的单词，把所有单词降序排序(取前50000个，表示常出现的单词).
(2)每个编号ID都可以使用50000维的二进制(one-hot)表示
(3)最后，我们会产生一个矩阵M，行大小维词的个数5000，列大小为词向量的维度(嵌入的维度)，比如矩阵的第一行就是编号ID=0，即network对应的词向量

------



### 疑问

- 训练必须是torch.LongTensor??
- x = torch.tensor([2.0], requires_grad=True)
  - 这里如果我没设置requites_grad = True 的话是否会出问题？
    - 这一点在下面的风格迁移指南中有介绍1.2部分

### 1.0版本所带来的不同

- 有关Variable的变动

  - > 
    >
    > The Variable API has been deprecated: Variables are no longer necessary to use autograd with tensors. Autograd automatically supports Tensors with `requires_grad` set to `True`. Below please find a quick guide on what has changed:
    >
    > - `Variable(tensor)` and `Variable(tensor, requires_grad)` still work as expected, but they return Tensors instead of Variables.
    > - `var.data` is the same thing as `tensor.data`.
    > - Methods such as `var.backward(), var.detach(), var.register_hook()` now work on tensors with the same method names.
    >
    > In addition, one can now create tensors with `requires_grad=True` using factory methods such as [`torch.randn()`](https://pytorch.org/docs/stable/torch.html#torch.randn), [`torch.zeros()`](https://pytorch.org/docs/stable/torch.html#torch.zeros), [`torch.ones()`](https://pytorch.org/docs/stable/torch.html#torch.ones), and others like the following:
    >
    > ```python
    > autograd_tensor = torch.randn((2, 3, 4), requires_grad=True)
    > ```

- ==[版本迁移指南](https://github.com/bat67/pytorch-tutorials-examples-and-books/blob/master/PyTorch版本变化及迁移指南/README.md)==

#### ==待做==

- predict的部分需要再修改一下（可能）
- model的部分，也就是论文的Neural Model的部分需要再详细研究一下



---

### 2019.4.26

### pytorch

- [官网的DL for NLP的tutorial](<https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html>)
  - n-gram
    - log_softmax
      - ==为什么使用这个激活函数==
    - NLLLoss()
      - The negative log likelihood loss
    - 以上两者的结合？？

