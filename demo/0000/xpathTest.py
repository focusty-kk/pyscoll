
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 0000题 将你的QQ头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果


from PIL import Image, ImageDraw, ImageFont

original = Image.open('/Users/yanghui/Downloads/SoftColl/21f7cc8bdb7a4bfc85d5436becbc6e3c (1).jpg')

fnt = ImageFont.truetype("SFNSTextItalic.ttf", 80)

d = ImageDraw.Draw(original)

d.text((200, 0), "6", font=fnt, fill=(255,0,0,255))

original.save("finnal.jpg")
