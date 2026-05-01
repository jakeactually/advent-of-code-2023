
import re

with open('input.txt') as input:
    total = 0

    for line in input:
        series = [int(x) for x in re.findall(r'-?\d+', line)]
        stack = []

        while any(series):
            next_series = []

            for i in range(len(series) - 1):
                next_series.append(series[i + 1] - series[i])

            stack.append(series[::-1])
            series = next_series
        
        for i in reversed(range(len(stack) - 1)):
            stack[i].append(
                stack[i][-1] - stack[i + 1][-1]
            )

        total += stack[0][-1]
    
    print(total)
