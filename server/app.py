import json

import uuid

from flask import Flask, request, jsonify

from software_engering.db_function import *

import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/register')
def register():
    data = json.loads(request.form.get('data'))
    infor = dict()

    phone_number = data['phone_number']
    if register_check_phone_existence(phone_number):
        infor['regist_success'] = False
        infor['wrong_code'] = 1
        return jsonify(infor)

    mail = data['mail']
    if register_check_mail_existence(mail):
        infor['regist_success'] = False
        infor['wrong_code'] = 2
        return jsonify(infor)

    username = data['username']
    password = data['password']
    insert_user(username=username,phone=phone_number,password=password,mail=mail)

    infor['regist_success'] = True
    infor['wrong_code'] = 1

    return jsonify(infor)

@app.route('/load')
def load():
    data = json.loads(request.form.get('data'))
    infor = {}
    mail = data['mail']
    password = data['password']
    if load_check_user_existence(mail) == False:
        infor['load_success'] = False
        infor['wrong_code'] = 1
        infor['user_id'] = 0
        return jsonify(infor)

    load_result = load_password_right(mail,password)
    if load_result == False:
        infor['load_success'] = False
        infor['wrong_code'] = 2
        infor['user_id'] = 0
        return jsonify(infor)

    else:
        infor['load_success'] = True
        infor['wrong_code'] = 0
        infor['user_id'] = load_result
        return jsonify(infor)

@app.route('/index')
def index():
    # 这个函数本来应该是利用用户的历史记录之类进行推荐的，但是现在推荐没有做出来
    # 就先随便选吧
    infor = {}
    article_list = get_random_ten_article()
    for article in article_list:
        related_good_infor = []
        related_good_list = article['related_good_list']
        for good_id in related_good_list:
            related_good_infor.append(get_good_base_infor(good_id))
        article['related_good_infor'] = related_good_infor
    infor['article_list'] = article_list

    







if __name__ == '__main__':
    app.run()
