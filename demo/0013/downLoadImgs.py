#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# edit by yanghui
import os
import urllib

from urllib import request
from  urllib.request import urlopen

import re


def downloadImage(pic_url):
    dirct = '0013'
    try:
        if not os.path.exists(dirct):  # 创建存放目录
            os.mkdir(dirct)
    except:
        print('Failed to create directory in %s' % dirct)
        exit()
    for i in pic_url:
        data = urllib.request.urlopen(i).read()
        i = re.split('/', i)[-1]
        print(i)
        path = dirct + '/' + i
        f = open(path, 'wb')
        f.write(data)
        f.close()
    print('Done !')


def Imageurl(data):
    re_Imageurl = re.compile(r'src="(http://imgsrc.baidu.com/forum/.*?)"')
    datao = re_Imageurl.findall(data)
    downloadImage(datao)


def open_url(url):
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    with request.urlopen(req) as f:
        Imageurl(f.read().decode('utf-8'))


url = 'http://tieba.baidu.com/p/2166231880'
open_url(url)
