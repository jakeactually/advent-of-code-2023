with open('12/input.txt') as input:
    total = 0

    for line in input:
        [springs, counts] = line.strip().split(' ')
        list_springs = ([*springs, '?'] * 5)[:-1]
        int_counts = [int(i) for i in counts.split(',')] * 5
        
        stack = [([], [], int_counts)]
        cache = set()

        while stack:
            positions, groups, counts = stack.pop()

            if f'{positions}' in cache:
                total += 1
                continue

            if not counts:
                ranges = [range(p, p + g) for p, g in zip(positions, groups)]
                valid = True

                for i, s in enumerate(list_springs):
                    if s == '#' and not any(i in r for r in ranges):
                        valid = False
                
                if valid:
                    total += 1
                    cache.add(f'{positions}')
                
                continue

            [c, *cs] = counts
            
            start = positions[-1] + groups[-1] + 1 if positions else 0
            
            for i in range(start, len(list_springs) - sum(cs) - len(cs) + 1 - c):
                valid = True
                
                for j in range(i, i + c):
                    if list_springs[j] == '.':
                        valid = False

                if (i + c) < len(list_springs) and list_springs[i + c] == '#':
                    valid = False

                if i > 0 and list_springs[i - 1] == '#':
                    valid = False

                if list_springs[i + c:].count('#') > sum(cs):
                    valid = False

                if valid:
                    stack.append(([*positions, i], [*groups, c], cs))

    print(total)
