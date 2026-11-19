# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('EDOK_NUI/SSOT_STREAM_ASSETS/node_001.jpg')
top = im.crop((0, 0, im.width, 350))
top.save('node001_top_banner.png')
print("Saved node001_top_banner.png, size:", top.size)
