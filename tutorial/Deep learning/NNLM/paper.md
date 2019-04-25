# paper

## NNLM

- 貌似可以结合cs224n的第一个作业

### idea

- 这边应该是在做语言模型的入门
  - [知乎参考](<https://zhuanlan.zhihu.com/p/40096816>)
  - 这篇对词的表示，即语言的表征学习做了还算全的概述
- 当然现在**语言模型** 应该是已经发展到了ELMo 和BERT等。这个是后面学习的事情。
- 当前主流的语言模型？
  - word2vec/glove/fastText/elmo/GPT/bert



### A Neural Probabilistic Language Model

#### 网络

- 简单的三层的前向神经网络，输入层是context的word embedding的联合，需要预先选择context的窗口大小。一层隐藏层。输出层是词表中每个词的概率，长度为词表大小。图中虚线表示输入层与输出层的直连。
- ![nnlm](E:/work/github/JA1lE1.github.io/My_Daily_Work/%E7%AC%94%E8%AE%B0/2019/4%E6%9C%88/pictures/paper/nnlm.png)

#### 公式

$$
\begin{array}{l}{x=\left(C\left(w_{t-1}\right), C\left(w_{t-2}\right), \ldots, C\left(w_{t-n+1}\right)\right)} \\ {y=b+W x+U \tanh (d+H x)} \\ {\hat{P}\left(w_{t} | w_{t-1}, \ldots, w_{t-n+1}\right)=\frac{e^{y_{w_{t}}}}{\sum_{i} e^{y_{i}}}}\end{array}
$$

#### ==等待==



## 