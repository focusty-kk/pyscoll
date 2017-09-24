#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# edit by yanghui
#tips: ⌃⌥O 优化import

import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter


class verificationCode(object):
    def __init__(self):
        self.font = 'SFNSTextItalic'
        self.height = 60
        self.width = 60 * 4
        self.image = None
        self.draw = None
        self.imagefont = None

    def buidImg(self):
        self.image = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        return self.image

    def buildImgFont(self):
        return ImageFont.truetype(self.font, 36)

    def drawImg(self):
        self.draw = ImageDraw.Draw(self.image)

    def fillImg(self):
        for x in range(self.width):
            for y in range(self.height):
                self.draw.point((x, y), fill=self.rondomColor())

    def rondomColor(self):
        return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

    def rondomColor2(self):
        return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

    def randomChar(self):
        return chr(random.randint(65, 90))

    def drawFont(self):
        for t in range(4):
            self.draw.text((60 * t + 10, 10), self.randomChar(), font=self.buildImgFont(), fill=self.rondomColor2())

    def imgFilter(self):
        return self.image.filter(ImageFilter.BLUR)


if __name__ == '__main__':
    veriCode = verificationCode()
    veriCode.buidImg()
    veriCode.buildImgFont()
    veriCode.drawImg()
    veriCode.fillImg()
    veriCode.drawFont()
    print('drawFont catch!')
    veriCode.imgFilter()
    veriCode.image.save('veriCode.jpg', 'jpeg')
