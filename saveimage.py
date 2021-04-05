from PIL import Image
import numpy as np
from random import randrange
import glob

width, height = 16, 16

txts = glob.glob("genes*.txt")
gen = int(txts[-1][-6:-5])
print(gen)

with open('select5.txt','r') as file:
    text = file.read()
    number = [ int(_) for _ in text.split('\n')[:-1] ][0]

    with open('out{}.txt'.format(gen),'r') as file:
        head = file.read()
        r1 = [ int(_) for _ in head.replace('[','').replace(']','').split('\n')[number*3].split(', ')]
        g1 = [ int(_) for _ in head.replace('[','').replace(']','').split('\n')[number*3+1].split(', ')]
        b1 = [ int(_) for _ in head.replace('[','').replace(']','').split('\n')[number*3+2].split(', ')]
        
    # オリジナル画像と同じサイズのImageオブジェクトを作成する
    img1 = Image.new('RGB', (width, height))

    cnt = 0
    for y in range(height):
        for x in range(width):
            img1.putpixel((x, y), (r1[cnt], g1[cnt], b1[cnt]))
            cnt += 1

    img1.resize((256, 256), Image.BOX).save('{}.png'.format(str(gen)))