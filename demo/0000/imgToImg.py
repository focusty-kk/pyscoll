#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from PIL import Image, ImageDraw, ImageFont


def imgCount(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('SFNSTextItalic.ttf', size=40)
    fontColor = '#f60'
    width, height = img.size
    print(img.size)
    draw.text((width - 200, 0), '99', font=font, fill=fontColor)
    img.save('saveImg.jpg')


if __name__ == '__main__':
    image = Image.open('/Users/yanghui/Downloads/SoftColl/21f7cc8bdb7a4bfc85d5436becbc6e3c (1).jpg')
    imgCount(image)
