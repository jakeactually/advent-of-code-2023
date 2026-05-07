with open('input.txt') as input:
    total = 0

    for line in input:
        [springs, counts] = line.strip().split(' ')
        list_springs = ([*springs, '?'] * 5)[:-1]
        int_counts = [int(i) for i in counts.split(',')] * 5

        stack = [([], False, list_springs)]
        result = []

        def stack_append(tuple):
            # print(tuple)
            stack.append(tuple)

        while stack:
            (groups, in_group, springs) = stack.pop()

            if not springs:
                if groups == int_counts:
                    result.append(groups)
                continue
            
            if len(springs) < sum(int_counts[len(groups):]) + len(int_counts) - 1 - len(groups):
                continue

            [x, *xs] = springs

            match x:
                case '?':
                    stack_append((groups, in_group, ['#', *xs]))
                    stack_append((groups.copy(), in_group, ['.', *xs]))
                case '#':
                    if not in_group:
                        groups.append(0)
                    group_index = len(groups) - 1
                    groups[group_index] += 1
                    if group_index < len(int_counts) and groups[group_index] <= int_counts[group_index]:
                        stack_append((groups, True, xs))
                case '.':
                    if in_group:
                        group_index = len(groups) - 1
                        if groups[group_index] == int_counts[group_index]:
                            stack_append((groups, False, xs))
                    else:
                        stack_append((groups, False, xs))
        
        print(len(result))
        total += len(result)

    print(total)
