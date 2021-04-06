

fireflys = []

def create_flys(n):
    for _ in range(n):
        ff = {
        'direction': random(0, TWO_PI),
        'x': randomInt(0, width),
        'y': randomInt(0, height),
        'speed': randomInt(3, 6)
        }
        fireflys.append(ff)
        
def animate():
    for f in fireflys:
        a_rad = atan2(-(target[1] - f['y']), target[0] - f['x']) 
        a_rad = a_rad % TWO_PI
        print f['direction'], a_rad, turn_direction(a_rad, f['direction'])
        
        diff = a_rad - f['direction']
        if diff < -PI:
            diff += TWO_PI;
    
        if diff > PI:
            diff -= TWO_PI
    
        if  diff > 0:
            f['direction'] += random(-0.1,0.3)
        else:
            f['direction'] -= random(-0.1,0.3)
            
        f['direction'] %= TWO_PI
    
        f['x'] += ff['speed'] * cos(f['direction'])
        f['y'] -= ff['speed'] * sin(f['direction'])
        
def draw():
    for f in fireflys:
        circle(f["x"], f["y"], 3)
