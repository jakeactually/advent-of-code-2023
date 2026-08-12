import re
from typing import Self

class Point2D:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> Self:
        return Point2D(self.x * scalar, self.y * scalar)

    def dot(self, other: Self) -> float:
        return self.x * other.x + self.y * other.y
    
    def __repr__(self) -> str:
        return f"Point2D(x={self.x}, y={self.y})"

class Ray2D:
    origin: Point2D
    direction: Point2D

    def __init__(self, origin, direction):
            self.origin = origin
            self.direction = direction

    def distance_to_point(self, p: Point2D) -> float:
        t = self.project_point(p)
        closest = self.point_at(t)
        return p.distance_to(closest)
    
    def __repr__(self) -> str:
            return f"Ray2D(origin={self.origin}, direction={self.direction})"

with open('input.txt') as input:
    rays = []

    for line in input.readlines():
        [x1, y1, _, x2, y2, _] = map(int, re.findall(r"-?\d+", line))
        a = Point2D(x1, y1)
        b = Point2D(x2, y2)
        ray = Ray2D(a, b)
        rays.append(ray)

    for i in range(len(rays)):
        for j in range(i + 1, len(rays)):
            a = rays[i]
            b = rays[j]
            
            d = b.origin - a.origin
            det = b.direction.dot(a.direction)

            if det == 0:
                print("never")
                continue

            u = d.dot(b.direction) / det
            v = d.dot(a.direction) / det

            p1 = a.origin + a.direction * u
            p2 = b.origin + b.direction * v

            print(p1, p2)
