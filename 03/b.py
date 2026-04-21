neighbors_offsets = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1)
]

def is_coord_in_limits(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

with open('input.txt') as input:
    matrix = [list(line.strip()) for line in input]
    height = len(matrix)
    gears_dict = {}
    gears_buffer = []
    buffer = ''

    for y in range(height):
        width = len(matrix[y])

        for x in range(width):
            chr = matrix[y][x]

            if chr.isdigit():
                neighbors = [
                    (y + dy, x + dx)
                    for dx, dy in neighbors_offsets
                    if is_coord_in_limits(x + dx, y + dy, width, height)
                ]

                for ny, nx in neighbors:
                    if matrix[ny][nx] == '*':
                        gears_buffer.append((nx, ny))

                buffer += chr
            
            if not chr.isdigit():
                for gear in gears_buffer:
                    if gear not in gears_dict:
                        gears_dict[gear] = set()
                    
                    gears_dict[gear].add(int(buffer))
                
                buffer = ''
                gears_buffer = []
    
    total = 0

    for gear, numbers in gears_dict.items():
        if len(numbers) == 2:
            total += numbers.pop() * numbers.pop()

    print(total)
