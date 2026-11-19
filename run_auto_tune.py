# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy as np

raw_ori = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'

def auto_tune_slice(img_fn, y0_target, y1_target):
    fp = os.path.join(raw_ori, img_fn)
    im = Image.open(fp)
    arr = np.array(im.convert('RGB'))
    h, w, _ = arr.shape
    
    # search y0 (-40 to +40)
    best_y0, min_v0 = y0_target, float('inf')
    for dy in range(-40, 41):
        y = y0_target + dy
        if 0 <= y < h:
            v = np.var(arr[y, int(w*0.2):int(w*0.8)])
            if v < min_v0:
                min_v0 = v
                best_y0 = y
                
    # search y1 (-40 to +40)
    best_y1, min_v1 = y1_target, float('inf')
    for dy in range(-40, 41):
        y = y1_target + dy
        if 0 <= y < h:
            v = np.var(arr[y, int(w*0.2):int(w*0.8)])
            if v < min_v1:
                min_v1 = v
                best_y1 = y
                
    print(f"{img_fn}: y0={best_y0} (var={min_v0:.1f}), y1={best_y1} (var={min_v1:.1f}), h={best_y1-best_y0}")
    return best_y0, best_y1

print("Tuning Count 2:")
auto_tune_slice("LINE_capture_800252921.297142.jpg", 3600, 4150)

print("Tuning Count 5 (ถอดเหล็ก 4000):")
auto_tune_slice("LINE_capture_800253185.789705.jpg", 4100, 4650)

print("Tuning Count 8-13:")
auto_tune_slice("LINE_capture_800253553.588898.jpg", 2650, 3150)
auto_tune_slice("LINE_capture_800253553.588898.jpg", 3450, 4100)
auto_tune_slice("LINE_capture_800253553.588898.jpg", 4200, 4700)
auto_tune_slice("LINE_capture_800253553.588898.jpg", 4900, 5500)
auto_tune_slice("LINE_capture_800253553.588898.jpg", 5600, 6200)

print("Tuning Count 14-16:")
auto_tune_slice("LINE_capture_800254134.610661.jpg", 3350, 3950)
auto_tune_slice("LINE_capture_800254134.610661.jpg", 4600, 5250)
auto_tune_slice("LINE_capture_800254134.610661.jpg", 5400, 6050)

print("Tuning Count 19-21:")
auto_tune_slice("LINE_capture_800256213.882803.jpg", 150, 850)
auto_tune_slice("LINE_capture_800256213.882803.jpg", 1050, 1750)
auto_tune_slice("LINE_capture_800256213.882803.jpg", 2050, 2750)
