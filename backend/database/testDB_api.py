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

        for i in range(0, 100):
            insert_article(1, 'article' + str(i), str(i), [])
        for i in range(0, 55):
            insert_comment(1, i + 1, 'Article', 'comment' + str(i), i)
        for i in range(0, 52):
            insert_reply(1, i + 1, 'Comment', 'reply1' + str(i), i - 100)
        

        for i in range(2, 52):
            insert_user('User' + str(i), 'pswd', 1, 'mail')
            insert_likes(i, i, 'Article')
            insert_likes(i, i, 'Comment')
            insert_likes(i, i, 'Reply')

            insert_message(i, 1, '', 3 * i + 1)
            
            insert_reply(i, i, 'Comment','' , 3 * i + 2)
            insert_reply(i, i, 'Reply','' , 3 * i + 2 + 100)

        dct0 = get_tips(1)
        self.assertTrue(dct0['likes'])
        self.assertTrue(dct0['reply'])
        self.assertTrue(dct0['message'])
        dct1 = get_tips(1)
        self.assertFalse(dct1['likes'])
        self.assertFalse(dct1['reply'])
        self.assertFalse(dct1['message'])
    
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

    def test_insert_likes_get_like(self):
        CYWDB.connect()
        CYWDB.build()
        
        insert_user("a", "passworda", 1111111, 'a@cyw.com')
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')
        insert_user("c", "passwordb", 1111111, 'b@cyw.com')

        #a, b, c 各写一篇文章
        insert_article(1, 'article_a', 'ctt', [])
        insert_article(2, 'article_b', 'ctt', [])
        insert_article(3, 'article_c', 'ctt', [])

        #abc 给 a文章评论， bc 给 b文章评论， c 给 c文章评论
        insert_comment(1, 1, 'Article', 'comment_a', 1)
        insert_comment(2, 1, 'Article', 'comment_b', 2)
        insert_comment(3, 1, 'Article', 'comment_c', 3)
        insert_comment(2, 2, 'Article', 'comment_b', 4)
        insert_comment(3, 2, 'Article', 'comment_c', 5)
        insert_comment(3, 3, 'Article', 'comment_c', 6)

        #每人给自己文章、评论点赞
        for i in range(1, 4):
            insert_likes(i, i, 'Article')
        insert_likes(1, 1, 'Comment')
        insert_likes(2, 2, 'Comment')
        insert_likes(2, 4, 'Comment')
        insert_likes(3, 3, 'Comment')
        insert_likes(3, 5, 'Comment')
        insert_likes(3, 6, 'Comment')

        #print(get_like(1))
        #print(get_like(2))
        #print(get_like(3))

    def test_insert_comment_get_reply(self):
        CYWDB.connect()
        CYWDB.build()
        
        insert_user("a", "passworda", 1111111, 'a@cyw.com')
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')
        insert_user("c", "passwordb", 1111111, 'b@cyw.com')

        #a 写一篇文章
        insert_article(1, 'article_a', 'ctt', [])

        #abc 给 a文章评论
        insert_comment(1, 1, 'Article', 'comment_a', 1)
        insert_comment(2, 1, 'Article', 'comment_b', 2)
        insert_comment(3, 1, 'Article', 'comment_c', 3)

        #bc回复 a 的评论
        insert_reply(2, 1, 'Comment', 'reply_b', 1)
        insert_reply(3, 1, 'Comment', 'reply_c', 2)

        print(get_reply_list(1))

    def test_insert_collection_get_collection(self):
        CYWDB.connect()
        CYWDB.build()
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        for i in range(1, 51):
            insert_good('Good' + str(i), 1.0, '')
            insert_collection(1, 'Good', i, 2 * i)
        for i in range(1, 51):
            insert_article(1, 'Article' + str(i), '', [i])
            insert_collection(1, 'Article', i, 2 * i + 1)

        lst = get_collection_list(1)
        #for item in lst:
        #    print(item)

    def test_insert_access_get_hislist(self):
        CYWDB.connect()
        CYWDB.build()
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')

        for i in range(1, 51):
            insert_good('Good' + str(i), 1.0, '')
            insert_access(1, 'Good', i, 2 * i)
        for i in range(1, 51):
            insert_article(1, 'Article' + str(i), '', [i])
            insert_access(1, 'Article', i, 2 * i + 1)

        lst = get_history_list(1)
        #for item in lst:
        #    print(item)

    def test_insert_comment_get_reply(self):
        CYWDB.connect()
        CYWDB.build()
        
        insert_user("a", "passworda", 1111111, 'a@cyw.com')
        insert_user("b", "passwordb", 1111111, 'b@cyw.com')
        insert_user("c", "passwordb", 1111111, 'b@cyw.com')

        #a 写一篇文章
        insert_article(1, 'article_a', 'ctt', [])

        #abc 给 a文章评论
        insert_comment(1, 1, 'Article', 'comment_a', 1)
        insert_comment(2, 1, 'Article', 'comment_b', 2)
        insert_comment(3, 1, 'Article', 'comment_c', 3)

        #bc回复 a 的评论
        insert_reply(2, 1, 'Comment', 'reply_b', 1)
        insert_reply(3, 1, 'Comment', 'reply_c', 2)

        lst = get_comment_infor(1, 'Article')
        #print()
        #for item in lst:
        #    print(item)


if __name__ == '__main__':
    unittest.main()