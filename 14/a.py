with open('input.txt') as input:
    lines = input.read().splitlines()
    matrix = [list(s) for s in lines]

    height = len(matrix)
    width = len(matrix[0])

    total = 0

    for x in range(width):
        collecting_balls = True
        chunks = [[]]

        for y in reversed(range(height)):
            current = matrix[y][x]

            if current == 'O':
                if not collecting_balls:                    
                    chunks.append([])
                
                collecting_balls = True
            if current == '#':
                collecting_balls = False
            
            if current != '.':
                chunks[-1].append((y, current))

        for c in chunks:
            balls = [n for (n, r) in c if r == 'O']
            cubes = [n for (n, r) in c if r == '#']

            first = cubes[0] + 1 if cubes else 0
            mapped_balls = [height - first - i for i in range(len(balls))]

            total += sum(mapped_balls)

    print(total)
