from PIL import Image
import os

dl_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'
img = Image.open(os.path.join(dl_root, 'LINE_capture_800252756.687906.jpg'))

# Crop y=2000 to y=3200
crop1 = img.crop((0, 2000, img.width, 3200))
crop1.save(r'd:\Project\ชวกม.2\EDOK_NUI\test_real_crop_01.png')
print("Cropped real chat 01:", crop1.size)
