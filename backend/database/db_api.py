from dbutil import *

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