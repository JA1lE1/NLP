# LDA tutorial



## 参考

- [徐1达 LDA](<https://www.bilibili.com/video/av24093797?from=search&seid=1446281961805634843>)

## 先验知识

狄利克雷分布 :point_right: beta berbouli

贝叶斯 非参数估计

高斯混合模型（可能需要看完所有的EM）

独立同分布

log-likelihood

最大似然估计 

周博LDA





### 狄利克雷分布

#### 参考

- [徐1达](<https://www.youtube.com/watch?v=qT6CQ9BFDL8&t=181s>)

#### 先验知识

- 概率密度函数
  - 描述连续型随机变量
    - 对于随机变量X，若存在一个**非负**的可积函数f(x)，使得对任意实数x，有$F(x)=\int_{-\infty}^{x} f(t) d t$ 则称X为连续性随机变量。其中f(x)为X的概率分布密度函数，简称概率密度记为X～f(x)**。**
    - ==随机变量==









####  混合高斯模型

- 分布函数 

  - Cumulative Distribution Function 设X是一个

    随机变量，x是任意实数，函数 ![img](https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D110/sign=713b5351f21f3a295ec8d1cfa924bce3/d000baa1cd11728bba7f7eadcafcc3cec2fd2ceb.jpg) 称为X的分布函数。有时也记为 ![img](https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D63/sign=74abd3f98acb39dbc5c06455d11670c0/58ee3d6d55fbb2fbea79ef01444a20a44623dc57.jpg) 。

  - 常见的"高斯曲线"是其概率密度函数

- 参考

  - [徐1达](<https://www.youtube.com/watch?v=C6xjPAIeeRk&list=PLFze15KrfxbF4J6SW-cFqvPQjLr5ZCdyv&index=2>)