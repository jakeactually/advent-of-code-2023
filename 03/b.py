import re

red_regex = r'(\d+) red'
blue_regex = r'(\d+) blue'
green_regex = r'(\d+) green'

with open('input.txt') as input:
    total = 0

    for line in input:
        reds = [int(red) for red in re.findall(red_regex, line)]
        blues = [int(blue) for blue in re.findall(blue_regex, line)]
        greens = [int(green) for green in re.findall(green_regex, line)]
        powers = max(reds) * max(blues) * max(greens)
        total += powers
    
    print(total)
