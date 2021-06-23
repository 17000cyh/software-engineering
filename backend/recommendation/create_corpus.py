import gensim

origin = open('ml-1m/ratings.dat')
corpus = open('corpus.txt','w')
user_index = 1
for line in origin.readlines():
    items = line.strip().split("::")
    if int(items[0])!=user_index:
        user_index = int(items[0])
        corpus.writelines('\n')

    if int(items[2]) == 5 or int(items[2])==4:
        corpus.writelines('%s '%items[1])

