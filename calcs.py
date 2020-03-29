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
f = open('data/test.txt', 'r')
jsonData = json.load(f)
f.close()
# tableData0=contents
d = jsonData
#print(d)
am=0
for key in jsonData:
    print(key['amount'])  # titleのみ参照
    if not key['amount'] == "":
        am=am+int(key['amount'])
print (am)