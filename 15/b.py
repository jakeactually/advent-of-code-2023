def hash(string):
    current = 0

    for char in string:
        current += ord(char)
        current *= 17
        current %= 256

    return current

with open('input.txt') as input:
    steps = input.read().strip().split(',')
    state = {}

    for step in steps:
        if '-' in step:
            label = step[:-1]
            index = hash(label)

            if index in state and state[index]:
                state[index] = [(l, f) for (l, f) in state[index] if l != label]
        elif '=' in step:
            label, focus = step.split('=')
            index = hash(label)

            if index not in state:
                state[index] = [(label, focus)]
                continue

            boxes = state[index]
            changed = False

            for i, (l, f) in enumerate(boxes):
                if l == label:
                    boxes[i] = (l, focus)
                    changed = True
                    break
            
            if not changed:
                boxes.append((label, focus))

    total = 0

    for box_i, box in state.items():
        for len_i, (_, focus) in enumerate(box):
                total += (box_i + 1) * (len_i + 1) * int(focus)

    print(total)
