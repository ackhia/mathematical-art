

def turn_direction(target, current):
    prov = target - current
    
    if -PI < prov and prov <= PI:
        turn = prov 
    elif prov > PI:
        turn = prov - TWO_PI
    elif prov  <= -PI:
        turn = prov + TWO_PI 

    return  prov




target = [300, 300]

print atan2(10,10) * 180 / PI

def setup():
    size(600,600)
    frameRate(30)
    
def animate():

    
def draw():
    animate()
    background(0)
    circle(ff["x"], ff["y"], 3)
    circle(target[0], target[1], 5)
