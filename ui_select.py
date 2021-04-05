from PIL import Image
import numpy as np
from random import randrange
import glob

width, height = 16, 16

txts = glob.glob("gen*.txt")
gen = int(txts[-1][3:-4])
print("gen", gen)

txts = glob.glob("select*.txt")
phase = int(txts[-1][-5])+1
print("phase", phase)

# 各phaseテキストファイルに書かれているidxを取得
with open('select{}.txt'.format(phase-1),'r') as file:
    text = file.read()
    numbers = [ int(_) for _ in text.split('\n')[:-1] ]

with open('select{}.txt'.format(phase),'w') as ffff:
    for i in range(0, len(numbers), 2):
        with open('gen{}.txt'.format(gen),'r') as file:
            head = file.read()
            r1 = [ int(_) for _ in head.replace('[','').replace(']','').split('\n')[numbers[i]*3].split(', ')]
            g1 = [ int(_) for _ in head.replace('[','').replace(']','').split('\n')[numbers[i]*3+1].split(', ')]
            b1 = [ int(_) for _ in head.replace('[','').replace(']','').split('\n')[numbers[i]*3+2].split(', ')]
            r2 = [ int(_) for _ in head.replace('[','').replace(']','').split('\n')[numbers[i+1]*3].split(', ')]
            g2 = [ int(_) for _ in head.replace('[','').replace(']','').split('\n')[numbers[i+1]*3+1].split(', ')]
            b2 = [ int(_) for _ in head.replace('[','').replace(']','').split('\n')[numbers[i+1]*3+2].split(', ')]

        # Imageオブジェクトを作成する
        img1 = Image.new('RGB', (width, height))
        img2 = Image.new('RGB', (width, height))

        cnt = 0
        for y in range(height):
            for x in range(width):
                img1.putpixel((x, y), (r1[cnt], g1[cnt], b1[cnt]))
                img2.putpixel((x, y), (r2[cnt], g2[cnt], b2[cnt]))
                cnt += 1
                
        dst = Image.new('RGB', (width*2+1, height))
        bar = Image.new('RGB', (1, height))
        for y in range(height):
            bar.putpixel((0, y), (0,0,0))

        dst.paste(img1, (0, 0))
        dst.paste(bar, (width, 0))
        dst.paste(img2, (width+1, 0))

        dst.resize((528, 256), Image.BOX).save('tmp.png')
        
        while True:
            select = input("{}-{}：".format(phase, i))
            if select == "j":
                ffff.write('{}\n'.format(numbers[i]))
                break
            if select == "k":
                ffff.write('{}\n'.format(numbers[i+1]))
                break