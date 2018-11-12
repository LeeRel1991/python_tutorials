#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: r.li
@license: Apache Licence 
@contact: r.li@bmi-tech.com
@site: 
@software: PyCharm
@file: narcissistic_number.py
@time: 18-10-15 下午9:58
@brief： 
"""

import sys


def shuixianhua(min_v, max_v):
    re = []
    for x in range(min_v, max_v):
        last_one = x % 10
        mid_one = (x // 10) % 10
        first_one = x // 100

        # print(first_one, mid_one, last_one)
        if x == pow(last_one, 3) + pow(mid_one, 3) + pow(first_one, 3):
            re.append(str(x))
    return re


def main(data):
    for line in data:
        min_v, max_v = line.split()
        min_v = int(min_v)
        max_v = int(max_v)
        # print(min_v, max_v)
        re = shuixianhua(min_v, max_v)

        if len(re):
            print(" ".join(re))
        else:
            print("no")


main(['100 120\n', '300 380'])


if __name__ == '__main__':
    pass