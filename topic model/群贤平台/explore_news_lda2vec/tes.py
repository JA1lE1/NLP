from data_prepare import news_prepare

i = 0
for text in news_prepare('cn_sina.csv'):
    print(text)
    print()
    i = i+1
    if i > 4:
        break