import requests
import bs4
import json
import codecs
import time

def keywordHtml(keyword, page=1):
    searchUrlPrefix = 'https://search.jd.com/Search?keyword='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    r = requests.get(searchUrlPrefix + keyword + '&page=' + str(page), headers=headers)
    return r.text

def html2Idlst(html):
    soup = bs4.BeautifulSoup(html)
    itms = soup.find_all('li', {'class': 'gl-item'})
    lst = []
    for itm in itms:
        lst.append(itm.attrs['data-sku'])
    return lst

def itemHtml(id):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    itemUrlPrefix = 'https://item.jd.com/'
    r = requests.get(itemUrlPrefix + id + '.html', headers=headers)
    return r.text

def parseItem(html):
    soup = bs4.BeautifulSoup(html)
    itms = soup.find_all('div', {'class': 'sku-name'})
    name = itms[0].text.strip()

    itms = soup.find_all('ul', {'class': 'parameter2 p-parameter-list'})
    itms = itms[0].find_all('li')
    infos = {}
    for itm in itms:
        s = itm.text.split('：')
        infos[s[0]] = s[1]

    return {
        'name': name,
        'info': infos
    }

def getPrice(id):
    priceUrlPrefix = 'http://p.3.cn/prices/mgets?type=1&skuIds='
    r = requests.get(priceUrlPrefix + id)
    lst = json.loads(r.text)
    return float(lst[0]['p'])

def parseProduct(id):
    html = itemHtml(id)
    dct = parseItem(html)
    price = getPrice(id)
    dct['price'] = price
    return dct

if __name__ == '__main__':
    #from dbutils import *
    #connect()
    #clearGoodslist()
    product_List = []

    for keyword in ['手机', '书桌', '电脑', '冰箱', '空调', '水杯', '洗衣机']:
                    #['水果', '男装', '女装', '图书', '蔬菜', '饮料', '运动']:#
        print('keyword', keyword)
        for page in range(1, 7):
            print('page:', page)

            for ti in range(5):
                try:
                    html = keywordHtml(keyword, page)
                    idlst = html2Idlst(html)
                    if len(idlst) != 0:
                        break
                except:
                    continue

            for id in idlst:
                for ti in range(5):
                    try:
                        dct = parseProduct(id)
                        print('goods_id:', id)
                        print('\tname:', dct['name'])
                        print('\tprice:', dct['price'])
                        print('\tinfo:', dct['info'])
                        product_List.append(dct)
                        break
                    except:
                        continue
                time.sleep(5)

            time.sleep(50)

            with codecs.open('productList.json', 'w', encoding='utf-8') as f:
                json.dump(product_List, f, ensure_ascii=False)

    print(len(product_List))
        #insertGoods(dct['name'], dct['price'])
    #close()