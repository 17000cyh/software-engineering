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
    {'article_name','article_content','article_id','author','related_good_list','id'}
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