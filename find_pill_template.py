# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
from PIL import Image

def load_cv2_unicode(p):
    im = Image.open(p)
    return np.array(im.convert('L'))

template_p = r'C:/Users/EVE/.gemini/antigravity/brain/c8211d09-030e-4b24-8837-3ce9589aa4a6/.user_uploaded/media_1795035913928_3189cf63.png'
template = load_cv2_unicode(template_p)
th, tw = template.shape[:2]

asset_dir = r'd:\Project\ชวกม.2\EDOK_NUI\SSOT_STREAM_ASSETS'
print("Searching for date pill template in nodes 1 to 50...")

for i in range(1, 51):
    fn = f"node_{i:03d}.jpg"
    fp = os.path.join(asset_dir, fn)
    if not os.path.exists(fp):
        continue
    img = load_cv2_unicode(fp)
    crop_top = img[:min(800, img.shape[0]), :]
    if crop_top.shape[0] < th or crop_top.shape[1] < tw:
        continue
    res = cv2.matchTemplate(crop_top, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.65:
        print(f"FOUND MATCH in {fn}! MaxVal = {max_val:.3f} at location {max_loc}")
