import jieba
import json


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
            
            goods.append([i, name + infoStr])
    return goods

uselessWord = {'，', ':', '(', ')', ' ', '>', '-', '（', '）', '/', '；', '+', '~'}
def cutWord(infoStr):
    words = jieba.cut(infoStr, cut_all=True)
    words = [x for x in words if x not in uselessWord]
    return words

def getWordDct(goods):
    goodsWrdDct = []
    for id, goodInfo in goods:
        #print(goodInfo)
        dct = {}
        for wrd in cutWord(goodInfo):
            dct[wrd] = 0
        goodsWrdDct.append([id, list(dct.keys())])
    for x in goodsWrdDct:
        print(x)
    return goodsWrdDct

def getKeyword(goodsWrdDct):
    wordcnt = {}
    for id, wrdlst in goodsWrdDct:
        for wrd in wrdlst:
            if wrd not in wordcnt:
                wordcnt[wrd] = 0
            else: 
                wordcnt[wrd] += 1
    
    min_occur = 10
    max_occur = len(goodsWrdDct) / 10
    goodsKeyword = []
    for id, wrdlst in goodsWrdDct:
        wrds = [wrd for wrd in wrdlst 
                    if wordcnt[wrd] > min_occur 
                        and wordcnt[wrd] < max_occur 
                        and len(wrd) >= 2]
        print(id, wrds)
        goodsKeyword.append([id, wrds])
    keyWrdLst = [wrd for wrd in wordcnt.keys()
                        if wordcnt[wrd] > min_occur 
                            and wordcnt[wrd] < max_occur 
                            and len(wrd) >= 2]
    return goodsKeyword, keyWrdLst

goods = load_data(['../jdspider/pL1.json'])
goodsWrdDct = getWordDct(goods)
goodsKeyword, keyWrdLst = getKeyword(goodsWrdDct)

if __name__ == '__main__':
    goods = load_data(['../jdspider/pL1.json'])
    goodsWrdDct = getWordDct(goods)
    goodsKeyword, keyWrdLst = getKeyword(goodsWrdDct)
    print(len(keyWrdLst))
