# https://www.youtube.com/watch?v=guOyA7Ijqgk

import sympy

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open('input.txt')]

xn, yn, zn, vxn, vyn, vzn = sympy.symbols("xn yn zn vxn vyn vzn")

equations = []

for sx, sy, sz, vx, vy, vz in hailstones:
    equations.append((xn - sx) * (vy - vyn) - (yn - sy) * (vx - vxn))
    equations.append((yn - sy) * (vz - vzn) - (zn - sz) * (vy - vyn))

answers = sympy.solve(equations)
print(answers)
