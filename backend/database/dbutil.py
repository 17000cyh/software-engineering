import sqlite3
import os

class Field:
    def __init__(self, name, isKey, dataType, canbeNull):
        self.name = name
        self.isKey = isKey
        self.dataType = dataType
        self.canbeNull = canbeNull
class Table:
    def __init__(self, name, fieldList):
        self.name = name
        self.fieldList = fieldList
        self.name2field = {}
        for field in fieldList:
            self.name2field[field.name] = field

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
                            ]),
            "Friend" :    Table("FriendRelationList", [
                                Field("fr_id", True, "INTEGER", False),
                                Field("fr_userid", False, "TNTEGER", False),
                                Field("fr_frid", False, "INTEGER", False),
                            ]),
            "CollectionGood" :    Table("CollectionGoodList", [
                                Field("clg_id", True, "INTEGER", False),
                                Field("clg_userid", False, "TNTEGER", False),
                                Field("clg_goodid", False, "INTEGER", False),
                                Field("clg_time", False, "INTEGER", False),
                            ]),
            "CollectionArticle" :    Table("CollectionArticleList", [
                                Field("cla_id", True, "INTEGER", False),
                                Field("cla_userid", False, "TNTEGER", False),
                                Field("cla_articleid", False, "INTEGER", False),
                                Field("cla_time", False, "INTEGER", False),
                            ]),
            "AccessGood" :    Table("AccessGoodList", [
                                Field("acg_id", True, "INTEGER", False),
                                Field("acg_userid", False, "TNTEGER", False),
                                Field("acg_goodid", False, "INTEGER", False),
                                Field("acg_time", False, "INTEGER", False),
                            ]),
            "AccessArticle" :    Table("AccessArticleList", [
                                Field("aca_id", True, "INTEGER", False),
                                Field("aca_userid", False, "TNTEGER", False),
                                Field("aca_articleid", False, "INTEGER", False),
                                Field("aca_time", False, "INTEGER", False),
                            ]),
            "Message" :   Table("MessageList", [
                                Field("ms_id", True, "INTEGER", False),
                                Field("ms_senderid", False, "TNTEGER", False),
                                Field("ms_receiverid", False, "INTEGER", False),
                                Field("ms_content", False, "TEXT", False)
                            ]),
            "UnreadMessage" :   Table("UnreadMessageList", [
                                Field("ums_id", True, "INTEGER", False),
                                Field("ums_senderid", False, "TNTEGER", False),
                                Field("ums_receiverid", False, "INTEGER", False),
                                Field("ums_msid", False, "INTEGER", False)
                            ]),
            "UnreadLikes" :   Table("UnreadLikesList", [
                                Field("ulk_id", True, "INTEGER", False),
                                Field("ulk_senderid", False, "TNTEGER", False),
                                Field("ulk_receiverid", False, "INTEGER", False)
                            ]),
            "UnreadReply" :   Table("UnreadReplyList", [
                                Field("ure_id", True, "INTEGER", False),
                                Field("ure_senderid", False, "TNTEGER", False),
                                Field("ure_receiverid", False, "INTEGER", False),
                                Field("ure_msid", False, "INTEGER", False)
                            ]),

            "Good" :      Table("GoodList", [
                                Field("good_id", True, "INTEGER", False),
                                Field("good_name", False, "TEXT", False),
                                Field("good_price", False, "REAL", False),
                                Field("good_type", False, "TEXT", False),
                                Field("good_info", False, "TEXT", True),
                            ]),
            "KeywordGood" :    Table("KeywordGoodList", [
                                Field("kg_id", True, "INTEGER", False),
                                Field("kg_keyword", False, "TEXT", False),
                                Field("kg_goodid", False, "INTEGER", False),
                            ]),
            "Article" :    Table("ArticleList", [
                                Field("ar_id", True, "INTEGER", False),
                                Field("ar_publisherid", False, "TNTEGER", False),
                                Field("ar_content", False, "TEXT", False),
                            ]),
            "Comment" :    Table("CommentList", [
                                Field("cm_id", True, "INTEGER", False),
                                Field("cm_articleid", False, "TNTEGER", False),
                                Field("cm_publisherid", False, "TNTEGER", False),
                                Field("cm_content", False, "TEXT", False),
                            ]),
            "ArticleGood" : Table("ArticleGoodList", [
                                Field("ag_id", True, "INTEGER", False),
                                Field("ag_articleid", False, "TNTEGER", False),
                                Field("ag_goodid", False, "INTEGER", False),
                            ]),
            "ArticleKeyword" : Table("ArticleKeywordList", [
                                Field("ak_id", True, "INTEGER", False),
                                Field("ak_articleid", False, "TNTEGER", False),
                                Field("ak_keyword", False, "TEXT", False),
                            ])
        }

        os.system('rm CYW.db')

        self.conn = sqlite3.connect('CYW.db')
        self.cursor = self.conn.cursor()

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
    def insert(self, tableName, valueList):
        table = self.tableDict[tableName]
        command = "INSERT INTO " + table.name + "("
        
        for field in table.fieldList:
            command += field.name + ","
        command = command[:-1]
        command += ")\nVALUES (NULL,"
        for i, value in enumerate(valueList):
            if table.fieldList[i + 1].dataType == "TEXT":
                command += "\'"  + value + "\',"
            else:
                command += str(value) + ","
        command = command[:-1] + ");"
        #print(command)
        self.cursor.execute(command)
        self.conn.commit()
    def query(self, tableName, conditionDict, fieldList):
        table = self.tableDict[tableName]
        command = "SELECT "
        for field in fieldList:
            command += field + ","
        command = command[:-1]
        command += " FROM " + table.name

        if len(conditionDict.items()) != 0:
            command += " WHERE "
            for field, value in conditionDict.items():
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
        table = self.tableDict[tableName]
        command = "UPDATE " + table.name + " set "
        field, value = modificationPair
        
        if table.name2field[field].dataType == "TEXT":
            command += field + "=" + "\'" + value + "\'"
        else:
            command += field + "=" + value
        command += " WHERE "
        for field, value in conditionDict.items():
            command += field + "="
            if table.name2field[field].dataType == "TEXT":
                command += "\'" + value + "\'"
            else:
                command += value
            command += " AND "
        command = command[:-5] + ";"
        #print(command)
        self.cursor.execute(command)
        self.conn.commit()
    def remove(self, tableName, conditionDict):
        table = self.tableDict[tableName]
        command = "DELETE FROM " + table.name + " WHERE "
        for field, value in conditionDict.items():
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