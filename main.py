# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import signal
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from collections import deque
import datetime
import threading
import time
import json
#from lib import functions
#from lib import gl
app = QtWidgets.QApplication([])
 
win = uic.loadUi("ui/hotei.ui") #specify the location of your .ui file
view2 = uic.loadUi("ui/view2.ui")
win.resize(1024,750)
win.show()


#functions.setTree(win)
#functions.setTree01(win)
#functions.setTree02(win)
#functions.setTable(win)
#t1 = threading.Thread(target=functions.hello1(win))
#t1 = threading.Timer(1, functions.hello1(win))
#t1.start()

def setTable(win):
    headers = ["内容", "重要度", "優先度"]
    # ファイルをオープンする
    #test_data = open("data/tabledata.json", "r")
    # すべての内容を読み込む
    #contents = test_data.read()
    # ファイルをクローズする
    #test_data.close()
    f = open('data/tabledata.json', 'r')
    jsonData = json.load(f)
    f.close()
    #tableData0=contents
    tableData0=jsonData
    model = MyTableModel(tableData0,headers)
    win.tableView.setModel(model)
    header = win.tableView.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    win.tableView.resizeColumnToContents(1)
    win.tableView.resizeColumnToContents(2)

def setTable2(win):
    headers = ["内容", "重要度", "優先度"]
    # ファイルをオープンする
    #test_data = open("data/tabledata.json", "r")
    # すべての内容を読み込む
    #contents = test_data.read()
    # ファイルをクローズする
    #test_data.close()
    f = open('data/shisan.json', 'r')
    jsonData = json.load(f)
    f.close()
    #tableData0=contents
    tableData0=jsonData
    model = MyTableModel(tableData0,headers)
    win.tableView_2.setModel(model)
    header = win.tableView_2.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    win.tableView_2.resizeColumnToContents(1)
    win.tableView_2.resizeColumnToContents(2)

def setTable3(win):
    headers = ["内容", "重要度", "優先度"]
    # ファイルをオープンする
    #test_data = open("data/tabledata.json", "r")
    # すべての内容を読み込む
    #contents = test_data.read()
    # ファイルをクローズする
    #test_data.close()
    f = open('data/nittei.json', 'r')
    jsonData = json.load(f)
    f.close()
    #tableData0=contents
    tableData0=jsonData
    model = MyTableModel(tableData0,headers)
    win.tableView_4.setModel(model)
    header = win.tableView_4.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    win.tableView_4.resizeColumnToContents(1)
    win.tableView_4.resizeColumnToContents(2)

def setTable4(win):
    headers = ["内容", "重要度", "優先度"]
    # ファイルをオープンする
    # test_data = open("data/tabledata.json", "r")
    # すべての内容を読み込む
    # contents = test_data.read()
    # ファイルをクローズする
    # test_data.close()
    f = open('data/renrakutyou.json', 'r')
    jsonData = json.load(f)
    f.close()
    # tableData0=contents
    tableData0 = jsonData
    model = MyTableModel(tableData0, headers)
    win.tableView_3.setModel(model)
    header = win.tableView_3.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    win.tableView_3.resizeColumnToContents(1)
    win.tableView_3.resizeColumnToContents(2)

class MyTableModel(QAbstractTableModel):
    def __init__(self, list, headers=[], parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.list = list
        self.headers = headers

    def rowCount(self, parent):
        return len(self.list)

    def columnCount(self, parent):
        return len(self.list[0])

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role):
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            return self.list[row][column]

        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.list[row][column]
            return value

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            self.list[row][column] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:

            if orientation == Qt.Horizontal:

                if section < len(self.headers):
                    return self.headers[section]
                else:
                    return "not implemented"
            else:
                num = section + 1
                return "No. %d" % num


def scheduler():
    t = threading.Timer(1, scheduler)
    t.start()
    #print(time.time())
    hello1(win)


def hello1(win):
    dayarr = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    now = datetime.datetime.now()
    str1 = now.strftime("%Y/%m/%d")
    str2 = now.strftime("%H:%M:%S")
    str3 = dayarr[now.weekday()]
    # win.label.setText("Hello Japan.")
    #win.label_2.setText(str1 + str3 + str2)
    # hello("hello1")

    # 目標時刻
    #f = open('data/targetdate.json', 'r')
    #jsonData = json.load(f)
    #f.close()
    #dt1 = datetime.datetime(int(jsonData["year"]), int(jsonData["month"]), int(jsonData["day"]), int(jsonData["hour"]))
    #win.label.setText(jsonData["mes"])
    # 日カウント
    #tdt = dt1 - now
    # 時間カウント
    #str4 = str(tdt)
    win.label_16.setText(str2)
    win.label_17.setText(str1+str3)

def show_view2():
    view2.show()

win.pushButton_4.clicked.connect(show_view2)

setTable(win)
setTable2(win)
setTable3(win)
setTable4(win)
#table.show()
t = threading.Thread(target = scheduler)
t.start()
#t.stopping.set()  # 終了中フラグを立てる
t.join()   # スレッドが終了するまで待つ
#gl.main()
sys.exit(app.exec())
