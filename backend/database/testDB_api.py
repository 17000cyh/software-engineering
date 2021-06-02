import unittest
from db_api import *

class TestDBAPI(unittest.TestCase):
    #用户相关操作
    def test_insert_user_check_phone(self):
        CYWDB.connect()
        CYWDB.build()

        insert_user("a", "passworda", 1234567, 'a@cyw.com')
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        self.assertTrue(register_check_phone_existence(1234567))
        self.assertTrue(register_check_phone_existence(1111111))
        self.assertFalse(register_check_phone_existence(1111112))
        self.assertFalse(register_check_phone_existence(10 ** 100))
        self.assertFalse(register_check_phone_existence('sdfsdaf'))

    def test_insert_user_check_mail(self):
        CYWDB.connect()
        CYWDB.build()

        insert_user("a", "passworda", 1234567, 'a@cyw.com')
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        self.assertTrue(register_check_mail_existence("a@cyw.com"))
        self.assertTrue(register_check_mail_existence("b@cyw.com"))
        self.assertFalse(register_check_mail_existence("c@cyw.com"))
        
        longstr = ''.join(['a' for i in range(10 ** 8)])
        self.assertFalse(register_check_mail_existence(longstr))
        self.assertFalse(register_check_mail_existence(123456))

    def test_insert_user_check_password(self):
        CYWDB.connect()
        CYWDB.build()

        insert_user("a", "passworda", 1234567, 'a@cyw.com')
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        self.assertTrue(load_password_right("a@cyw.com", "passworda"))
        self.assertTrue(load_password_right("b@cyw.com", "passwordb"))
        self.assertFalse(load_password_right("a@cyw.com", "passwordc"))
        self.assertFalse(load_password_right("c@cyw.com", "passworda"))
        
        longstr = ''.join(['a' for i in range(10 ** 8)])
        self.assertFalse(load_password_right("a@cyw.com", longstr))

    def test_insert_user_get_baseinfo(self):
        CYWDB.connect()
        CYWDB.build()

        insert_user("a", "passworda", 1234567, 'a@cyw.com')
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        self.assertTrue(get_user_base_infor(1)['name'] == "a")
        self.assertTrue(get_user_base_infor(2)['name'] == "b")
        self.assertFalse(get_user_base_infor(1)['name'] == "b")

    #商品相关操作
    def test_insert_good_get_baseinfo(self):
        CYWDB.connect()
        CYWDB.build()

        for i in range(1, 51):
            insert_good("good" + str(i), i, "type" + str(i))

        for i in range(1, 51):
            dct = get_good_base_infor(i)
            self.assertTrue(dct['good_name'] == 'good' + str(i))
            self.assertTrue(dct['id'] == i)

    def test_insert_good_get_rand(self):
        CYWDB.connect()
        CYWDB.build()

        for i in range(1, 51):
            insert_good("good" + str(i), i, "type" + str(i))

        lst = get_random_ten_good()
        #for item in lst:
        #    print(item)

    #文章相关操作
    def test_insert_article_get_rand(self):
        CYWDB.connect()
        CYWDB.build()
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        for i in range(1, 51):
            insert_article(1, "article" + str(i), "", [i, i + 1, i + 2])

        lst = get_random_ten_article()
        #for item in lst:
        #    print(item)
    
    #用户收藏、访问相关
    def test_insert_collection_get_recent(self):
        CYWDB.connect()
        CYWDB.build()
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        for i in range(1, 51):
            insert_good('Good' + str(i), 1.0, '')
            insert_collection(1, 'Good', i, 2 * i)
        for i in range(1, 51):
            insert_article(1, 'Article' + str(i), '', [i])
            insert_collection(1, 'Article', i, 2 * i + 1)

        lst = get_five_user_collection(1)
        #for item in lst:
        #    print(item)

    def test_insert_access_get_history(self):
        CYWDB.connect()
        CYWDB.build()
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        for i in range(1, 51):
            insert_good('Good' + str(i), 1.0, '')
            insert_access(1, 'Good', i, 2 * i)
        for i in range(1, 51):
            insert_article(1, 'Article' + str(i), '', [i])
            insert_access(1, 'Article', i, 2 * i + 1)

        lst = get_five_user_history(1)
        #for item in lst:
        #    print(item)

    def test_insert_message_get_tips(self):
        CYWDB.connect()
        CYWDB.build()
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        for i in range(2, 52):
            insert_user('User' + str(i), 'pswd', 1, 'mail')
            insert_likes(i, 1)
            insert_message(i, 1, '', 3 * i + 1)
            insert_reply(i, 1, '', 3 * i + 2)

        #print(get_tips(1))
        #print(get_tips(1))
    
    def test_insert_message_get_communication(self):
        CYWDB.connect()
        CYWDB.build()
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        for i in range(2, 52):
            insert_user('User' + str(i), 'pswd', 1, 'mail')
            insert_message(i, 1, '', 3 * i + 1)
            insert_message(1, i, '', 3 * i + 2)
        #print(get_user_communicate(1))

    def test_insert_message_get_message_betweeen(self):
        CYWDB.connect()
        CYWDB.build()
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')
        insert_user("c", "passwordc", 1111111, 'c@cyw.com')

        for i in range(2, 52):
            insert_message(2, 1, 'Message' + str(2 * i), 3 * i + 1)
            insert_message(1, 2, 'Message' + str(2 * i + 1), 3 * i + 2)

        lst = get_message_between_two(1, 2)
        #for item in lst:
        #    print(item)

if __name__ == '__main__':
    unittest.main()