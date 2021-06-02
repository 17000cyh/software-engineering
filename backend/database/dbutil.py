import sqlite3
import os

class Field:
    def __init__(self, name, isKey, dataType, canbeNull, foreignKey = ""):
        self.name = name
        self.isKey = isKey
        self.dataType = dataType
        self.canbeNull = canbeNull
        self.foreignKey = foreignKey
class Table:
    def __init__(self, name, fieldList):
        self.name = name
        self.fieldList = fieldList
        self.name2field = {}
        for field in fieldList:
            self.name2field[field.name] = field

def filtV(v):
    symbolList = ['\'', '#', '/', '*', ' ', '-', '+', ';', ',', '%']
    maxLen = 500
    maxNum = 1000000000000000000
    if type(v) == type("str"):
        for symbol in symbolList:
            v = v.replace(symbol, '')
        if len(v) >= maxLen:
            v = v[:maxLen]
        return v
    elif type(v) == type(1):
        if v >= maxNum:
            v = v % maxNum
        return v
    else:
        #print(v)
        return v

class Database:
    def __init__(self):
        self.tableDict = {
            "User" :      Table("UserList", [
                                Field("user_id", True, "INTEGER", False),
                                Field("user_name", False, "TEXT", False),
                                Field("user_password", False, "TEXT", False),
                                Field("user_phonenumber", False, "INTEGER", False),
                                Field("user_email", False, "TEXT", False),
                                Field("user_info", False, "TEXT", True),
                                Field("user_profilepath", False, "TEXT", True),
                            ]),
            "Friend" :    Table("FriendRelationList", [
                                Field("fr_id", True, "INTEGER", False),
                                Field("fr_userid", False, "TNTEGER", False, foreignKey="User"),
                                Field("fr_frid", False, "INTEGER", False, foreignKey="User"),
                            ]),
            "CollectionGood" :    Table("CollectionGoodList", [
                                Field("clg_id", True, "INTEGER", False),
                                Field("clg_userid", False, "TNTEGER", False, foreignKey="User"),
                                Field("clg_goodid", False, "INTEGER", False, foreignKey="Good"),
                                Field("clg_time", False, "INTEGER", False),
                            ]),
            "CollectionArticle" :    Table("CollectionArticleList", [
                                Field("cla_id", True, "INTEGER", False),
                                Field("cla_userid", False, "TNTEGER", False, foreignKey="User"),
                                Field("cla_articleid", False, "INTEGER", False, foreignKey="Article"),
                                Field("cla_time", False, "INTEGER", False),
                            ]),
            "AccessGood" :    Table("AccessGoodList", [
                                Field("acg_id", True, "INTEGER", False),
                                Field("acg_userid", False, "TNTEGER", False, foreignKey="User"),
                                Field("acg_goodid", False, "INTEGER", False, foreignKey="Good"),
                                Field("acg_time", False, "INTEGER", False),
                            ]),
            "AccessArticle" :    Table("AccessArticleList", [
                                Field("aca_id", True, "INTEGER", False),
                                Field("aca_userid", False, "TNTEGER", False, foreignKey="User"),
                                Field("aca_articleid", False, "INTEGER", False, foreignKey="Good"),
                                Field("aca_time", False, "INTEGER", False),
                            ]),

            "Message" :   Table("MessageList", [
                                Field("ms_id", True, "INTEGER", False),
                                Field("ms_senderid", False, "TNTEGER", False, foreignKey="User"),
                                Field("ms_receiverid", False, "INTEGER", False, foreignKey="User"),
                                Field("ms_content", False, "TEXT", False),
                                Field("ms_time", False, "INTEGER", False)
                            ]),
            "UnreadMessage" :   Table("UnreadMessageList", [
                                Field("ums_id", True, "INTEGER", False),
                                Field("ums_msid", False, "INTEGER", False, foreignKey="Message"),
                                Field("ums_receiverid", False, "INTEGER", False, foreignKey="User")
                            ]),
            
            "Likes" :   Table("LikesList", [
                                Field("lk_id", True, "INTEGER", False),
                                Field("lk_senderid", False, "TNTEGER", False, foreignKey="User"),
                                Field("lk_targetid", False, "INTEGER", False),
                                Field("lk_type", False, "TEXT", False),      #= Comment Reply Article
                            ]),
            "UnreadLikes" :   Table("UnreadLikesList", [
                                Field("ulk_id", True, "INTEGER", False),
                                Field("ulk_lkid", False, "INTEGER", False, foreignKey="Likes"),
                                Field("ulk_receiverid", False, "INTEGER", False, foreignKey="User")
                            ]),

            "Reply" :   Table("ReplyList", [
                                Field("rp_id", True, "INTEGER", False),
                                Field("rp_senderid", False, "TNTEGER", False, foreignKey="User"),
                                Field("rp_targetid", False, "INTEGER", False),
                                Field("rp_type", False, "TEXT", False),     #= Comment Reply
                                Field("rp_content", False, "TEXT", False),
                                Field("rp_time", False, "INTEGER", False)
                            ]),
            "UnreadReply" :   Table("UnreadReplyList", [
                                Field("urp_id", True, "INTEGER", False),
                                Field("urp_rpid", False, "INTEGER", False, foreignKey="Reply"),
                                Field("urp_receiverid", False, "INTEGER", False, foreignKey="User")
                            ]),                

            "Comment" :    Table("CommentList", [
                                Field("cm_id", True, "INTEGER", False),
                                Field("cm_articleid", False, "TNTEGER", False, foreignKey="Article"),
                                Field("cm_goodid", False, "TNTEGER", False, foreignKey="Good"),
                                Field("cm_publisherid", False, "TNTEGER", False, foreignKey="User"),
                                Field("cm_content", False, "TEXT", False),
                                Field("cm_time", False, "TNTEGER", False),
                            ]),
            "UnreadComment" :   Table("UnreadCommentList", [
                                Field("ucm_id", True, "INTEGER", False),
                                Field("ucm_cmid", False, "INTEGER", False, foreignKey="Comment"),
                                Field("ucm_receiverid", False, "INTEGER", False, foreignKey="User")
                            ]),     
            

            "Good" :      Table("GoodList", [
                                Field("good_id", True, "INTEGER", False),
                                Field("good_name", False, "TEXT", False),
                                Field("good_price", False, "REAL", False),
                                Field("good_type", False, "TEXT", False),
                                Field("good_info", False, "TEXT", True),
                                Field("good_imgpath", False, "TEXT", True)
                            ]),
            "KeywordGood" :    Table("KeywordGoodList", [
                                Field("kg_id", True, "INTEGER", False),
                                Field("kg_keyword", False, "TEXT", False),
                                Field("kg_goodid", False, "INTEGER", False, foreignKey="Good"),
                            ]),
            "Article" :    Table("ArticleList", [
                                Field("ar_id", True, "INTEGER", False),
                                Field("ar_publisherid", False, "TNTEGER", False, foreignKey="User"),
                                Field("ar_name", False, "TEXT", False),
                                Field("ar_content", False, "TEXT", False),
                            ]),
            "ArticleGood" : Table("ArticleGoodList", [
                                Field("ag_id", True, "INTEGER", False),
                                Field("ag_articleid", False, "TNTEGER", False, foreignKey="Article"),
                                Field("ag_goodid", False, "INTEGER", False, foreignKey="Good"),
                            ]),
            "ArticleKeyword" : Table("ArticleKeywordList", [
                                Field("ak_id", True, "INTEGER", False),
                                Field("ak_articleid", False, "TNTEGER", False, foreignKey="Article"),
                                Field("ak_keyword", False, "TEXT", False),
                            ])
        }
        self.connected = False
    def connect(self):
        if not self.connected:
            self.conn = sqlite3.connect('CYW.db')
            self.cursor = self.conn.cursor()        
        connected = True
    def build(self):
        os.system('rm CYW.db')
        self.connect()
        for table in self.tableDict.values():
            command = 'CREATE TABLE ' + table.name + '(\n'
            for field in table.fieldList:
                fieldStr = '    '
                fieldStr += field.name + " "
                fieldStr += field.dataType + " "
                if field.isKey:
                    fieldStr += "PRIMARY KEY AUTOINCREMENT "
                    #fieldStr += "PRIMARY KEY "
                if not field.canbeNull:
                    fieldStr += "NOT NULL "
                fieldStr += ",\n"
                command += fieldStr
            command = command[:-2]
            command += '\n);'
            #print(command)
            self.cursor.execute(command)
            self.conn.commit()
    def load_goods(self, fileList = ['../jdspider/pL.json']):
        import json
        for dataFile in fileList:
            goodList = json.load(open(dataFile, "r"))

            for goodDct in goodList:
                name = goodDct['name']
                price = goodDct['price']
                info = goodDct['info']
                tp = goodDct['type']
                imgpath = goodDct['imgpath']

                infoStr = ""
                for k, v in info.items():
                    infoStr += k + "：" + v + '，'
                infoStr = infoStr[: -1]

                #name = name.replace('\'', '').replace('\"', '')
                #infoStr = infoStr.replace('\'', '').replace('\"', '')

                print(name, price, infoStr, tp, imgpath)
                self.insert("Good", [name, price, tp, infoStr, imgpath])
    def load_goods_keyword(self, goodsKeyword = None):
        assert(goodsKeyword != None)
        for id, kwrdLst in goodsKeyword:
            print(id, kwrdLst)
            for kwrd in kwrdLst:
                self.insert('KeywordGood', [kwrd, id])
    def insert(self, tableName, valueList):
        assert(type(valueList) == type([]))
        table = self.tableDict[tableName]
        command = "INSERT INTO " + table.name + "("
        
        for field in table.fieldList:
            command += field.name + ","
        command = command[:-1]
        command += ")\nVALUES (NULL,"
        for i, value in enumerate(valueList):
            #filt user provided data
            value = filtV(value)
            if table.fieldList[i + 1].dataType == "TEXT":
                command += "\'"  + value + "\',"
            else:
                command += str(value) + ","
        command = command[:-1] + ");"
        #print(command)
        self.cursor.execute(command)
        self.conn.commit()
    def query(self, tableName, conditionDict, fieldList):
        assert(type(conditionDict) == type({}))
        assert(type(fieldList) == type([]))
        table = self.tableDict[tableName]
        command = "SELECT "
        if len(fieldList) != 0:
            for field in fieldList:
                field = filtV(field)
                command += field + ","
            command = command[:-1]
        else:
            command += "*"
        command += " FROM " + table.name

        if len(conditionDict.items()) != 0:
            command += " WHERE "
            for field, value in conditionDict.items():
                field = filtV(field)
                value = filtV(value)
                
                command += field + "="
                if table.name2field[field].dataType == "TEXT":
                    command += "\'" + value + "\'"
                else:
                    command += str(value)
                command += " AND "
            command = command[:-5] + ";"
        else:
            command += ";"
        #print(command)
        self.cursor.execute(command)
        self.conn.commit()
        res = []
        for row in self.cursor:
            dct = {}
            for i, field in enumerate(fieldList):
                dct[field] = row[i]
            res.append(dct)
        return res
    def modify(self, tableName, conditionDict, modificationPair):
        assert(type(conditionDict) == type({}))
        table = self.tableDict[tableName]
        command = "UPDATE " + table.name + " set "
        field, value = modificationPair
        field = filtV(field)
        value = filtV(value)
        
        if table.name2field[field].dataType == "TEXT":
            command += field + "=" + "\'" + value + "\'"
        else:
            command += field + "=" + str(value)
        command += " WHERE "
        for field, value in conditionDict.items():
            field = filtV(field)
            value = filtV(value)
            command += field + "="
            if table.name2field[field].dataType == "TEXT":
                command += "\'" + value + "\'"
            else:
                command += str(value)
            command += " AND "
        command = command[:-5] + ";"
        #print(command)
        self.cursor.execute(command)
        self.conn.commit()
    def remove(self, tableName, conditionDict):
        assert(type(conditionDict) == type({}))
        table = self.tableDict[tableName]
        command = "DELETE FROM " + table.name + " WHERE "
        for field, value in conditionDict.items():
            field = filtV(field)
            value = filtV(value)
            command += field + "="
            if table.name2field[field].dataType == "TEXT":
                command += "\'" + value + "\'"
            else:
                command += str(value)
            command += " AND "
        command = command[:-5] + ";"
        #print(command)
        self.cursor.execute(command)
        self.conn.commit()

CYWDB = Database()

if __name__ == '__main__':
    CYWDB.build()
    CYWDB.load_goods()
   
    '''CYWDB.insert("User", ["wsw", "password",111 11111111,"i am wsw"])
    #CYWDB.remove("User", {"user_name": "wsw"})
    print(CYWDB.query("User", {"user_name": "wsw"}, ["user_info"]))
    CYWDB.modify("User", {"user_name": "wsw"}, ["user_info", "new info"])
    print(CYWDB.query("User", {"user_name": "wsw"}, ["user_info"]))
    print(CYWDB.query("User", {"user_name": "wsw"}, ["user_phonenumber"]))
    print(CYWDB.query("User", {}, ["user_phonenumber"]))
'''
    ### import goods data into database

    '''import json
    dataFile = '../jdspider/pL2.json'
    goodList = json.load(open(dataFile, "r"))

    for goodDct in goodList:
        name = goodDct['name']
        price = str(goodDct['price'])
        info = goodDct['info']
        infoStr = ""
        for k, v in info.items():
            infoStr += k + ":" + v + ','
        infoStr = infoStr[: -1]

        name = name.replace('\'', '').replace('\"', '')
        infoStr = infoStr.replace('\'', '').replace('\"', '')

        print(name, price, infoStr)
        CYWDB.insert("Good", [name, price, infoStr])
'''