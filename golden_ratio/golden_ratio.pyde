from random import random, randint

golden_ratio_conjugate = 0.618033988749895
dots = []

def setup():
    size(1000, 600)
    frameRate(60)
    colorMode(HSB, 1, 1, 1)
    dots.append(list(create_dots(80, 200)))
    dots.append(list(create_dots(50, 150)))
    dots.append(list(create_dots(100, 80)))
    dots.append(list(create_dots(10, 200)))

c = random()
def gr():
    global c
    c += golden_ratio_conjugate * randint(0,20)
    c %= 1.0
    return c

def face(x, y, s, a, colour, wink=False, vol_x=False, vol_y=False, rotation_vol=False):
        pushMatrix()
        fill(colour,0.5,0.95)
        translate(x, y)
        rotate(a)
        circle(0, 0, s)
        fill(colour,golden_ratio_conjugate,0.95)
        ss = s / 3 * golden_ratio_conjugate
        circle(ss, ss, ss)
        fill(colour,golden_ratio_conjugate,0.95)
        
        circle(0-ss, ss, ss/2)
        if wink:
            stroke(colour,golden_ratio_conjugate,0.3)
            translate(-5,-8)
            strokeWeight(1.7)
            line(ss, -ss-8, ss-18, -ss+18) 
        else:
            circle(ss, 0-ss, ss/2)
        popMatrix()

def create_dots(n, max_size):
    dot_list = []
    for _ in range(n):
        x = gr() * width 
        y = gr() * height 
        s = gr() * max_size
        a = gr() * TWO_PI
        vol_x = gr() if random() > 0.5 else -gr()
        vol_y = gr() if random() > 0.5 else -gr()
        rotation_vol = gr() if random() > 0.5 else -gr()
        angle = gr() * TWO_PI
        colour = gr()
        #face(x, y, s, a)
        dot_list.append({"x": x, "y": y, "s": s, "a": a, "colour": colour, "vol_y":vol_y, "vol_x":vol_x, "rotation_vol": rotation_vol})
    return dot_list

def draw_dots(d):
    for dot in d:
        face(**dot)

bgc = gr()
def animate():
    for l in dots:
        for d in l:
            d["x"] += d["vol_x"] * 15
            d["y"] += d["vol_y"] * 15
            d["x"] = d["x"] % width
            d["y"] = d["y"] % height
            d["a"] += d["rotation_vol"] / 5
            if d["a"] > 0:
                d["a"] = d["a"] % TWO_PI
            else:
                d["a"] = d["a"] % -TWO_PI
        

a = golden_ratio_conjugate
def draw():
    background(bgc, golden_ratio_conjugate, 0.9);
    draw_dots(dots[0])

    #filter(BLUR, 20)
    
    draw_dots(dots[1])
        
    draw_dots(dots[2])
    
   # filter(BLUR, 0.3); 
        
    draw_dots(dots[3])
    
    #filter(BLUR, 1); 
    
    global a
    a += -0.1
    face(width*golden_ratio_conjugate, height*golden_ratio_conjugate, 225, a, golden_ratio_conjugate, True)
    
    animate()
    print(frameRate)
