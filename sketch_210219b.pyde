from math import hypot
from random import randint, choice, shuffle

def ED(a, b):
    return hypot(a[0]-b[0], a[1] - b[1])

        
        
k = []
def setup():
    size(1780 * 2, 1000 * 2)
    background(0)
    global k
    im = loadImage('Full.jpg')
    for _ in range(50):
        points = []
        for i in range(700):
            h = randint(0, 1780 * 2)
            w = randint(0, 1000 * 2)
            points.append((h,w))
        for i in points:
            for j in points:
                if hypot(i[0]-j[0], i[1]-j[1]) < 100 and choice([0,0,1]):
                    strokeWeight(3)
                    k.append([i[0], i[1], j[0], j[1], im.get(i[0]/2, i[1]/2)])
    shuffle(k)
    for a, b, c, d, e in k:
        stroke(e)
        line(a, b, c, d)
    save('JTS.jpg')
