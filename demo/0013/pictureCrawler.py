#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# edit by yanghui
import urllib

from urllib import request

import re


class pictureCrawler(object):
    def __init__(self):
        pass

    def openUrl(self, url):
        req = request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
        with request.urlopen(req) as f:
            return f.read().decode('utf-8')

    def imgUrlArr(self, data):
        print(data)
        re_Imageurl = re.compile(r'src="(http://imgsrc.baidu.com/forum/.*?)"')
        return re_Imageurl.findall(data)


if __name__ == '__main__':
    pic = pictureCrawler()
    fdata = pic.openUrl('http://tieba.baidu.com/p/2166231880')
    farr = pic.imgUrlArr(fdata)
    print(farr)
