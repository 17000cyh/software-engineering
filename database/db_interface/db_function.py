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

def insert_user(username,phone,mail,password,user_id):
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