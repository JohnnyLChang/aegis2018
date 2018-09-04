from PIL import Image
from numpy import *

img = Image.open('./2018AEGIS_onion.bmp')
arr = array(img)

def decode(d):
    unbin = ''
    for i in range(0, len(d), 8):
        unbin += chr(int(''.join(d[i:i+8]), base=2))
    print(unbin)

for i in range(255):
    data = ''
    for x in arr:
        for y in x:
            if y[1] == i:
                data += '0'
            elif y[1] == i+1:
                data += '1'
    decode(data)