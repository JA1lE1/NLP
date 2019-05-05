from gensim.corpora import WikiCorpus

space = b" "
i = 0
output = open('wiki-zh-article.txt', 'wb')
wiki = WikiCorpus('zhwiki-latest-pages-articles.xml.bz2', lemmatize = False, dictionary = {})
for text in wiki.get_texts():
    output.write(space.join(text) + b"\n")
    i = i + 1
    if (i % 10000 == 0):
        print("Saved " + str(i) + " articles")

output.close()
print("Finished Saved " + str(i) + " articles")