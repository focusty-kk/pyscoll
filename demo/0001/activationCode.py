#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import random, string, uuid

forSelect = string.ascii_letters + string.digits


def generate(count, length):
    for x in range(count):
        re = ""
        for y in range(length):
            re += random.choice(forSelect)
        print(re)


if __name__ == "__main__":
    generate(200, 20)
