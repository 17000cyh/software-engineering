from dbutil import *

import unittest

import numpy as np
class TestCaseGenerator:
    def __init__(self):
        self.tableCnt = {}
    def randStr(self):
        l = np.random.randint(1, 16)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        lst = np.random.choice(letters, l)
        return ''.join(list(lst))
    def randInt(self):
        return np.random.randint(low=1, high=1000)
    def randChoice(self, lst, num):
        idxs = range(len(lst))
        cidxs = list(np.random.choice(idxs, num, replace = False))
        return [lst[idx] for idx in cidxs]
    def randField(self, field):
        if field.dataType == "TEXT":
            return self.randStr()
        else:
            return str(self.randInt())
    def randItem(self, table):
        valueList = []
        for field in table.fieldList:
            valueList.append(self.randField(field))
        if table.name not in self.tableCnt:
            self.tableCnt[table.name] = 0
        self.tableCnt[table.name] += 1
        valueList [0] = self.tableCnt[table.name]
        return valueList
    def generateItemList(self, numItem):
        itemList = []
        tables = list(CYWDB.tableDict.keys())
        numTables = len(tables)
        for i in range(numItem):
            tableName = tables[np.random.randint(numTables)]
            table = CYWDB.tableDict[tableName]
            item = self.randItem(table)
            itemList.append((tableName, item))
        return itemList
tg = TestCaseGenerator()
itemList = tg.generateItemList(20)

class TestDBMethods(unittest.TestCase):
    def test_insert_query(self):
        CYWDB.connect()
        CYWDB.build()
        #for item in itemList:
        #    print(item)
        for tableName, itemValues in itemList:
            CYWDB.insert(tableName, itemValues[1:])
        for tableName, itemValues in itemList:
            table = CYWDB.tableDict[tableName]
            for i in range(len(table.fieldList)):
                field = table.fieldList[i]
                res = CYWDB.query(tableName, {field.name: itemValues[i]}, [])
                self.assertTrue(len(res) != 0)
    def test_insert_remove_query(self):
        CYWDB.connect()
        CYWDB.build()

        removeList = tg.randChoice(itemList, np.random.randint(low=1, high=len(itemList) + 1) // 2)
        reserveList = [item for item in itemList if item not in removeList]
        
        for tableName, itemValues in itemList:
            CYWDB.insert(tableName, itemValues[1:])
        for tableName, itemValues in removeList:
            table = CYWDB.tableDict[tableName]
            CYWDB.remove(tableName, {table.fieldList[0].name: itemValues[0]})

        for tableName, itemValues in removeList:
            table = CYWDB.tableDict[tableName]
            res = CYWDB.query(tableName, {table.fieldList[0].name: itemValues[0]}, [])
            #print("res:", res)
            self.assertTrue(len(res) == 0)
        for tableName, itemValues in reserveList:
            table = CYWDB.tableDict[tableName]
            res = CYWDB.query(tableName, {table.fieldList[0].name: itemValues[0]}, [])
            self.assertTrue(len(res) != 0)
    def test_insert_modify_query(self):
        CYWDB.connect()
        CYWDB.build()

        modifyList = tg.randChoice(itemList, np.random.randint(low=1, high=len(itemList) + 1) // 2)
        modifyField = []
        for tableName, itemValues in modifyList:
            table = CYWDB.tableDict[tableName]
            fieldList = table.fieldList[1:]
            field = tg.randChoice(fieldList, 1)[0]
            if field.dataType == "TEXT":
                modifyValue = tg.randStr()
            else:
                modifyValue = tg.randInt()
            modifyField.append((field.name, modifyValue))
        
        '''for item in modifyList:
            print(item)
        for field in modifyField:
            print(field)'''

        for tableName, itemValues in itemList:
            CYWDB.insert(tableName, itemValues[1:])
        for i in range(len(modifyList)):
            tableName, itemValues = modifyList[i]
            fieldName, modifyValue = modifyField[i]
            table = CYWDB.tableDict[tableName]
            CYWDB.modify(tableName, {table.fieldList[0].name: itemValues[0]}, (fieldName, modifyValue))

        for i in range(len(modifyList)):
            tableName, itemValues = modifyList[i]
            fieldName, modifyValue = modifyField[i]
            table = CYWDB.tableDict[tableName]
            res = CYWDB.query(tableName, {table.fieldList[0].name: itemValues[0]}, [fieldName])
            self.assertTrue(len(res) == 1)
            #print(res[0][fieldName], modifyValue)
            #print(res[0])
            self.assertTrue(res[0][fieldName] == modifyValue)

if __name__ == '__main__':
    unittest.main()
