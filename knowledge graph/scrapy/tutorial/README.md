# README

## Heima

```
/html/body/div[1]/div[5]/div[2]/div[2]/ul/li[1]/div[2]
```



### items.py

```
name
level
info
```



## 基本步骤

- 创建爬虫scrapy的项目
  - scrapy startproject XXXX
- 生成爬虫
  - scrapy genspider   mmm（name） "website"
- 提取数据
  - 使用Xpath
- 保存数据
  - 在pipeline中保存

## 重点记录

- scrapy 特殊定义list 可以使用extract()

- lOGGING 的等级设置

  - LOG_LEVEL = "WARNING"
  - 在setting.py下设置

- pipelines.py中可以设置多个pipeline

  - 对应的需要在setting中设置响应的优先级（权重）

  - ```python
    ITEM_PIPELINES = {
        'mySpider.pipelines.MyspiderPipeline': 300,
    }
    # 在setting中原本是被注释了 需要取消注释
    ```

- 这边items.py 的作用是 可以在 spider(主爬虫文件中导入先关的类 比如 在mySpider中是itcast.py)

  - itcast.py中 yield 的==返回值== 可以是 dict 可以是 scrapy.Item的子类(==这里在class中传入一个类是表示当前类继承传入的子类？？==) 

- parse

  - 返回值必须是==Request BaseItem dict or None==
  - parse名字不能修改为其他 对应的pipeline中 的def方法名字也不能改

##  心得

- 说出来我自己都不信 scrapy的第一个bug我居然调了一天之久
  - 在此期间 我由于==过于急躁== 导致没有看清win环境下的bug(scrapy的logging太多 我没有细看 这里是由于python write 文件的时候 encoding = 'utf-8' 没有写导致的)
  - 我拓展了linux 环境下 的vim的两种方法 和新的micro 编辑器 说句实在话 还是很ZZ