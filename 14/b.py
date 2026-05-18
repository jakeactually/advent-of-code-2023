def get_positions(matrix, char):
    s = set()

    for y, row in enumerate(matrix):
        for x, c in enumerate(row):
            if c == char:
                s.add((x, y))

    return s

def roll(current_balls, axis_1_length, axis_2_positions, horizontal):
    new_balls = set()

    def to_global(x, y):
        return (y, x) if horizontal else (x, y)

    for axis_1 in range(axis_1_length):
        collecting_balls = True
        chunks = [[]]

        for axis_2 in axis_2_positions:
            if to_global(axis_1, axis_2) in current_balls:
                if not collecting_balls:                    
                    chunks.append([])
                
                chunks[-1].append((axis_1, axis_2, True))
                collecting_balls = True
            
            if to_global(axis_1, axis_2) in walls_set:
                chunks[-1].append((axis_1, axis_2, False))
                collecting_balls = False

        start = axis_2_positions[0]
        end = axis_2_positions[-1]
        sign = 1 if start > end else -1

        for chunk in chunks:
            balls = [axis_2 for (_, axis_2, is_ball) in chunk if is_ball]
            walls = [axis_2 for (_, axis_2, is_ball) in chunk if not is_ball]

            if not balls:
                continue

            first_wall = walls[0] + sign if walls else end
            new_balls |= set([to_global(axis_1, first_wall + i * sign) for i in range(len(balls))])
    
    return new_balls

def cycle(current_balls):
    balls = current_balls
    
    balls = roll(balls, width, list(reversed(range(height))), False)
    balls = roll(balls, height, list(reversed(range(width))), True)
    balls = roll(balls, width, list(range(height)), False)
    balls = roll(balls, height, list(range(width)), True)

    return balls

with open('input.txt') as input:
    lines = input.read().splitlines()
    matrix = [list(s) for s in lines]

    balls_set = get_positions(matrix, 'O')
    walls_set = get_positions(matrix, '#')

    height = len(matrix)
    width = len(matrix[0])

    cycle_count = 0
    set_to_count = {}
    count_to_set = {}

    while frozenset(balls_set) not in set_to_count:
        set_to_count[frozenset(balls_set)] = cycle_count
        count_to_set[cycle_count] = frozenset(balls_set)
        balls_set = cycle(balls_set)
        cycle_count += 1

    loop_start = set_to_count[frozenset(balls_set)]
    loop_end = cycle_count
    loop_size = loop_end - loop_start
    goal = loop_start + (1000000000 - loop_start) % loop_size

    print(goal)
    print(sum(height - y for (_, y) in count_to_set[goal]))
