from gensim.models import Word2Vec

model = Word2Vec.load('embedding')

infor_dict = {}
dict_file = open('ml-1m/movies.dat', encoding='ISO-8859-1')

for line in dict_file.readlines():
    items = line.strip().split("::")
    infor_dict[items[0]] = "%s::%s"%(items[1],items[2])

recommand = model.wv.most_similar('1193')

print(infor_dict['1193'])
for item in recommand:
    print(infor_dict[item[0]])