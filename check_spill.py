import os
from PIL import Image

preview_dir = r'd:\Project\ชวกม.2\EDOK_NUI\PDF_PREVIEW_PAGES'
for fn in sorted(os.listdir(preview_dir)):
    fp = os.path.join(preview_dir, fn)
    im = Image.open(fp)
    # top 150px
    top_crop = im.crop((0, 0, im.width, 150))
    # bottom 150px
    bot_crop = im.crop((0, im.height - 150, im.width, im.height))
    # let's save thumbnails or check where the element is
    # save bottom and top
