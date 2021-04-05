from random import random, randint

size(1000, 600)
colorMode(HSB, 1, 1, 1)

golden_ratio_conjugate = 0.618033988749895

i = 1
c = random()
def gr():
    global c
    for _ in range(randint(0,10)):
        c += golden_ratio_conjugate
        c %= 1.0
    #print c
    return c


for _ in range(1000):
    fill(gr(),0.5,0.95)
    x = gr() * width 
    y = gr() * height 
    #print x, y, width, height
    s = gr() * 300
    circle(x, y, s)
    

filter(BLUR, 20)
    
for _ in range(100):
    fill(gr(),0.5,0.95)
    x = gr() * width 
    y = gr() * height 
    #print x, y, width, height
    s = gr() * 150
    circle(x, y, s)
    
filter(BLUR, 20);   
    
for _ in range(1800):
    fill(gr(),0.5,0.95)
    x = gr() * width 
    y = gr() * height 
    #print x, y, width, height
    s = gr() * 50
    circle(x, y, s)
    
filter(ERODE)
