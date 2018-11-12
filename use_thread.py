#!/usr/bin/env python
# encoding: utf-8


# -------------------------------------------------------
# version: v0.1
# author: lirui
# license: Apache Licence
# project: learning
# function:
# file: use_thread
# time: 2/23/18 5:58 PM
# -------------------------------------------------------

import threading
import random
import time


def use_event():
    """
    Event实现与Condition类似的功能，不过比Condition简单一点。
    它通过维护内部的标识符来实现线程间的同步问题。（threading.Event和.NET中的System.Threading.ManualResetEvent类实现同样的功能。）
    事件机制是线程间通信机制的一种, Event对象实现了简单的线程通信机制,它提供了设置信号,清除信号,等待等用于实现线程间的通信。
    通俗点理解就如,跑步比赛的时候裁判是一个线程,各个运动员是是不同的线程,各个运动员(线程)都在等待裁判的枪声(event)才开始跑一样
    :return: 
    """
    event = threading.Event()

    def chiHuoGuo(name):
        # 等待事件，进入等待阻塞状态
        print('%s 已经启动' % threading.currentThread().getName())
        print('小伙伴 %s 已经进入就餐状态！' % name)
        time.sleep(1)
        event.wait()
        # 收到事件后进入运行状态
        print('%s 收到通知了.' % threading.currentThread().getName())
        print('%s 小伙伴 %s 开始吃咯！' % (time.time(), name))

    class myThread(threading.Thread):  # 继承父类threading.Thread
        def __init__(self, name):
            """重写threading.Thread初始化内容"""
            threading.Thread.__init__(self)

            self.people = name

        def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
            """重写run方法"""

            chiHuoGuo(self.people)  # 执行任务
            print("qq交流群：226296743")
            print("结束线程: %s\n" % threading.currentThread().getName())
            time.sleep(2)

    # 设置线程组
    threads = []
    # 创建新线程
    thread1 = myThread("a")
    thread2 = myThread("b")
    thread3 = myThread("c")

    # 添加到线程组
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)

    # 开启线程
    for thread in threads:
        thread.start()

    time.sleep(5)
    # 发送事件通知
    print('\n集合完毕，人员到齐了，开吃咯！\n')
    event.set()


def use_condition():
    """
    可以把Condiftion理解为一把高级的琐，它提供了比Lock, RLock更高级的功能，允许我们能够控制复杂的线程同步问题。
    threadiong.Condition在内部维护一个琐对象（默认是RLock），可以在创建Condigtion对象的时候把琐对象作为参数传入。
    使用Condition对象可以在某些事件触发或者达到特定的条件后才处理数据，
    Condition除了具有Lock对象的acquire方法和release方法外，还有wait方法、notify方法、notifyAll方法等用于条件处理。
    :return: 
    """
    L = []

    class boy(threading.Thread):
        def __init__(self, cond, name='A boy'):
            threading.Thread.__init__(self)
            self.cond = cond
            self.name = name

        def run(self):
            time.sleep(1)
            '''boy start conversation, make sure  
               the girl thread stared before send notify'''
            self.cond.acquire()
            print(self.name + ':Hello pretty~,I miss you\n')
            self.cond.notify()
            self.cond.wait()
            print(self.name + ':like moth missing fire\n')
            self.cond.notify()
            self.cond.wait()
            print(self.name + ':and I bought a gift for you in the list L\n')
            L.append('channel5')
            self.cond.notify()
            self.cond.release()

    class girl(threading.Thread):
        def __init__(self, cond, name='A girl'):
            threading.Thread.__init__(self)
            self.cond = cond
            self.name = name

        def run(self):
            self.cond.acquire()
            self.cond.wait()
            print(self.name + ':Really, show me how much~\n')
            self.cond.notify()
            self.cond.wait()
            print(self.name + ':you\'re so sweet~')
            self.cond.notify()
            self.cond.wait()
            print(self.name + ':wow~~, that\'s ' + L.pop() + '---the one I dreamed for so long, I love you')
            self.cond.release()

    cond = threading.Condition()
    husband = boy(cond, 'Aidan')
    wife = girl(cond, 'PPP')
    husband.start()
    wife.start()
    # husband.start()
    husband.join()  # wait untill these two threads end
    wife.join()
    print('end converdarion\n')


def use_lock():
    # lock = threading.Lock()  # Lock对象
    # lock.acquire()
    # print("acquired")
    # lock.acquire()  # 产生了死琐。
    # print("acquired two")
    # lock.release()
    # lock.release()

    """这两种琐的主要区别是：RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。
    注意：如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。"""
    rLock = threading.RLock()  # RLock对象
    rLock.acquire()
    print("acquired")
    rLock.acquire()  # 在同一线程内，程序不会堵塞。
    print("acquired two")
    rLock.release()
    rLock.release()


if __name__ == '__main__':
    # use_event()
    # use_condition()
    use_lock()