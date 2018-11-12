#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: r.li
@license: Apache Licence 
@contact: r.li@bmi-tech.com
@site: 
@software: PyCharm
@file: use_decorator.py
@time: 18-7-4 下午7:26
@brief： 装饰器
"""


class Foo(object):
    def __init__(self, name):
        self.name = name
        print ("name ", self.name)

    def __call__(self, func):
        def _call(*args, **kw):
            print ('class decorator runing')
            print ("param ", args, kw)
            a = func(*args, **kw)

            print ("func excu result  ", a)
            return a

        return _call


class Bar(object):
    @Foo("Foo1")
    def bar(self, test, ids):
        print ('bar')
        print ('test = ', test)
        print('ids= ', ids )

        return "finished"

def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug
def say(something):
    print "hello {}!".format(something)


def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@logging(level='INFO')
def speak(something):
    print "say {}!".format(something)

# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print "do {}...".format(something)

if __name__ == '__main__':
    # a = Bar().bar('aa', 'ids')
    # print a

    say("hello world")
    speak("speak")
    do("do ")
