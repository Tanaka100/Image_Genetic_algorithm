from random import randrange

with open('gen0.txt','w') as file:
    
    for i in range(128):
        r, g, b = [], [], []
        for y in range(16):
            for x in range(16):
                r.append((randrange(0, 255, 20)))
                g.append((randrange(0, 255, 20)))
                b.append((randrange(0, 255, 20)))
            
        file.write('{}\n{}\n{}\n'.format(r,g,b))