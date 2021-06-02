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
    data = json.loads(request.form.get('data'))
    user_id = data['user_id']

    infor = {}
    article_list = get_random_ten_article()
    for article in article_list:
        related_good_infor = []
        related_good_list = article['related_good_list']
        for good_id in related_good_list:
            related_good_infor.append(get_good_base_infor(good_id))
        article['related_good_infor'] = related_good_infor
    infor['article_list'] = article_list

    collection = get_five_user_collection(user_id)
    history = get_five_user_history(user_id)

    user_infor = {'collection':collection,'history':history}

    tips = get_tips(user_id)
    infor['user_infor'] = user_infor
    infor['tips'] = tips

    return jsonify(infor)

@app.route('/follow')
def follow():
    # 该函数和上一个函数在本阶段是一样的。
    data = json.loads(request.form.get('data'))
    user_id = data['user_id']

    infor = {}
    article_list = get_random_ten_article()
    for article in article_list:
        related_good_infor = []
        related_good_list = article['related_good_list']
        for good_id in related_good_list:
            related_good_infor.append(get_good_base_infor(good_id))
        article['related_good_infor'] = related_good_infor
    infor['article_list'] = article_list

    collection = get_five_user_collection(user_id)
    history = get_five_user_history(user_id)

    user_infor = {'collection': collection, 'history': history}

    tips = get_tips(user_id)
    infor['user_infor'] = user_infor
    infor['tips'] = tips

    return jsonify(infor)

@app.route('/hot')
def get_hot():
    data = json.loads(request.form.get('data'))
    user_id = data['user_id']

    infor = {}
    good_list = get_random_ten_good()

    infor['good_list'] = good_list

    collection = get_five_user_collection(user_id)
    history = get_five_user_history(user_id)

    user_infor = {'collection': collection, 'history': history}

    tips = get_tips(user_id)
    infor['user_infor'] = user_infor
    infor['tips'] = tips

    return jsonify(infor)

@app.route('/user_center/space/message')
def get_message():
    # 这个函数用于当用户访问个人中心的私信界面时，传送对应的信息。
    data = json.loads(request.form.get('data'))
    user_id = data['user_id']

    user_id_list = get_user_communicate(user_id)
    user_list = []
    for user_id in user_id_list:
        user_list.append(get_user_base_infor(user_id))


    messages = get_message_between_two(user_id,user_list[0]['user_id'])
    infor = {'users':user_list,'messages':messages}
    return jsonify(infor)

@app.route('/get_message')
def get_message():
    data = json.loads(request.form.get('data'))
    user_id = data['user_id']
    target_user_id = data['target_user_id']

    messages = get_message_between_two(user_id,target_user_id)
    return jsonify({'messages':messages})

@app.route('/send_message')
def send_message():
    data = json.loads(request.form.get('data'))
    user_id = data['user_id']
    target_user_id = data['target_user_id']
    content = data['content']
    now_time = time.time()

    insert_message(user_id,target_user_id,content,now_time)

@app.route('/get_like')
def get_like_list():
    data = json.loads(request.form.get('data'))
    user_id = data['user_id']
    like_list = get_like(user_id)
    return jsonify({'like_list':like_list})






if __name__ == '__main__':
    app.run()
