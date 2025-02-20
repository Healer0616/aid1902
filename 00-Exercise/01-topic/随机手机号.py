# -*- coding: utf-8 -*- 
# @Time    : 2021/1/19 上午11:49
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : 0.py
# @Software: PyCharm


import random


class PhoneNOGenerator:
    # 随机生成手机号码

    def phoneNORandomGenerator(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


if __name__ == '__main__':
    pg = PhoneNOGenerator()
    print(pg.phoneNORandomGenerator())
