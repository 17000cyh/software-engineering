"""
这个文件用于实现一个简单的协同过滤算法。
基本思路是计算商品的相似度（因为用户的变化量比较明显，但是商品的数量是比较稳定的）
计算的方法是：
首先建立商品向量，即1:3.5,2：4这样的字典
然后构造一个商品相似度矩阵
"""

import csv


def build_good_vector(path):
    source = csv.reader(open(path))
    good_dict = {}
    first = True
    for item in source:
        if first:
            first = False
            continue
        user_id = int(item[0])
        good_id = int(item[1])
        rating = float(item[2])
        if good_id not in good_dict.keys():
            good_dict[good_id] = {}
            good_dict[good_id][user_id] = rating
        else:
            good_dict[good_id][user_id] = rating
    return good_dict


# print(build_good_vector('data/ratings.csv'))
def compute_distance(good_vector1, good_vector2):
    distance_square = 0
    for key in good_vector1.keys() - good_vector2.keys():
        distance_square += good_vector1[key] ** 2
    for key in good_vector2.keys() - good_vector1.keys():
        distance_square += good_vector2[key] ** 2
    for key in good_vector2.keys() & good_vector1.keys():
        distance_square += (good_vector1[key] - good_vector2[key]) ** 2
    return distance_square ** 0.5


def add_vectors(vector_list):
    result = {}
    length = len(vector_list)
    for vector in vector_list:
        for key in vector.keys() - result.keys():
            result[key] = vector[key]
        for key in vector.keys() & result.keys():
            result[key] += vector[key]
    for key in result.keys():
        result[key] = result[key] / length
    return result

def compute_sim(target,good_vectors):
    distance_result = {}
    for key in good_vectors.keys():
        distance_result[key] = compute_distance(target,good_vectors[key])
    result = sorted(distance_result.items(),key=lambda d:d[1])
    return result

def read_good_index_dict(path):
    source = csv.reader(open(path,encoding='utf-8'))
    first = True
    result = {}
    for item in source:
        if first:
            first = False
            continue
        result[int(item[0])] = "%s;%s"%(item[1],item[2])
    return result

def find_sim(target,good_vectors,good_index,top):
    result = {}
    sort_tuple = compute_sim(target,good_vectors)
    for i in range(1,top+1):
        result[sort_tuple[i][0]] = good_index[sort_tuple[i][0]]
    return result


good_index = read_good_index_dict('data/movies.csv')
good_vector_list = build_good_vector('data/ratings.csv')
print(good_vector_list.keys())
print(find_sim(good_vector_list[1],good_vector_list,good_index,10))