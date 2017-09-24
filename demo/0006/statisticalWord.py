#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# edit by yanghui
import glob
import os

import re
from collections import OrderedDict


def get_num(ke_word, filename):
    f = open(filename, 'r', encoding='utf-8').read()
    re_zhengze = re.compile(r'[\s\,\;\.\n]{1}' + ke_word + r'[\s\,\;\.\n]{1}')
    numbers = re_zhengze.findall(f)
    return len(numbers)


def artivale_analysis(dirs):
    article = glob.glob(r'*.txt')
    dictdata = OrderedDict()
    for m in article:
        doc =open(m, 'r', encoding='utf-8').read()
        doc = re.findall(r'[\w\-\_\.\']+', doc)
        doc = list(map(lambda x: x.strip('.'), doc))
        for n in doc:
            dictdata[n] = get_num(n, m)

        a = OrderedDict(sorted(dictdata.items(), key=lambda x: x[1], reverse=True))
        print(a)
        print('在 %s 中出现次数最多的单词是 ' % m)
        for c in a:
            print(c + ': %s 次' % a[c])
            break
    return False


if __name__ == '__main__':
    file = '.'
    artivale_analysis(file)
    print(os.path)
