import re

with open('input.txt') as input:
    [head, _, *rest] = input.read().splitlines()
    graph = {}

    for line in rest:
        [key, left, right] = re.findall(r'\w+', line)
        graph[key] = (left, right)

    steps = 0
    current_key = 'AAA'

    while current_key != 'ZZZ':
            direction = head[steps % len(head)]
            left, right = graph[current_key]
            current_key = left if direction == 'L' else right
            steps += 1

    print(steps)
