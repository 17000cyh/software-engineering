from dbutil import *
import numpy as np

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
    CYWDB.insert('User', [username, password, phone, mail, ""])

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
    res = CYWDB.query('User', {"user_email": mail}, ["id", "user_password"])
    assert(len(res) == 1)
        
    if password == res[0]["user_password"]:
        return res[0]["user_id"]
    else:
        return False

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

        publisherId = res[0]["ar_id"]
        pres = CYWDB.query('User', {"user_id": publisherId}, ["user_name"])
        assert(len(pres) == 1)
        
        user_name = pres[0]['user_name']

        rres = CYWDB.query('ArticleGood', {"ag_articleid": id}, ["ag_goodid"])
        rresList = [dct["ag_goodid"] for dct in res]

        returnList.append({
                'article_name': res[0]['ar_name'],
                'article_content': res[0]['ar_content'],
                'id': id,
                'author': user_name,
                'related_good_list': rresList,
            }
        )
        
    return returnList

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
        aid = adct['cla_goodid']
        res = CYWDB.query('Article', {"ar_id": aid}, ["ar_name"])
        assert(len(res) == 1)

        resList.append({
            'type': 'article', 
            'name': res[0]["ar_name"], 
            'id': aid, 
            'time': gdct["cla_time"]
        })

    resList.sort(key = lambda dct: dct['time'])

    resList = resList[: 5]
    for i in range(len(resList)):
        resList[i].pop('time')
    
    return resList

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
        aid = adct['aca_goodid']
        res = CYWDB.query('Article', {"ar_id": aid}, ["ar_name"])
        assert(len(res) == 1)

        resList.append({
            'type': 'article', 
            'name': res[0]["ar_name"], 
            'id': aid, 
            'time': gdct["aca_time"]
        })

    resList.sort(key = lambda dct: dct['time'])

    resList = resList[: 5]
    for i in range(len(resList)):
        resList[i].pop('time')
    
    return resList

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

    return {
        'likes': len(lres) != 0,
        'reply': len(rres) != 0,
        'message': len(mres) != 0
    }

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