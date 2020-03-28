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
nnw = uic.loadUi("ui/nnw.ui")
view2 = uic.loadUi("ui/view2.ui")
hensyu = uic.loadUi("ui/hensyu.ui")
addnew = uic.loadUi("ui/addnew.ui")
sokusanki = uic.loadUi("ui/sokusanki.ui")

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
    # test_data = open("data/tabledata.json", "r")
    # すべての内容を読み込む
    # contents = test_data.read()
    # ファイルをクローズする
    # test_data.close()
    f = open('data/test2.txt', 'r')
    jsonData = json.load(f)
    f.close()
    # tableData0=contents
    d = jsonData
    print(d)
    i = 0
    j = 0
    # for i, (key, value) in enumerate(d["events"].items()):
    # set row count
    win.tableWidget_2.setRowCount(10)
    # set column count
    win.tableWidget_2.setColumnCount(4)
    win.tableWidget_2.itemDoubleClicked.connect(show_hensyu)
    # currentQTableWidgetItem.row()

    for item in d:
        # print(str(i)+":"+item["title"])
        Data = QTableWidgetItem(str(item["title"]))
        j = 0
        win.tableWidget_2.setItem(i, j, Data)

        j = 1
        Data2 = QTableWidgetItem(str(item["body"]))
        win.tableWidget_2.setItem(i, j, Data2)

        j = 2

        if not item.get('date'):
            print('NULL')
        else:
            Data2 = QTableWidgetItem(str(item["date"]))
            win.tableWidget_2.setItem(i, j, Data2)

        j = 3
        Data2 = QTableWidgetItem(str(item["amount"]))
        win.tableWidget.setItem(i, j, Data2)
        i = i + 1
    win.tableWidget_2.resizeColumnToContents(0)
    win.tableWidget_2.resizeColumnToContents(2)
'''
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
'''
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

#更新ロジック
#指定のデータ番号のデータを削除し新しいものを書き込む　配列操作で指定の番号を削除して行う
#全部書き込む

def close_nnw():
    #表示順序の変更
    #ウインドウから値を取得
    #オブジェクトの数だけ繰り返す。
    #開いたときに初期化 今日の日付にする
    #dt = self.ui.dateTimeEdit.dateTime()
    #dt_string = dt.toString(self.ui.dateTimeEdit.displayFormat())


    #nnw.dateTimeEdit.strftime()
    PATH_FILE = 'data/test2.txt'
    title = nnw.lineEdit.text()
    body = nnw.textEdit.toPlainText()
    amount = nnw.lineEdit_2.text()
    name = nnw.label_2.text()
    date=nnw.dateTimeEdit.dateTime()
    #日付形式を指定して保存
    date=date.toString("yyyy/MM/dd hh:mm:ss")

    if nnw.groupItemType.checkedId() < 0:
        strItemType = "未選択"
    else:
        strItemType = ['やりたいこと', 'ほしいもの'][nnw.groupItemType.checkedId()]

    d={}
    keys = ['title', 'body', 'amount','name','date','type']
    values = [title, body, amount,name,date,strItemType]

    d.update(zip(keys, values))
    print(d)
    #data=json.dumps(list)
    data=d
    append_json_to_file(data, PATH_FILE)
    # 検証（保存ファイルのまるごと読み込み）
    f_saved = open(PATH_FILE, "r")
    contents = f_saved.read()
    f_saved.close()
    nnw.close()
    setTable(win)
def setTable3(win):
    headers = ["内容", "重要度", "優先度"]
    # ファイルをオープンする
    # test_data = open("data/tabledata.json", "r")
    # すべての内容を読み込む
    # contents = test_data.read()
    # ファイルをクローズする
    # test_data.close()
    f = open('data/test.txt', 'r')
    jsonData = json.load(f)
    f.close()
    # tableData0=contents
    d = jsonData
    print(d)
    i = 0
    j = 0
    # for i, (key, value) in enumerate(d["events"].items()):
    # set row count
    win.tableWidget.setRowCount(10)
    # set column count
    win.tableWidget.setColumnCount(4)
    win.tableWidget.itemDoubleClicked.connect(show_hensyu)
    # currentQTableWidgetItem.row()

    for item in d:
        # print(str(i)+":"+item["title"])
        Data = QTableWidgetItem(str(item["title"]))
        j = 0
        win.tableWidget.setItem(i, j, Data)

        j = 1
        Data2 = QTableWidgetItem(str(item["body"]))
        win.tableWidget.setItem(i, j, Data2)

        j = 2

        if not item.get('date'):
            print('NULL')
        else:
            Data2 = QTableWidgetItem(str(item["date"]))
            win.tableWidget.setItem(i, j, Data2)

        j = 3
        Data2 = QTableWidgetItem(str(item["amount"]))
        win.tableWidget.setItem(i, j, Data2)
        i = i + 1
    win.tableWidget.resizeColumnToContents(2)
    win.tableWidget.resizeColumnToContents(3)
def show_hensyu(self):
    #print(self.currentQTableWidgetItem.row())
    #番目のデータ 　削除
    print(self.row())
    #ファイルを読んでデータを表示する
    f = open('data/test.txt', 'r')
    jsonData = json.load(f)
    f.close()
    #tableData0=contents
    d=jsonData
    i=0
    for item in d:
        if i==self.row():
            # print(str(i)+":"+item["title"])

            if not item.get('title'):
                print('NULL')
            else:
                s01 = str(item["title"])
                hensyu.lineEdit.setText(s01)

            if not item.get('amount'):
                print('NULL')
            else:
                s02=item["amount"]
                hensyu.lineEdit_2.setText(s02)
            if not item.get('date'):
                print('NULL')
            else:
                s03 =item["date"]
                #alarm_date = QtCore.QDateTime(s03)
                alarm_date=datetime.datetime.strptime(s03, "%Y/%m/%d %H:%M")
                # dateTimeEdit.setDate(alarm_date)
                hensyu.dateTimeEdit.setDate(alarm_date)
        i=i+1

    hensyu.show()

#        rows = [value[k] for k in keys] + [key]
#        w.insertRow(w.rowCount())
#        for j, v in enumerate(rows):
#            it = QtWidgets.QTableWidgetItem(v)
#            w.setItem(i, j, it)
# ''''''
# header = win.tableView.horizontalHeader()
# header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
# win.tableView.resizeColumnToContents(1)
# win.tableView.resizeColumnToContents(2)

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
def addnew_obj():
    #ウインドウから値を取得
    #オブジェクトの数だけ繰り返す。
    #開いたときに初期化
    PATH_FILE = 'data/test.txt'
    # for i in range(10):
    #    key  = 'key{num}'.format(num=i)
    #    data = { key: i }                    # サンプル辞書データ
    #    append_json_to_file(data, PATH_FILE) # 要素を追加
    # data={"title":"うめきちとうめこ","body":"松本さん 10日で卵を産む","amount":"8000","date":"2020/02/17 12:00"}
    title = addnew.lineEdit.text()
    body = addnew.textEdit.toPlainText()
    amount = addnew.lineEdit_2.text()
    #date = addnew.lineEdit.text()
    #data = '{"title": "'+title+'", "body": "'+body+'", "amount": "'+amount+'", "date": "2020/02/28 11:00"}'
    #data = '{title: ' + title + ', body: ' + body + ', amount: ' + amount + ', date: 2020/02/28 11:00}'
    #list='{"title": "' + title + '", "body": "' + body + '", "amount": "' + amount + '", "date": "2020/02/28 11:00"}'
    d={}
    keys = ['title', 'body', 'amount']
    values = [title, body, amount]

    d.update(zip(keys, values))
    print(d)
    #data=json.dumps(list)
    data=d
    append_json_to_file(data, PATH_FILE)
    # 検証（保存ファイルのまるごと読み込み）
    f_saved = open(PATH_FILE, "r")
    contents = f_saved.read()
    f_saved.close()
    addnew.close()
def show_addnew():
    addnew.show()
    #表のアップデート

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

def show_sokusanki():
    sokusanki.show()
def show_view2():
    view2.show()
def append_json_to_file(data: dict, path_file: str) -> bool:
    with open(path_file, 'ab+') as f:  # ファイルを開く
        f.seek(0, 2)  # ファイルの末尾（2）に移動（フォフセット0）
        if f.tell() == 0:  # ファイルが空かチェック
            f.write(json.dumps([data]).encode())  # 空の場合は JSON 配列を書き込む
            #f.write(data)
        else:
            f.seek(-1, 2)  # ファイルの末尾（2）から -1 文字移動
            f.truncate()  # 最後の文字を削除し、JSON 配列を開ける（]の削除）
            f.write(' , '.encode())  # 配列のセパレーターを書き込む
            f.write(json.dumps(data).encode())  # 辞書を JSON 形式でダンプ書き込み
            #f.write(data)
            f.write(']'.encode())  # JSON 配列を閉じる
    return f.close()  # 連続で追加する場合は都度 Open, Close しない方がいいかもimport json

import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
def stock():
    start = datetime.datetime(2012, 1, 1)
    end = datetime.datetime(2017, 12, 31)

    #f = web.DataReader('SNE', 'morningstar', start, end)
    f = web.DataReader('SNE', 'yahoo', start, end)
    print(f.head())
    #f2 = web.DataReader(['SNE', 'AAPL'], 'morningstar', start, end)
    f2 = web.DataReader(['SNE', 'AAPL'], 'yahoo', start, end)

    print(type(f2.index))
    print(f2.head())
    print(f2.tail())
    f2_u = f2.unstack(0)
    print(f2_u.head())
    f2_u['Close'].plot(title='SNE vs AAPL', grid=True)
    plt.show()
    #plt.savefig('data/dst/pandas_datareader_morningstar.png')
    #ModuleNotFoundError: No module named 'pandas_datareader'
    #(base) PS D:\06.gitrepo\hoteityou> pip install pandas-datareader
    #pip install git+https://github.com/pydata/pandas-datareader.git
def show_nnw():
    currentDate = QDateTime()
    nnw.groupItemType = QButtonGroup()
    nnw.groupItemType.addButton(nnw.radioButton, 0)
    nnw.groupItemType.addButton(nnw.radioButton_2, 1)
    nnw.dateTimeEdit.setDateTime(currentDate.currentDateTime())
    nnw.show()


setTable(win)
setTable2(win)
setTable3(win)
setTable4(win)
#table.show()
win.pushButton_4.clicked.connect(show_view2)
win.pushButton_6.clicked.connect(show_nnw)
addnew.pushButton.clicked.connect(addnew_obj)
win.pushButton_3.clicked.connect(show_addnew)
nnw.pushButton.clicked.connect(close_nnw)
win.pushButton_5.clicked.connect(stock)
win.pushButton_7.clicked.connect(show_sokusanki)
t = threading.Thread(target = scheduler)
t.start()
#t.stopping.set()  # 終了中フラグを立てる
t.join()   # スレッドが終了するまで待つ
#gl.main()
sys.exit(app.exec())
