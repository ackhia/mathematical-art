from random import random, randint

size(1000, 600)
colorMode(HSB, 1, 1, 1)

golden_ratio_conjugate = 0.618033988749895

i = 1
c = random()
def gr():
    global c
    c += golden_ratio_conjugate * randint(0,20)
    c %= 1.0
    return c

def face(x, y, s, a, wink=False):
        pushMatrix()
        colour = gr()
        fill(colour,0.5,0.95)
        translate(x, y)
        rotate(a)
        circle(0, 0, s)
        fill(colour,gr(),0.95)
        ss = s / 3 * golden_ratio_conjugate
        circle(ss, ss, ss)
        fill(colour,gr(),0.95)
        circle(ss, 0-ss, ss/2)
        if wink:
            scale(0.5, 1);
        circle(0-ss, ss, ss/2)
        popMatrix()

def dots(n, max_size):
    for _ in range(n):
        x = gr() * width 
        y = gr() * height 
        s = gr() * max_size
        a = gr() * TWO_PI
        face(x, y, s, a)

dots(300, 200)
    
filter(BLUR, 20)

dots(500, 150)
    
    
dots(600, 80)

filter(BLUR, 0.3); 
    
dots(10, 200)

filter(BLUR, 1); 

face(width*golden_ratio_conjugate, height*golden_ratio_conjugate, 225, 0)
