# https://www.youtube.com/watch?v=guOyA7Ijqgk

import re

class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Point2D(x={self.x}, y={self.y})"

class Ray2D:
    def __init__(self, pos: Point2D, vel: Point2D):
            self.pos = pos
            self.vel = vel

            self.a = vel.y
            self.b = -vel.x
            self.c = vel.y * pos.x - vel.x * pos.y
        
    def __repr__(self) -> str:
            return f"Ray2D(pos={self.pos}, vel={self.vel})"

with open('input.txt') as input:
    rays = []

    for line in input.readlines():
        [x1, y1, _, x2, y2, _] = map(int, re.findall(r"-?\d+", line))
        a = Point2D(x1, y1)
        b = Point2D(x2, y2)
        ray = Ray2D(a, b)
        rays.append(ray)

    total = 0

    for i in range(len(rays)):
        for j in range(i + 1, len(rays)):
            r1 = rays[i]
            r2 = rays[j]
            
            if r1.a * r2.b == r1.b * r2.a:
                continue

            x = (r1.c * r2.b - r2.c * r1.b) / (r1.a * r2.b - r2.a * r1.b)
            y = (r2.c * r1.a - r1.c * r2.a) / (r1.a * r2.b - r2.a * r1.b)

            low = 200000000000000
            high = 400000000000000

            if low <= x <= high and low <= y <= high:
                if all((x - hs.pos.x) * hs.vel.x >= 0 and (y - hs.pos.y) * hs.vel.y >= 0 for hs in (r1, r2)):
                    total += 1

    print(total)
