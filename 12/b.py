with open('input.txt') as input:
    lines = input.read().splitlines()
    sorted_lines = sorted(lines, key = lambda l: l.count('?'))
    total = 0

    for line in sorted_lines:
        [springs, counts] = line.strip().split(' ')
        list_springs = ([*springs, '?'] * 5)[:-1]
        int_counts = [int(i) for i in counts.split(',')] * 5
        
        stack = [([], False, list_springs)]
        visited = set()

        while stack:
            (groups, in_group, springs) = stack.pop()

            if f'{groups} ' + ''.join(springs) in set():
                continue

            visited.add(f'{groups} ' + ''.join(springs))

            if not springs:
                if groups == int_counts:
                    total += 1
                continue

            if len(springs) < sum(int_counts) - sum(groups):
                continue

            print(groups, springs)

            [x, *xs] = springs

            match x:
                case '?':
                    stack.append((groups, in_group, ['#', *xs]))
                    stack.append((groups.copy(), in_group, ['.', *xs]))
                case '#':
                    if not in_group:
                        groups.append(0)

                    gi = len(groups) - 1
                    groups[gi] += 1

                    if gi < len(int_counts) and groups[gi] <= int_counts[gi]:
                        stack.append((groups, True, xs))
                case '.':
                    if in_group:
                        gi = len(groups) - 1
                        
                        if groups[gi] == int_counts[gi]:
                            stack.append((groups, False, xs))
                    else:
                        stack.append((groups, False, xs))

    print(total)
