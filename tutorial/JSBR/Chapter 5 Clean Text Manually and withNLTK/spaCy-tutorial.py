# -*-coding:utf-8-*-
import spacy
nlp= spacy.load("en_core_web_sm")

## Tokenization
doc = nlp(u"Apple is looking at buying U.K. startup for $1 billion")
print(doc)


