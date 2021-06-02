from dbutil import *
import numpy as np

#用户相关操作
def register_check_phone_existence(phone_number):
    """
    这个函数判断传入的phone_number是否已经存在
    :param phone_number:
    :return:is_phone_number_existence,bool
    """

    if type(phone_number) != type(1):
        return False
    res = CYWDB.query('User', {"user_phonenumber": phone_number}, ["user_name"])
    return len(res) != 0

def register_check_mail_existence(mail):
    """
    这个函数判断传入的mail是否存在
    :param phone_number:
    :return:is_phone_number_existence,bool
    """
    if type(mail) != type('str'):
        return False
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

    assert(len(goodIdList) >= 10)
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
    插入私信
    :param user_id:         用户id
    :param target_user_id:      目标用户id
    :param content:               私信内容
    :param time:                       发送时间
    :return:None
    """
    CYWDB.insert('Message', [user_id, target_user_id, content, time])
    res = CYWDB.query('Message', {'ms_time': time}, ['ms_id'])
    assert(len(res) == 1)
    CYWDB.insert('UnreadMessage', [res[0]['ms_id'], target_user_id])

def insert_reply(user_id, target_id, target_type, content, time):
    """
    插入回复
    :param user_id:
    :param target_id:
    :param target_type: 只能为 Comment Reply
    :param content:
    :param time:
    :return:None
    """
    assert(target_type=='Comment' or target_type=='Reply')
    if target_type == 'Comment':
        res = CYWDB.query('Comment', {'cm_id': target_id}, ['cm_publisherid'])
        assert(len(res) == 1)
        receiver = res[0]['cm_publisherid']
    elif target_type == 'Reply':
        res = CYWDB.query('Reply', {'rp_id': target_id}, ['rp_senderid'])
        assert(len(res) == 1)
        receiver = res[0]['rp_senderid']

    CYWDB.insert('Reply', [user_id, target_id, target_type, content, time])
    res = CYWDB.query('Reply', {'rp_time': time}, ['rp_id'])
    assert(len(res) == 1)
    CYWDB.insert('UnreadReply', [res[0]['rp_id'], receiver])

def insert_likes(user_id, target_id, target_type):
    """
    插入点赞
    :param user_id:         点赞用户id
    :param target_id:       点赞目标id
    :param target_type:     点赞目标的类型，只能为 Comment, Article, Reply
    :return:None
    """
    assert(target_type=='Comment' or target_type=='Article' or target_type=='Reply')
    if target_type == 'Comment':
        res = CYWDB.query('Comment', {'cm_id': target_id}, ['cm_publisherid'])
        assert(len(res) == 1)
        receiver = res[0]['cm_publisherid']
    elif target_type == 'Reply':
        res = CYWDB.query('Reply', {'rp_id': target_id}, ['rp_senderid'])
        assert(len(res) == 1)
        receiver = res[0]['rp_senderid']
    elif target_type == 'Article':
        res = CYWDB.query('Article', {'ar_id': target_id}, ['ar_publisherid'])
        assert(len(res) == 1)
        receiver = res[0]['ar_publisherid']
    CYWDB.insert('Likes', [user_id, target_id, target_type])
    res = CYWDB.query('Likes', 
            {'lk_senderid': user_id, 
            'lk_targetid': target_id, 
            'lk_type': target_type}, 
            ['lk_id'])
    assert(len(res) == 1)
    CYWDB.insert('UnreadLikes', [res[0]['lk_id'], receiver])

def insert_comment(user_id, target_id, target_type, content, time):
    """
    插入评论
    :param user_id:         评论用户id
    :param target_id:       目标id
    :param target_type:     目标类型：只能为Good 或 Article
    :param content:         内容
    :param time:            发布时间
    :return:None
    """
    assert(target_type == 'Good' or target_type == 'Article')

    if target_type == 'Article':
        res = CYWDB.query('Article', {'ar_id': target_id}, ['ar_publisherid'])
        assert(len(res) == 1)
        receiver = res[0]['ar_publisherid']
        article_id = target_id
        good_id = -1
    elif target_type == 'Good':
        article_id = -1
        good_id = target_id

    CYWDB.insert('Comment', [article_id, good_id, user_id, content, time])
    res = CYWDB.query('Comment', 
            {'cm_articleid': article_id, 
            'cm_goodid': good_id,
            'cm_publisherid': user_id, 
            'cm_content': content,
            'cm_time': time}, 
            ['cm_id'])
    assert(len(res) == 1)
    
    if target_type == 'Article':
        CYWDB.insert('UnreadComment', [res[0]['cm_id'], receiver])

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
    rres = CYWDB.query('UnreadReply', {"urp_receiverid": user_id}, ["urp_id"])
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

def get_like(user_id):
    """
    这个函数通过user_id获取点赞内容。点赞的内容是一个列表，列表当中是一个like字典，如下：
    {'total','last_like_user','content','like_id'}
    其中，total是指这一个内容（比如说，评论、回复、文章等等）一共有几个人点赞
    last_like_user记录了最后一个点赞用户的名称
    content是被点赞内容（评论、回复、文章等）的一个摘要，比如前十个字
    like_id是被点赞内容的id，以便于找到这个点赞的具体内容
    :param user_id:
    :return:like_list
    """
    user_lks = CYWDB.query('Likes', {'lk_senderid': user_id}, ['lk_targetid', 'lk_type'])

    rtlst = []
    for item in user_lks:
        dct = {}
        
        target_id = item['lk_targetid']
        target_type = item['lk_type']
        res = CYWDB.query('Likes', 
                {'lk_targetid': target_id, 'lk_type': target_type}, 
                ['lk_id', 'lk_senderid'])
        dct['total'] = len(res)
        
        res.sort(key = lambda pir: -pir['lk_id'])
        luserid = res[0]['lk_senderid']
        dct['last_like_user'] = get_user_base_infor(luserid)['name']
        
        if target_type == 'Article':
            #print('target_id', target_id)
            res = CYWDB.query('Article', {'ar_id': target_id}, ['ar_content'])
            assert(len(res) == 1)
            ct = res[0]['ar_content'][:10]
        elif target_type == 'Comment':
            res = CYWDB.query('Comment', {'cm_id': target_id}, ['cm_content'])
            assert(len(res) == 1)
            ct = res[0]['cm_content'][:10]
        elif target_type == 'Reply':
            res = CYWDB.query('Reply', {'rp_id': target_id}, ['rp_content'])
            assert(len(res) == 1)
            ct = res[0]['rp_content'][:10]
        dct['content'] = ct

        dct['like_id'] = target_id

        rtlst.append(dct)

    return rtlst

def get_reply_list(user_id):
    """
    这个函数根据user_id获取新增的回复内容。新增的回复内容是一个列表，列表当中是一个reply字典，如下：
    {'user_name':user_name,'reply_id':reply_id,'type':type,'content':content}
    其中，user_name表示作出回复的这个用户的名称，reply_id指示了当前reply的id
     注意在该函数的语境下，reply既可以指对自己文章的一个comment，也可以指对于comment的reply
    所以，type表示目标内容的类型有两种：comment和reply，content是对reply内容的一个概括（比如说，前几个字）
    :param user_id:
    :return:reply_list
    """
    rres = CYWDB.query('UnreadReply', {"urp_receiverid": user_id}, ["urp_id", "urp_rpid"])
    cres = CYWDB.query('UnreadComment', {"ucm_receiverid": user_id}, ["ucm_id", "ucm_cmid"])

    for item in rres:
        CYWDB.remove('UnreadReply', item)
    for item in cres:
        CYWDB.remove('UnreadComment', item)

    rtlst = []
    for item in rres:
        dct = {}
        res = CYWDB.query('Reply', {'rp_id': item['urp_rpid']}, ['rp_senderid', 'rp_content'])
        assert(len(res) == 1)

        dct['user_name'] = get_user_base_infor(res[0]['rp_senderid'])['name']
        dct['reply_id'] = item['urp_rpid']
        dct['type'] = 'Reply'
        dct['content'] = res[0]['rp_content'][:10]

        rtlst.append(dct)
    
    for item in cres:
        dct = {}
        res = CYWDB.query('Comment', {'cm_id': item['ucm_cmid']}, ['cm_publisherid', 'cm_content'])
        assert(len(res) == 1)

        dct['user_name'] = get_user_base_infor(res[0]['cm_publisherid'])['name']
        dct['reply_id'] = item['ucm_cmid']
        dct['type'] = 'Comment'
        dct['content'] = res[0]['cm_content'][:10]

        rtlst.append(dct)

    return rtlst

def get_collection_list(user_id):
    """
    这个函数根据user_id获取用户最近的收藏内容。收藏内容是一个列表，其中每一个列表当中都是一个infor字典，结构如下：
    {'good_id':good_id,'good_name':good_name,'good_type':good_type}
    :param user_id:
    :return:collection_list
    """
    gres = CYWDB.query('CollectionGood', {"clg_userid": user_id}, 
                    ["clg_goodid", "clg_time"])
    resList = []
    for gdct in gres:
        gid = gdct['clg_goodid']
        res = CYWDB.query('Good', {"good_id": gid}, ["good_name", "good_type"])
        assert(len(res) == 1)

        resList.append({
            'good_type': res[0]["good_type"],
            'good_name': res[0]["good_name"], 
            'good_id': gid, 
            'time': gdct["clg_time"]
        })
    resList.sort(key = lambda dct: -dct['time'])

    resList = resList[: 5]
    for i in range(len(resList)):
        resList[i].pop('time')
    
    return resList

def get_history_list(user_id):
    """
    这个函数的输入和输出形式和上一个函数完全一样，只不过数据访问是从用户的history当中来的
    :param user_id:
    :return:history_list
    """

    gres = CYWDB.query('AccessGood', {"acg_userid": user_id}, 
                    ["acg_goodid", "acg_time"])
    resList = []
    for gdct in gres:
        gid = gdct['acg_goodid']
        res = CYWDB.query('Good', {"good_id": gid}, ["good_name", "good_type"])
        assert(len(res) == 1)

        resList.append({
            'good_type': res[0]["good_type"],
            'good_name': res[0]["good_name"], 
            'good_id': gid, 
            'time': gdct["acg_time"]
        })
    resList.sort(key = lambda dct: -dct['time'])

    resList = resList[: 5]
    for i in range(len(resList)):
        resList[i].pop('time')
    
    return resList

def get_comment_infor(target_id, target_type):
    """
    这个函数根据target_id
    target_type 只能为 Good 或 Article:
    
    对于某一篇文章/商品的评论内容进行返回，
    返回的内容是一个comment_list，list当中的comment如下
    {
    'content':content,
    'username':username,
    'user_id':user_id,
    'id':id,
    'profile_path':profile_path,
    'time':time,
    'like_number':like_number,
    'reply_list':reply_list
    },
    其中，content是指本comment的内容，username是指发送这个评论的用户名称，user_id指发送评论的用户的id，id指评论的id
    profile_path指用户头像的路径，time指评论发送的时间，
    like_number指点赞的数量，
    reply_list指针对这个评论的回复列表，它也是一个列表，每一项的具体结构如下：
    {
    'content':content,'
    username':username,
    'user_id':user_id,
    'id':id,
    'target_user':target_user,
    'target_id':target_id,
    'reply_type':reply_type':reply_type,
    'profile_path':profile_path,
    'time':time,
    'like_number':like_number},
    由于reply可以是针对comment的，
    也可以是针对某一个reply的，所以这里使用了reply_type进行区分reply_type有两个值：reply和comment
    除此之外，这里还有几个参数：target_user是指这条reply回复的用户，target_id是指回复用户的id
    :param target_id:
    :return:comment_list
    """
    assert(target_type == 'Good' or target_type == 'Article')
    if target_type == 'Good':
        resl = CYWDB.query('Comment', 
                {'cm_goodid': target_id, 'cm_articleid': -1}, 
                ['cm_id', 'cm_publisherid', 'cm_content', 'cm_time'])  
    elif target_type == 'Article':
        resl = CYWDB.query('Comment', 
                {'cm_goodid': -1, 'cm_articleid': target_id}, 
                ['cm_id', 'cm_publisherid', 'cm_content', 'cm_time'])  

    rtlst = []
    for item in resl:
        dct = {}
        dct['content'] = item['cm_content']
        dct['username'] = get_user_base_infor(item['cm_publisherid'])['name']
        dct['user_id'] = item['cm_publisherid']
        dct['profile_path'] = get_user_base_infor(item['cm_publisherid'])['profile_path']
        dct['time'] = item['cm_time']
        
        res = CYWDB.query('Likes', {'lk_targetid': item['cm_id'], 'lk_type': 'Comment'}, ['lk_id'])  
        dct['like_number'] = len(res)

        rres = CYWDB.query('Reply', 
                    {'rp_targetid': item['cm_id'], 'rp_type': 'Comment'}, 
                    ['rp_id', 'rp_senderid', 'rp_content', 'rp_time'])
        rplst = []
        for rp in rres:
            ndct = {}
            ndct['content'] = rp['rp_content']
            ndct['username'] = get_user_base_infor(rp['rp_senderid'])['name']
            ndct['user_id'] = rp['rp_senderid']
            ndct['id'] = rp['rp_id']
            ndct['target_user'] = item['cm_publisherid']
            ndct['target_id'] = item['cm_id']
            ndct['reply_type'] = 'Comment'
            ndct['profile_path'] = get_user_base_infor(rp['rp_senderid'])['profile_path']
            ndct['time'] = rp['rp_time']
            
            res = CYWDB.query('Likes', {'lk_targetid': rp['rp_id'], 'lk_type': 'Reply'}, ['lk_id'])  
            ndct['like_number'] = len(res)

            rplst.append(ndct)
        dct['reply_list'] = rplst

        rtlst.append(dct)
    return rtlst
    


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