from PIL import Image
from random import randrange, randint
import glob
import os
import shutil

width, height = 16, 16

txts = glob.glob("gen*.txt")
print(txts[-1][3:-4])
gen = int(txts[-1][3:-4])

with open('select5.txt','r') as file:
    numbers = [ int(_) for _ in file.read().split('\n')[:-1] ]
    
    # 代表画像の生成
    with open('gen{}.txt'.format(gen),'r') as fff:
        gens = fff.read().replace('[','').replace(']','').split('\n')
        number = numbers[0]
        r = [ int(_) for _ in gens[number*3].split(', ')]
        g = [ int(_) for _ in gens[number*3+1].split(', ')]
        b = [ int(_) for _ in gens[number*3+2].split(', ')]
        
    img = Image.new('RGB', (width, height))
    cnt = 0
    for y in range(height):
        for x in range(width):
            img.putpixel((x, y), (r[cnt], g[cnt], b[cnt]))
            cnt += 1
    img.resize((256, 256), Image.BOX).save('{}.png'.format(str(gen)))

with open('gen{}.txt'.format(gen+1),'w') as file1:
    with open('gen{}.txt'.format(gen),'r') as file:
        head = file.read()
        data = head.replace('[','').replace(']','').split('\n')
        for i in range(128):
            print(i)
            # 親を含める
            if i == 32:
                r = data[numbers[0]*3]
                g = data[numbers[0]*3+1]
                b = data[numbers[0]*3+2]
            elif i == 64:
                r = data[numbers[1]*3]
                g = data[numbers[1]*3+1]
                b = data[numbers[1]*3+2]
            elif i == 96:
                r = data[numbers[2]*3]
                g = data[numbers[2]*3+1]
                b = data[numbers[2]*3+2]
            elif i == 120:
                r = data[numbers[3]*3]
                g = data[numbers[3]*3+1]
                b = data[numbers[3]*3+2]
            else:
                r, g, b = [], [], []
                cnt = 0
                for y in range(16):
                    for x in range(16):
                        mutation = randint(0,99)
                        if mutation < 5:
                            # 5/100の確率で突然変異
                            r.append((randrange(0, 255, 20)))
                            g.append((randrange(0, 255, 20)))
                            b.append((randrange(0, 255, 20)))
                        else:
                            # 4つからランダムに選んで交配
                            rand = randint(0,3)
                            r.append(int(data[numbers[rand]*3].split(', ')[cnt]))
                            g.append(int(data[numbers[rand]*3+1].split(', ')[cnt]))
                            b.append(int(data[numbers[rand]*3+2].split(', ')[cnt]))
                        cnt += 1
                                        
            file1.write('{}\n{}\n{}\n'.format(r,g,b))

# 前世代の代表画像生成

# 前世代のファイルの移動
os.mkdir(str(gen))
shutil.move('gen{}.txt'.format(gen), '{}/'.format(gen))
shutil.move('select1.txt', '{}/'.format(gen))
shutil.move('select2.txt', '{}/'.format(gen))
shutil.move('select3.txt', '{}/'.format(gen))
shutil.move('select4.txt', '{}/'.format(gen))
shutil.move('select5.txt', '{}/'.format(gen))