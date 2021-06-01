import json
import codecs

if __name__ == '__main__':
    goodTypeList = json.load(open("productList.json", "r"))
    goodTypeDct = {dct['id']: dct for dct in goodTypeList}

    rtList = []
    for dataFile in ['pL1.json', 'pL2.json']:
        goodList = json.load(open(dataFile, "r"))

        for goodDct in goodList:
            dct = {}

            name = goodDct['name']
            price = goodDct['price']
            info = goodDct['info']
            if '商品编号' in info:
                id = str(info['商品编号'])
            elif '商品编码' in info:
                id = str(info['商品编码'])
            else:
                print(info)
                input()
            if id in goodTypeDct:
                tp = goodTypeDct[id]['type']
                imgname = id + '.jpg'
                dct['id'] = id
                dct['name'] = name
                dct['price'] = price
                dct['info'] = info
                dct['type'] = tp
                dct['imgpath'] = imgname
                rtList.append(dct)
            else:
                dct['id'] = id
                dct['name'] = name
                dct['price'] = price
                dct['info'] = info
                dct['type'] = ''
                dct['imgpath'] = ''
                rtList.append(dct)
    print(len(rtList))
    with codecs.open('pL.json', 'w', encoding='utf-8') as f:
        json.dump(rtList, f, ensure_ascii=False)
