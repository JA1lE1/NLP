# -*-coding:utf-8-*-
import re
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt', encoding='utf-8')
text = file.read()
file.close()
# words = text.split()   # 返回值是list类型
words = re.split(r'\W+', text)    # 以非单词字符切割字符串
print(words[:100])





