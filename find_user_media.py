# -*- coding: utf-8 -*-
import os
import glob
from PIL import Image

# Search where media_1795036777323_42d3d722.png was cropped from
media_p = r'C:/Users/EVE/.gemini/antigravity/brain/c8211d09-030e-4b24-8837-3ce9589aa4a6/.user_uploaded/media_1795036777323_42d3d722.png'
if os.path.exists(media_p):
    with Image.open(media_p) as im:
        print("User uploaded image size:", im.size)
