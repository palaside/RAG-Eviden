# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy as np
import pytesseract

def find_best_quiet_zone(im, y_start, y_end, search_range=60):
    """
    Finds a horizontal band in im between (target - search_range) and (target + search_range)
    where vertical variation is minimal (uniform background).
    """
    arr = np.array(im.convert('RGB'))
    h, w, _ = arr.shape
    
    # helper to find quiet y near y_val
    def scan_quiet(y_val, direction=1): # direction 1=down, -1=up
        best_y = y_val
        min_var = float('inf')
        for dy in range(0, search_range):
            y = y_val + dy * direction
            if 0 <= y < h:
                # check row slice in middle 70% of image width
                row = arr[y, int(w*0.2):int(w*0.8)]
                var = np.var(row)
                if var < min_var:
                    min_var = var
                    best_y = y
                if var < 15.0: # clean background found
                    return y
        return best_y

    top_y = scan_quiet(y_start, direction=-1)
    bot_y = scan_quiet(y_end, direction=1)
    return top_y, bot_y

print("Quiet Zone detector defined.")
