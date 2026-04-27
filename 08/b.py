import re
import math

with open('input.txt') as input:
    [head, _, *rest] = input.read().splitlines()
    graph = {}

    for line in rest:
        [key, left, right] = re.findall(r'\w+', line)
        graph[key] = (left, right)

    keys_that_end_with_A = [key for key in graph if key.endswith('A')]
    
    def get_steps_for_key(key):
        steps = 0
        current_key = key
        while not current_key.endswith('Z'):
            direction = head[steps % len(head)]
            left, right = graph[current_key]
            current_key = left if direction == 'L' else right
            steps += 1
        return steps
    
    all_Steps = [get_steps_for_key(key) for key in keys_that_end_with_A]
    print(math.lcm(*all_Steps))
