import gensim
from gensim.models import word2vec

sentences = word2vec.Text8Corpus('corpus.txt')

model=gensim.models.Word2Vec(sentences,sg=1,window=5,min_count=2,negative=3,sample=0.001,hs=1,workers=4)

model.save('embedding')