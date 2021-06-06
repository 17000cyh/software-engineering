import jieba
import json
import numpy as np

def load_data(fileList):
    goods = []
    for dataFile in fileList:
        goodList = json.load(open(dataFile, "r"))

        for i, goodDct in enumerate(goodList):
            name = goodDct['name']
            price = str(goodDct['price'])
            info = goodDct['info']
            infoStr = ""
            for k, v in info.items():
                infoStr += k + ":" + v + '，'
            
            goods.append([i + 1, name + infoStr])
    return goods

uselessWord = {'，', ':', '(', ')', ' ', '>', '-', '（', '）', '/', '；', '+', '~'}
def cutWord(infoStr, cut_all = False):
    words = jieba.cut(infoStr, cut_all=cut_all)
    words = [x for x in words if x not in uselessWord]
    return words

def getWordDct(goods):
    goodsWrdDct = []
    for id, goodInfo in goods:
        #print(goodInfo)
        dct = {}
        wrds = cutWord(goodInfo)
        for wrd in wrds:
            if wrd in dct:
                dct[wrd] += 1
            else:
                dct[wrd] = 1
        
        n_wrds = len(wrds)
        for wrd in dct.keys():
            dct[wrd] /= n_wrds
        
        goodsWrdDct.append([id, dct])
    
    #TF for good word pair
    return goodsWrdDct

def getKeyword(goodsWrdDct):
    wordcnt = {}
    for id, wrdlst in goodsWrdDct:
        for wrd in wrdlst:
            if wrd not in wordcnt:
                wordcnt[wrd] = 0
            else: 
                wordcnt[wrd] += 1
    num_goods = len(goodsWrdDct)

    idfs = {}
    for wrd in wordcnt.keys():
        idfs[wrd] = np.log(num_goods / (wordcnt[wrd] + 1)) / np.log(10.0)

    keyWrdLst = {}
    min_tf_idf = 0.01
    min_occur = 10
    max_occur = len(goodsWrdDct) / 5
    for id, wrdlst in goodsWrdDct:
        #print(id)
        for wrd in wrdlst.keys():
            wrdlst[wrd] *= idfs[wrd]
        eraseWrds = []
        for wrd, tfidf in wrdlst.items():
            if tfidf >= min_tf_idf  and wordcnt[wrd] > min_occur and wordcnt[wrd] < max_occur:
                keyWrdLst[wrd] = 0
                #print('\t', wrd, tfidf)
            else:
                eraseWrds.append(wrd)
        for wrd in eraseWrds:
            wrdlst.pop(wrd)
    keyWrdLst = list(keyWrdLst.keys())

    return goodsWrdDct, keyWrdLst

goodsKeyword = None
keyWrdLst = None
def getKeywordBuild():
    global goodsKeyword, keyWrdLst
    goods = load_data(['../jdspider/pL1.json'])
    goodsWrdDct = getWordDct(goods)
    goodsKeyword, keyWrdLst = getKeyword(goodsWrdDct)
getKeywordBuild()

if __name__ == '__main__':
    goods = load_data(['../jdspider/pL1.json'])
    goodsWrdDct = getWordDct(goods)
    goodsKeyword, keyWrdLst = getKeyword(goodsWrdDct)
    print(len(keyWrdLst))
