
import numpy as np

with open('input.txt') as input:
    paragraphs = input.read().split('\n\n')

    matrices = [
        np.array([list(l) for l in p.splitlines()])
        for p in paragraphs
    ]

    total = 0

    for m in matrices:
        for y in range(1, len(m)):
            cut = min(y, len(m) - y)
            top = m[:y][-cut:]
            bottom = np.flipud(m[y:][:cut])

            if np.count_nonzero(top != bottom) == 1:
                total += y * 100
                break

        m = m.T

        for y in range(1, len(m)):
            cut = min(y, len(m) - y)
            top = m[:y][-cut:]
            bottom = np.flipud(m[y:][:cut])

            if np.count_nonzero(top != bottom) == 1:
                total += y
                break
    
    print(total)
