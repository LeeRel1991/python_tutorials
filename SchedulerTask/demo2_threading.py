#!/usr/bin/env python
# encoding: utf-8


# -------------------------------------------------------
# version: v0.1
# author: lirui
# license: Apache Licence
# project: 
# function:
# file: demo2_threading.py
# time: 2017/11/24 0024 8:32
# -------------------------------------------------------

from threading import Timer
import time

def func(msg, starttime):
    print (u'程序启动时刻：', starttime, '当前时刻：', time.time(), '消息内容 --> %s' % (msg))

# 下面的两个语句和上面的 scheduler 效果一样的
Timer(5, func, ('hello', time.time())).start()
Timer(3, func, ('world', time.time())).start()

count = 0
def loopfunc(msg,starttime):
    global count
    print (u'启动时刻：', starttime, ' 当前时刻：', time.time(), '消息 --> %s' % (msg))
    count += 1
    if count < 3:
        Timer(3, loopfunc, ('world %d' % (count), time.time())).start()

Timer(3, loopfunc, ('world %d' % (count), time.time())).start()