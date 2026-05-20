def hash(string):
    current = 0

    for char in string:
        current += ord(char)
        current *= 17
        current %= 256

    return current

with open('input.txt') as input:
    steps = input.read().strip().split(',')
    total = sum(hash(step) for step in steps)
    print(total)
