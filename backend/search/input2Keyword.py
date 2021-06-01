import jieba
from getKeyword import cutWord, keyWrdLst
import numpy as np
import codecs

wvdct = {}
def readWordVec(fileName='wrdvec.txt'):
    with codecs.open(fileName, 'r', encoding='utf-8') as f:
        n, d = map(int, f.readline(-1).strip().split(' '))
        print(n, d)
        for i in range(n):
            if i % 1000 == 999:
                print('read', i, 'of', n)
            itms = f.readline(-1).strip().split(' ')
            wrd = itms[0]
            vec = np.array(list(map(float, itms[1:])))
            wvdct[wrd] = vec
readWordVec()

def getKeyword(wrd):
    # get the most similiar keyword 
    if wrd in keyWrdLst:
        return 1, wrd
    else: 
        if wrd not in wvdct:
            return -1, None
        wrdvec = wvdct[wrd]
        
        mcos = -1
        rkwrd = None  
        for kwrd in keyWrdLst:
            if kwrd not in wvdct:
                continue
            kwrdvec = wvdct[kwrd]
            ccos = np.inner(wrdvec, kwrdvec) / (np.linalg.norm(wrdvec) * np.linalg.norm(kwrdvec))
            if ccos <= 0:
                continue
            if ccos > mcos:
                mcos = ccos
                rkwrd = kwrd
        return mcos, rkwrd

def getKeywordList(text):
    wrds = cutWord(text)
    rtLst = []
    for wrd in wrds:
        mv, kwrd = getKeyword(wrd)
        if kwrd != None:
            rtLst.append((mv, kwrd))
    return rtLst

if __name__ == '__main__':
    #print(cutWord("智能手机"))
    #readWordVec()
    print(getKeyword('手机'))
    print(getKeyword('电话'))
    print(getKeyword('洗衣'))
    print(getKeyword('冷冻'))