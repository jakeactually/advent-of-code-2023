
import numpy as np

with open('input.txt') as input:
    paragraphs = input.read().split('\n\n')

    matrices = [
        np.array([list(l) for l in p.splitlines()])
        for p in paragraphs
    ]

    total = 0

    for m in matrices:
        for y in range(1, len(m) - 1):
            cut = min(y, len(m) - y)
            top = m[:y][-cut:]
            bottom = np.flipud(m[y:][:cut])

            if np.array_equal(top, bottom):
                total += y
                break

        m = m.T

        for y in range(1, len(m) - 1):
            cut = min(y, len(m) - y)
            top = m[:y][-cut:]
            bottom = np.flipud(m[y:][:cut])

            if np.array_equal(top, bottom):
                total += y * 100
                break
    
    print(total)
        