with open('input.txt') as input:
    total = 0

    for line in input:
        [springs, counts] = line.strip().split(' ')
        list_springs = list(springs)
        int_counts = [int(i) for i in counts.split(',')]
        
        stack = [([], False, list_springs)]

        while stack:
            (groups, in_group, springs) = stack.pop()

            if not springs:
                if groups == int_counts:
                    total += 1
                continue

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
