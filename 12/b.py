with open('input.txt') as input:
    total = 0

    for line in input:
        [springs, counts] = line.strip().split(' ')
        list_springs = list(springs)
        int_counts = [int(i) for i in counts.split(',')]
        
        stack = [([], int_counts)]

        while stack:
            positions, counts = stack.pop()
            
            if not counts:
                print(positions)
                total += 1
                continue

            [c, *cs] = counts
            
            start = positions[-1] if positions else 0
            
            for i in range(start, len(list_springs) - sum(cs) - len(cs) + 1 - c):
                valid = True
                
                for j in range(i, i + c):
                    if list_springs[j] == '.':
                        valid = False

                if (i + c) < len(list_springs) and list_springs[i + c] == '#':
                    valid = False

                if i > 0 and list_springs[i - 1] == '#':
                    valid = False

                if valid:
                    stack.append(([*positions, i + c + 1], cs))

    print(total)
