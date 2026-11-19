# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy as np

def fine_tune_y(arr, y_val, search_range=50, direction=0):
    """
    Finds y near y_val where variance of row (excluding side margins) is minimum.
    direction: 0 = both ways, 1 = downwards only, -1 = upwards only
    """
    h, w, _ = arr.shape
    best_y = y_val
    min_var = float('inf')
    
    if direction == 0:
        rng = range(-search_range, search_range + 1)
    elif direction == 1:
        rng = range(0, search_range + 1)
    else:
        rng = range(-search_range, 1)
        
    for dy in rng:
        y = y_val + dy
        if 0 <= y < h:
            # check middle 60% of row
            row = arr[y, int(w*0.2):int(w*0.8)]
            v = np.var(row)
            if v < min_var:
                min_var = v
                best_y = y
    return best_y, min_var

print("fine_tune_y defined")
