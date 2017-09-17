#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# edit by yanghui

inputWord = input('请输入！')
allWords = open(r'filtered_words.txt').readlines()

flg = False

for word in allWords:
    if word.find(inputWord) == -1:
        flg = True
        break

if flg:
    print('存在敏感词汇！')
