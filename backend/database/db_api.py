from dbutil import *
import numpy as np

#用户相关操作
def register_check_phone_existence(phone_number):
    """
    这个函数判断传入的phone_number是否已经存在
    :param phone_number:
    :return:is_phone_number_existence,bool
    """

    res = CYWDB.query('User', {"user_phonenumber": phone_number}, ["user_name"])
    return len(res) != 0

def register_check_mail_existence(mail):
    """
    这个函数判断传入的mail是否存在
    :param phone_number:
    :return:is_phone_number_existence,bool
    """

    res = CYWDB.query('User', {"user_email": mail}, ["user_name"])
    return len(res) != 0

def insert_user(username,password,phone,mail):
    """
    这个函数插入一个用户注册的内容
    :param username:
    :param phone:
    :param mail:
    :param password:
    :param user_id:
    :return:None
    """
    CYWDB.insert('User', [username, password, phone, mail, "", ""])

def load_check_user_existence(mail):
    """
    该函数根据mail的值判断用户是否存在，如果不存在返回False
    :param mail:
    :return:is_user_existence
    """

    res = CYWDB.query('User', {"user_email": mail}, ["user_name"])
    return len(res) != 0

def load_password_right(mail,password):
    """
    这个函数用于判断邮箱和密码是否匹配。如果匹配的话返回用户的id。否则，返回False
    :param mail:
    :param password:
    :return:
    """
    ""
    res = CYWDB.query('User', {"user_email": mail}, ["user_id", "user_password"])
    if len(res) != 1:
        return False
        
    if password == res[0]["user_password"]:
        return res[0]["user_id"]
    else:
        return False

def get_user_base_infor(user_id):
    """
    这个函数获取了用户的基本信息，包括名称、头像以及id，即：
    {'name','profile_path','user_id'}
    :param user_id:
    :return:infor
    """
    res = CYWDB.query('User', {"user_id": user_id}, ["user_name", "user_profilepath"])
    assert(len(res) == 1)

    return {
        'name': res[0]['user_name'],
        'profile_path': res[0]['user_profilepath'],
        'user_id': user_id
    }

#商品相关操作
def insert_good(good_name, good_price, good_type):
    #插入商品
    CYWDB.insert('Good', [good_name, good_price, good_type, "", ""])

def get_good_base_infor(id):
    """
    这个函数根据商品的id获取商品的基本信息。返回的内容将是一个字典，字典的键如下：
    {'good_name','good_type','id'}
    :param id:
    :return:good_infor
    """
    res = CYWDB.query('Good', {"good_id": id}, ["good_name", "good_type", "good_id"])
    assert(len(res) == 1)
    return {
        'good_name': res[0]['good_name'],
        'good_type': res[0]['good_type'],
        'id': res[0]['good_id']
    }

def get_random_ten_good():
    """
    这个函数获取十个随机的商品信息，返回是一个good_list列表，列表当中的每一个元素是一个字典good，
    good的元素如下：
    {'name':商品的名称,'img_path':商品的图片路径,'type':商品的类型,'price':商品的架构}
    :return:good_list
    """

    res = CYWDB.query('Good', {}, ["good_id"])
    goodIdList = [dct["good_id"] for dct in res]

    choosedId = np.random.choice(goodIdList, 10, replace = False)
    returnList = []
    for i in range(choosedId.shape[0]):
        id = choosedId[i]
        res = CYWDB.query('Good', {"good_id": id},
                ["good_name", "good_type", "good_price", "good_imgpath"])
        assert(len(res)) == 1

        returnList.append({
                'name': res[0]['good_name'],
                'img_path': res[0]['good_imgpath'],
                'type': res[0]['good_type'],
                'price': res[0]['good_price']
            }
        )
        
    return returnList

#文章相关操作
def insert_article(publisher_id, name, content, related_good_list):
    CYWDB.insert('Article', [publisher_id, name, content])
    res = CYWDB.query('Article', 
            {'ar_publisherid': publisher_id, 
                'ar_name': name}, 
            ["ar_id"])
    assert(len(res) == 1)
    article_id = res[0]['ar_id']
    for good_id in related_good_list:
        CYWDB.insert('ArticleGood', [article_id, good_id])

def get_random_ten_article():
    """
    这个函数获取10篇随机的文章
    :return:article_list
    返回一个列表，列表当中的每一个元素都是一个字典，键包括：
    {'article_name','article_content','id','author','related_good_list'}
    其中，related_good_list是一个关联商品id的列表
    """

    res = CYWDB.query('Article', {}, ["ar_id"])
    artclIdList = [dct["ar_id"] for dct in res]

    choosedId = np.random.choice(artclIdList, 10, replace = False)
    returnList = []
    for i in range(choosedId.shape[0]):
        id = choosedId[i]
        res = CYWDB.query('Article', {"ar_id": id},
                ["ar_name", "ar_content", "ar_publisherid"])
        assert(len(res) == 1)

        publisherId = res[0]["ar_publisherid"]
        pres = CYWDB.query('User', {"user_id": publisherId}, ["user_name"])
        assert(len(pres) == 1)
        
        user_name = pres[0]['user_name']

        rres = CYWDB.query('ArticleGood', {"ag_articleid": id}, ["ag_goodid"])
        
        rresList = [dct["ag_goodid"] for dct in rres]

        returnList.append({
                'article_name': res[0]['ar_name'],
                'article_content': res[0]['ar_content'],
                'id': id,
                'author': user_name,
                'related_good_list': rresList,
            }
        )
        
    return returnList

#用户收藏、访问相关
def insert_collection(user_id, collection_type, collection_id, collection_time):
    """
    添加用户收藏
    collection_type = Good | Article
    """
    if collection_type == 'Good':
        CYWDB.insert('CollectionGood', [user_id, collection_id, collection_time])
    elif collection_type == 'Article':
        CYWDB.insert('CollectionArticle', [user_id, collection_id, collection_time])

def get_five_user_collection(user_id):
    """
    这个函数根据user的id获取他最近收藏的五个商品或者文章的信息
    （这个地方如果不好做就先随机选也行），
    返回是一个list。list当中的每一个元素是一个字典，如下：
    {'type','name','id'}
    由于用户的收藏可能是一个文章，也可能是一个商品，
    所以这个地方需要用type标记出来
    如果用户收藏的是文章，则'name'表示文章的title。
    如果收藏的是商品，则表示的就是商品的名称。
    
    :param user_id:
    :return:collection_list
    """

    gres = CYWDB.query('CollectionGood', {"clg_userid": user_id}, 
                    ["clg_goodid", "clg_time"])
    ares = CYWDB.query('CollectionArticle', {"cla_userid": user_id}, 
                    ["cla_articleid", "cla_time"])
    
    resList = []
    for gdct in gres:
        gid = gdct['clg_goodid']
        res = CYWDB.query('Good', {"good_id": gid}, ["good_name"])
        assert(len(res) == 1)

        resList.append({
            'type': 'good', 
            'name': res[0]["good_name"], 
            'id': gid, 
            'time': gdct["clg_time"]
        })
    for adct in ares:
        aid = adct['cla_articleid']
        res = CYWDB.query('Article', {"ar_id": aid}, ["ar_name"])
        assert(len(res) == 1)

        resList.append({
            'type': 'article', 
            'name': res[0]["ar_name"], 
            'id': aid, 
            'time': adct["cla_time"]
        })

    resList.sort(key = lambda dct: -dct['time'])

    resList = resList[: 5]
    for i in range(len(resList)):
        resList[i].pop('time')
    
    return resList

def insert_access(user_id, access_type, access_id, access_time):
    """
    添加用户访问
    access_type = Good | Article
    """
    if access_type == 'Good':
        CYWDB.insert('AccessGood', [user_id, access_id, access_time])
    elif access_type == 'Article':
        CYWDB.insert('AccessArticle', [user_id, access_id, access_time])

def get_five_user_history(user_id):
    """
    这个函数根据user的id获取他最近访问的五个商品或者文章的信息
    （这个地方如果不好做就先随机选也行），
    返回是一个list。list当中的每一个元素是一个字典，如下：
    {'type','name','id'}
    由于用户访问的可能是一个文章，也可能是一个商品，
    所以这个地方需要用type标记出来
    如果用户访问的是文章，则'name'表示文章的title。
    如果访问的是商品，则表示的就是商品的名称。
    :param user_id:
    :return:history_list
    """
    gres = CYWDB.query('AccessGood', {"acg_userid": user_id}, 
                    ["acg_goodid", "acg_time"])
    ares = CYWDB.query('AccessArticle', {"aca_userid": user_id}, 
                    ["aca_articleid", "aca_time"])
    
    resList = []
    for gdct in gres:
        gid = gdct['acg_goodid']
        res = CYWDB.query('Good', {"good_id": gid}, ["good_name"])
        assert(len(res) == 1)

        resList.append({
            'type': 'good', 
            'name': res[0]["good_name"], 
            'id': gid, 
            'time': gdct["acg_time"]
        })
    for adct in ares:
        aid = adct['aca_articleid']
        res = CYWDB.query('Article', {"ar_id": aid}, ["ar_name"])
        assert(len(res) == 1)

        resList.append({
            'type': 'article', 
            'name': res[0]["ar_name"], 
            'id': aid, 
            'time': adct["aca_time"]
        })

    resList.sort(key = lambda dct: -dct['time'])

    resList = resList[: 5]
    for i in range(len(resList)):
        resList[i].pop('time')
    
    return resList

#用户间消息相关
def insert_message(user_id, target_user_id, content, time):
    """
    这个函数插入一些私信的信息
    :param user_id:
    :param target_user_id:
    :param content:
    :return:None
    """
    CYWDB.insert('Message', [user_id, target_user_id, content, time])
    res = CYWDB.query('Message', {'ms_time': time}, ['ms_id'])
    assert(len(res) == 1)
    ms_id = res[0]['ms_id']
    CYWDB.insert('UnreadMessage', [user_id, target_user_id, ms_id])

def insert_reply(user_id, target_user_id, content, time):
    """
    插入回复
    :param user_id:
    :param target_user_id:
    :param content:
    :return:None
    """
    CYWDB.insert('Message', [user_id, target_user_id, content, time])
    res = CYWDB.query('Message', {'ms_time': time}, ['ms_id'])
    assert(len(res) == 1)
    ms_id = res[0]['ms_id']
    CYWDB.insert('UnreadReply', [user_id, target_user_id, ms_id])

def insert_likes(user_id, target_user_id):
    """
    插入点赞
    :param user_id:
    :param target_user_id:
    :return:None
    """
    CYWDB.insert('UnreadLikes', [user_id, target_user_id])

def get_tips(user_id):
    """
    这个函数根据user的id，查看user是否有没有阅读的消息。
    一般而言，当用户获得一个点赞，或者有人私信用户，
    或者有人评论用户时，需要在数据库中某一个"未读"表当中进行更新
    当用户阅读了这些信息的时候，再讲这些信息进行删除。
    返回是一个字典Tips,如下：
    {
        'likes':一个布尔值，表示是否有新增的点赞,
        'reply':布尔值，有无新回复,
        'message':布尔值，有无新私信
    }
    :param user_id:
    :return:tips
    """
    lres = CYWDB.query('UnreadLikes', {"ulk_receiverid": user_id}, ["ulk_id"])
    rres = CYWDB.query('UnreadReply', {"ure_receiverid": user_id}, ["ure_id"])
    mres = CYWDB.query('UnreadMessage', {"ums_receiverid": user_id}, ["ums_id"])

    for item in lres:
        CYWDB.remove('UnreadLikes', item)
    for item in rres:
        CYWDB.remove('UnreadReply', item)
    for item in mres:
        CYWDB.remove('UnreadMessage', item)

    return {
        'likes': len(lres) != 0,
        'reply': len(rres) != 0,
        'message': len(mres) != 0
    }

def get_user_communicate(user_id):
    """
    这个函数通过用户的id，找出了所有和用户有过交谈的人，并且按照最后一次交谈的时间形成了一个列表
    列表当中的内容是与之交谈的用户的id，其中，最后一个与之交谈的用户的id放在最前面
    :param user_id:
    :return:user_communicate_list
    """
    sres = CYWDB.query('Message', {"ms_senderid": user_id}, ["ms_receiverid", "ms_time"])
    rres = CYWDB.query('Message', {"ms_receiverid": user_id}, ["ms_senderid", "ms_time"])

    rList = [{'user': dct['ms_receiverid'], 'time': dct['ms_time']} for dct in sres] +\
                    [{'user': dct['ms_senderid'], 'time': dct['ms_time']} for dct in rres]
    rList.sort(key = lambda dct: -dct['time'])
    
    returnList = []
    rdct = {}   #### hash dict, to accelerate checking process

    for dct in rList:
        id = dct['user']
        if id not in rdct:
            returnList.append(id)
            rdct[id] = 0
    return returnList

def get_message_between_two(begin_user,send_user):
    """
    这个函数获取了用户之间的聊天信息。
    但是，在查找的时候需要注意不能仅仅查找从begin_user查找到send_user，
    也需要查找从send_user到begin_user的信息。
    最终我们的返回将会是一个message_list，这个list的元素都是字典，字典的内容如下：
    {'content':私信的内容,'time':信息发送的时间,'from_user_id':信息发起者的id,'to_user_id':信息接受者的id}
    注意：返回的时候，需要按照时间的先后进行排序，最后发送的消息放到最前面
    :param begin_user:
    :param send_user:
    :return:message_list
    """
    sres = CYWDB.query('Message', {"ms_senderid": begin_user, "ms_receiverid": send_user}, 
                        ["ms_senderid", "ms_receiverid", "ms_content", "ms_time"])
    rres = CYWDB.query('Message', {"ms_senderid": send_user, "ms_receiverid": begin_user}, 
                        ["ms_senderid", "ms_receiverid", "ms_content", "ms_time"])
    res = rres + sres
    res.sort(key = lambda dct: -dct['ms_time'])
    return  [
        {
            'content': dct['ms_content'],
            'time': dct['ms_time'],
            'from_user_id': dct['ms_senderid'],
            'to_user_id': dct['ms_receiverid']
        }
        for dct in res
    ]

#检索商品相关
import sys
sys.path.append('../search')
from getKeyword import getKeywordBuild, goodsKeyword
from input2Keyword import getKeywordList, readWordVec
def retrieval_goods(text):
    """
    输入：搜索的字符串
    输出：排序后列表，每项是 (weight, id)
    weight:相关性权重
    id:商品编号（用于后续获取商品信息）
    """
    kwrdPairs = getKeywordList(text)
    dct = {}
    for mcos, kwrd in kwrdPairs:
        res = CYWDB.query('KeywordGood', {'kg_keyword': kwrd}, ['kg_goodid'])
        for item in res:
            id = item['kg_goodid']
            if id not in dct:
                dct[id] = 0
            dct[id] += mcos
    
    lst = [(dct[id], id) for id in dct.keys()]
    lst.sort(key=lambda pir: -pir[0])
    return lst



if __name__ == '__main__':
    insert_user("a", "password", 1234567, 'a@cyw.com')
    insert_user("b", "password", 1111111, 'b@cyw.com')

    print(register_check_phone_existence(1234567))
    print(register_check_phone_existence(1111111))
    print(register_check_phone_existence(1111112))
    print(register_check_mail_existence('a@cyw.com'))
    print(register_check_mail_existence('c@cyw.com'))

    insert_user("c", "password", 1111112, 'c@cyw.com')
    insert_user("d", "password", 1111113, 'd@cyw.com')

    print(register_check_phone_existence(1234567))
    print(register_check_phone_existence(1111111))
    print(register_check_phone_existence(1111112))
    print(register_check_mail_existence('a@cyw.com'))
    print(register_check_mail_existence('c@cyw.com'))