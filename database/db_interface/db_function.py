import sqlite3

conn = sqlite3.connect('data/data.db')
cursor = conn.cursor()


def register_check_phone_existence(phone_number):
    """
    这个函数判断传入的phone_number是否已经存在

    :param phone_number:
    :return:is_phone_number_existence,bool
    """
    pass


def register_check_mail_existence(mail):
    """
    这个函数判断传入的mial是否存在

    :param phone_number:
    :return:is_phone_number_existence,bool
    """
    pass

def insert_user(username,phone,mail,password):
    """
    这个函数插入一个用户注册的内容

    :param username:
    :param phone:
    :param mail:
    :param password:
    :param user_id:
    :return:None
    """
    pass


def load_check_user_existence(mail):
    """
    该函数根据mail的值判断用户是否存在，如果不存在返回False
    :param mail:
    :return:is_user_existence
    """
    pass

def load_password_right(mail,password):
    """
    这个函数用于判断邮箱和密码是否匹配。如果匹配的话返回用户的id。否则，返回Flase
    :param mail:
    :param password:
    :return:
    """
    pass

def get_random_ten_article():
    """
    这个函数获取10篇随机的文章
    :return:article_list
    返回一个列表，列表当中的每一个元素都是一个字典，键包括：
    {'article_name','article_content','id','author','related_good_list'}
    其中，related_good_list是一个关联商品id的列表
    """
    pass

def get_good_base_infor(id):
    """
    这个函数根据商品的id获取商品的基本信息。返回的内容将是一个字典，字典的键如下：
    {'good_name','good_type','id'}
    :param id:
    :return:good_infor
    """
    pass

def get_five_user_collection(user_id):
    """
    这个函数根据user的id获取他最近收藏的五个商品或者文章的信息（这个地方如果不好做就先随机选也行），返回是一个list。list当中的每一个元素是一个字典，如下：
    {'type','name','id'}
    由于用户的收藏可能是一个文章，也可能是一个商品，所以这个地方需要用type标记出来
    如果用户收藏的是文章，则'name'表示文章的title。如果收藏的是商品，则表示的就是商品的名称。
    :param user_id:
    :return:collection_list
    """
    pass

def get_five_user_history(user_id):
    """
    这个函数根据user的id获取他最近访问的五个商品或者文章的信息（这个地方如果不好做就先随机选也行），返回是一个list。list当中的每一个元素是一个字典，如下：
    {'type','name','id'}
    由于用户访问的可能是一个文章，也可能是一个商品，所以这个地方需要用type标记出来
    如果用户访问的是文章，则'name'表示文章的title。如果访问的是商品，则表示的就是商品的名称。
    :param user_id:
    :return:history_list
    """
    pass

def get_tips(user_id):
    """
    这个函数根据user的id，查看user是否有没有阅读的消息。
    一般而言，当用户获得一个点赞，或者有人私信用户，或者有人评论用户时，需要在数据库中某一个"未读"表当中进行更新
    当用户阅读了这些信息的时候，再讲这些信息进行删除。
    返回是一个字典Tips,如下：
    {'likes':一个布尔值，表示是否有新增的点赞,'reply':布尔值，有无新回复,'message':布尔值，有无新私信}

    :param user_id:
    :return:tips
    """
    pass

def get_random_ten_good():
    """
    这个函数获取十个随机的商品信息，返回是一个good_list列表，列表当中的每一个元素是一个字典good，
    good的元素如下：
    {'name':商品的名称,'img_path':商品的图片路径,'type':商品的类型,'price':商品的架构}
    :return:good_list
    """
    pass


def get_user_communicate(user_id):
    """
    这个函数通过用户的id，找出了所有和用户有过交谈的人，并且按照最后一次交谈的时间形成了一个列表
    列表当中的内容是与之交谈的用户的id，其中，最后一个与之交谈的用户的id放在最前面
    :param user_id:
    :return:user_communicate_list
    """
    pass

def get_user_base_infor(user_id):
    """
    这个函数获取了用户的基本信息，包括名称、头像以及id，即：
    {'name','profile_path','user_id'}
    :param user_id:
    :return:infor
    """
    pass

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
    pass

def insert_message(user_id,target_user_id,content,time):
    """
    这个函数插入一些私信的信息
    :param user_id:
    :param target_user_id:
    :param content:
    :return:None
    """

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

def get_collection_list(user_id):
    """
    这个函数根据user_id获取用户最近的收藏内容。收藏内容是一个列表，其中每一个列表当中都是一个infor字典，结构如下：
    {'good_id':good_id,'good_name':good_name,'good_type':good_type}
    :param user_id:
    :return:collection_list
    """

def get_history_list(user_id):
    """
    这个函数的输入和输出形式和上一个函数完全一样，只不过数据访问是从用户的history当中来的
    :param user_id:
    :return:history_list
    """

def get_comment_infor(target_id):
    """
    这个函数根据target_id对于某一篇文章/商品的评论内容进行返回，返回的内容是一个comment_list，list当中的comment如下
    {'content':content,'username':username,'user_id':user_id,'id':id,'profile_path':profile_path,'time':time,'like_number':like_number,
    'reply_list':reply_list},
    其中，content是指本comment的内容，username是指发送这个评论的用户名称，user_id指发送评论的用户的id，id指评论的id
    profile_path指用户头像的路径，time指评论发送的时间，like_number指点赞的数量，reply_list指针对这个评论的回复列表，它也是一个列表，每一项的具体结构如下：
    {'content':content,'username':username,'user_id':user_id,'id':id,'target_user':target_user,'target_id':target_id,'reply_type':reply_type':reply_type,'profile_path':profile_path,'time':time,'like_number':like_number},
    由于reply可以是针对comment的，也可以是针对某一个reply的，所以这里使用了reply_type进行区分reply_type有两个值：reply和comment
    除此之外，这里还有几个参数：target_user是指这条reply回复的用户，target_id是指回复用户的id
    :param target_id:
    :return:comment_list
    """