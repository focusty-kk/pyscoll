#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# edit by yanghui
import os
import re, glob

from PIL import Image


class wordCount(object):
    def __init__(self):
        self.name = None

    def openImg(self, path):
        file = glob.glob(r'*.jpg')
        for x in file:
            name = os.path.join(path, x)
            im = Image.open(name)
            im.thumbnail((1136, 640))
            print(im.format, im.size, im.mode)
            im.save(name, 'jpg')
        print('Done!')


if __name__ == '__main__':
    count = wordCount()
    path = './'
    count.openImg(path)

