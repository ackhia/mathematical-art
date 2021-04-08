
from random import randint

import fireflies

add_library("postfx")
fx = None
img = None
img_cords = []

def setup():
    size(700,700,P3D)
    frameRate(30)
    smooth()
    noStroke()
    background(0,0,0)
    
    global fx
    fx = PostFX(this)
    global img
    img = loadImage('peace.png')
    img.resize(width, height)
    img.loadPixels();
    global img_cords
    for y in range(img.height):
        for x in range(img.width):
            if img.pixels[y*width+x] != 0:
                img_cords.append([x, y])
                
    fireflies.set_targets(img_cords)
    fireflies.create_flys(5, 'big')
    #fireflies.set_targets([[100,100]])
    
def animate():
    fireflies.animate()

i = 1
def draw():
    global i
    if len(fireflies.fireflies) <= 4000:
        if i > 200 and randint(1,3) == 1:
            fireflies.create_flys(1)
        if i > 400:
            fireflies.create_flys(4)
        if i > 500:
            fireflies.create_flys(4)
        #print i, len(fireflies.fireflies)
    if i > 600:
        fx.render().rgbSplit(20).compose()
    i += 1
    animate()
    fill(0,0,0,7)
    rect(0,0,width,height)
    #image(img, 0, 0)
    fireflies.draw()
    print frameRate
    if randint(0,10) == 7:
        fireflies.change_targets()
    
    #fx.render().rgbSplit(20).compose();
    saveFrame("frames/######.tif")
