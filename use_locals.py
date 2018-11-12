#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: r.li
@license: Apache Licence 
@contact: r.li@bmi-tech.com
@site: 
@software: PyCharm
@file: use_locals.py
@time: 18-9-4 上午10:25
@brief： 
"""

def func(x, y):
    arg_a, arg_b = 'a', 'b'
    locals().setdefault("nam", "12")
    print("nam ", locals().get("nam"))
    def func_a():
        pass

    def func_b():
        pass

    def print_value():
        print(arg_a, arg_b)

    return locals()


if __name__ == '__main__':

    args = func(1, 2)
    print(type(args))
    for k, v in args.items():
        print(k, v)
