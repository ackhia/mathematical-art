
from random import randint

fireflies = []
targets = []

def create_flys(n, _size = 'small'):
    for _ in range(n):
        f = {
        'direction': random(0, TWO_PI),
        'x': randint(0, width),
        'y': randint(0, height),
        'speed': randint(3, 6),
        'target': randint(0, len(targets)-1),
        'brighness': 0.1,
        'size': _size
        }
        fireflies.append(f)

n = 0
def animate():
    for f in fireflies:
        target = targets[f['target']]
        a_rad = atan2(-(target[1] - f['y']), target[0] - f['x']) 
        a_rad = a_rad % TWO_PI
        
        diff = a_rad - f['direction']
        if diff < -PI:
            diff += TWO_PI;
    
        if diff > PI:
            diff -= TWO_PI
    
        global n
        if  diff > 0:
            f['direction'] += map(noise(n), 0, 1, -0.1, 0.3) #random(-0.1,0.3)
        else:
            f['direction'] -= map(noise(n), 0, 1, -0.1, 0.3) #random(-0.1,0.3)
        n += 1
            
        f['direction'] %= TWO_PI
    
        f['x'] += f['speed'] * cos(f['direction'])
        f['y'] -= f['speed'] * sin(f['direction'])
        
        target_distance_sq = sq(f['x'] - target[0]) + sq(f['y'] - target[1])
        assert(f['size'] in ['big', 'small'])
        _size = 1 if f['size'] == 'big' else 2
        f['brighness'] =  (sq(10 - min(sqrt(target_distance_sq), 7)) / 3) - _size
        
        
def set_targets(_targets):
    global targets
    targets = _targets
    
def change_targets():
    for f in fireflies[:floor(len(fireflies)/10)]:
        f['target'] = randint(0, len(targets)-1)
        
def draw():
    fill(100, 255, 100)
    #fill(200, 200,200)
    for f in fireflies:
        circle(f["x"], f["y"], f['brighness'])
    
    #fill(255,255,255)
    #for t in targets:
    #    circle(t[0], t[1], 5)
