#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: r.li
@license: Apache Licence 
@contact: r.li@bmi-tech.com
@site: 
@software: PyCharm
@file: phone.py
@time: 18-10-11 下午9:31
@brief： 
"""
import sys

dep_char_dict = {0: "Z", 2: "W", 8: "G", 6: "X", 4: "U"}
num_char_dict = {0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE",
                 4: 'FOUR', 5: 'FIVE', 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}


def min_number(data_str):
    char_cnt = {}
    chars = set(data_str)
    for c in chars:
        char_cnt[c] = data_str.count(c)
    print(char_cnt)

    num_cnt = {}
    for i in range(10):
        num_cnt[i] = 0

    # 第一批独立字符 数字
    for d, c in dep_char_dict.items():
        if c not in char_cnt.keys():
            num_cnt[d] = 0
        else:
            num_cnt[d] = char_cnt[c]
            # print(d, c, num_cnt[d])
    num_cnt[7] = char_cnt['S'] - num_cnt[6] if 'S' in char_cnt.keys() else 0
    num_cnt[5] = char_cnt['F'] - num_cnt[4] if 'F' in char_cnt.keys() else 0
    num_cnt[3] = char_cnt['T'] - num_cnt[2] - num_cnt[8] if 'T' in char_cnt.keys() else 0
    num_cnt[1] = char_cnt['O'] - num_cnt[0] - num_cnt[4] - num_cnt[2] if 'O' in char_cnt.keys() else 0
    num_cnt[9] = int((char_cnt['N'] - num_cnt[1] - num_cnt[7]) / 2) if 'N' in char_cnt.keys() else 0
    # print(num_cnt)

    # 根据哥数字的个数从小到大
    re_str = []
    for d, c in num_cnt.items():
        re_str += [d for i in range(c)]

    # print(re_str)
    re_str2 = []
    for i, d in enumerate(re_str):
        if int(d) >= 8:
            re_str2.append(str(int(d) - 8))
        else:
            re_str2.append(str(10 + int(d) - 8))

    # print(re_str2)
    return "".join(sorted(re_str2))


def main(data):
    num = int(data[0])
    phones_list = data[1:]
    # print("input ", phones_list)
    for ph in phones_list:
        # print(ph)
        if ph.isalpha():
            print(min_number(ph))


main(sys.stdin.readlines())

if __name__ == '__main__':
    a = 'OHEIWTEGTHENRTEO'
    # a.replace()
    main(['4', 'EIGHT', 'ZEROTWOONE', "OHWETENRTEO", 'OHEIWTEGTHENRTEO'])
