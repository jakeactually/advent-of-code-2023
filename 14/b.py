def get_positions(matrix, char):
    s = set()

    for y, row in enumerate(matrix):
        for x, c in enumerate(row):
            if c == char:
                s.add((x, y))

    return s

def roll(current_balls, axis_1_length, axis_2_positions):
    new_balls = set()

    for x in range(axis_1_length):
        collecting_balls = True
        chunks = [[]]

        for y in axis_2_positions:
            if (x, y) in current_balls:
                if not collecting_balls:                    
                    chunks.append([])
                
                chunks[-1].append((x, y, True))
                collecting_balls = True
            
            if (x, y) in walls_set:
                chunks[-1].append((x, y, False))
                collecting_balls = False

        start = axis_2_positions[0]
        end = axis_2_positions[-1]
        sign = 1 if start > end else -1

        for chunk in chunks:
            balls = [y for (_, y, is_ball) in chunk if is_ball]
            walls = [y for (_, y, is_ball) in chunk if not is_ball]

            if not balls:
                continue

            first_wall = walls[0] + sign if walls else end
            new_balls |= set([(x, first_wall + i * sign) for i in range(len(balls))])
    
    return new_balls

with open('input.txt') as input:
    lines = input.read().splitlines()
    matrix = [list(s) for s in lines]

    balls_set = get_positions(matrix, 'O')
    walls_set = get_positions(matrix, '#')

    height = len(matrix)
    width = len(matrix[0])

    new_balls = roll(balls_set, width, list(range(height)))

    for y in range(height):
        for x in range(width):
            if (x, y) in new_balls:
                print('0', end='')
            elif (x, y) in walls_set:
                print('#', end='')
            else:
                print('.', end='')

        print()
