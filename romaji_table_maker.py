#/usr/bin/env python3

# -*- coding: utf-8 -*-


DATA = './data/data.csv'
SPECIAL = './data/special.txt'

import csv
import sys

class romajiTable:
    def __init__(self):
        self.keyList = []
        self.valueList = {}

    def getKeyList(self):
        return self.keyList

    def getValueList(self):
        return self.valueList

    def getValue(self, key):
        return self.valueList[key]

    def addValue(self, key, value):
        if key in self.keyList:
            del self.keyList[self.keyList.index(key)]
            self.keyList.append(key)
            self.valueList[key] = value
        else:
            self.keyList.append(key)
            self.valueList[key] = value

    def addRomajiTable(self, filename):
        for line in open(filename):
            row = line.rstrip().split('\t')
            if len(row) == 2:
                key, value = row
                self.addValue(key, value)
                    
if __name__ == '__main__':
    # 引数指定
    argv = sys.argv
    argc = len(argv)
    
    romajiData = romajiTable()

    csvdata = []
    for line in csv.reader(open(DATA), delimiter=','):
        if len(line) == 16:
            csvdata.append(line)
            
    for i, row in enumerate(csvdata[1:], 1):
        for j, value in enumerate(row[1:], 1):
            key = '{0}{1}'.format(csvdata[i][0], csvdata[0][j])
            if value:
                romajiData.addValue(key, value)

    romajiData.addRomajiTable(SPECIAL)

    for uniqueFile in argv[1:]:
        romajiData.addRomajiTable(uniqueFile)
    
    for key in romajiData.getKeyList():
        print("{0}\t{1}".format(key, romajiData.getValue(key)))
