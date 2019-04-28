# README



## 2019.4.27

- 主要对于论文和代码中的lossfunction的理解，以cs229的讲义为主进行学习

## NNLM

### 需要理解的点

- ngram的目标是，输入输出是？，为什么采用NLLLoss function？
- NNLM与ngram改进的点在哪里，为什么它能够比ngram达到较好的效果
- NNLM和ngram的目标是一样的嘛

### 疑惑点

- MLE





### 对数似然函数

- 二分类

  - [知乎](<https://www.zhihu.com/question/27126057>)

  - 分几步简化描述下：

    （1）有一类概率型的目标函数，例如逻辑回归来解决二分类问题，假设其目标函数为p(x)，可以简单理解为样本x归属到某一类别的概率。

    （2）根据最大似然估计的理论，优化目标是使得P(X)=p(x1)(1-p(x2))p(x3)...最大化（这里假设x1和x3是正例，x2是负例，由于**目标函数是求正例的概率**，所以1-p(x)自然就是负例的概率）。

    （3）乘法表达式求极值比较麻烦，所以最好想办法转化成加法表达式。最自然的想法是两边取对数，把等式右边转化为加法表达式。由于对数单调增，那么求P(X)的最大值的问题，可以转化为求logP(X) 的最大值的问题。

    （4）求logP(X)的最大值，其实就是求-logP(X)的最小值。这个-logP(X)其实就是所谓的log loss了。

    （5）log loss本身的求解可以使用梯度下降等各种方法。log loss只代表了一个从原始的loss到log形式loss的转化过程。

    作者：Jean

    链接：https://www.zhihu.com/question/27126057/answer/532087859

    来源：知乎

  - [cs229的讲义](![1556346187243](C:\Users\ALEX\AppData\Roaming\Typora\typora-user-images\1556346187243.png))

    - 对logistic loss function 有个较好的理解
      - 下一步可以对该讲义的[1-3部分](<https://kivy-cn.github.io/Stanford-CS-229-CN/#/Markdown/cs229-notes1>) 好好看一下，顺便补一补概率统计的知识

- 多分类

  - cs231n
  - 



### future work

- 由于今天看复联，因此先到这，下一步应该是对negative likelihood loss function 以及CrossEntropy与logistics loss的区别 以及 log_softmax 这些之间的区别和联系，这里由于编码基于pytorch框架，这里可以借鉴[这篇文章](<https://blog.csdn.net/zhangxb35/article/details/72464152>)深入