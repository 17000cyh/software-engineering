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
    但是，在查找的时候需要注意不能仅仅查找从
    :param begin_user:
    :param send_user:
    :return:
    """



