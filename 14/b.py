def get_positions(matrix, char):
    s = set()

    for y, row in enumerate(matrix):
        for x, c in enumerate(row):
            if c == char:
                s.add((x, y))

    return s

with open('input.txt') as input:
    lines = input.read().splitlines()
    matrix = [list(s) for s in lines]

    balls_set = get_positions(matrix, 'O')
    walls_set = get_positions(matrix, '#')

    height = len(matrix)
    width = len(matrix[0])

    total = 0

    for x in range(width):
        collecting_balls = True
        chunks = [[]]

        for y in reversed(range(height)):
            if (x, y) in balls_set:
                if not collecting_balls:                    
                    chunks.append([])
                
                chunks[-1].append((x, y, True))
                collecting_balls = True
            
            if (x, y) in walls_set:
                chunks[-1].append((x, y, False))
                collecting_balls = False

        for chunk in chunks:
            balls = [y for (x, y, is_ball) in chunk if is_ball]
            walls = [y for (x, y, is_ball) in chunk if not is_ball]

            first_wall = walls[0] + 1 if walls else 0
            mapped_balls = [height - first_wall - i for i in range(len(balls))]

            total += sum(mapped_balls)

    print(total)
