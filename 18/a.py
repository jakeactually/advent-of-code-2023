direction_to_delta = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}

with open('input.txt') as input:
    steps = [line.split() for line in input.read().splitlines()]
    points = set()
    current = (0, 0)

    for (dir, size, _) in steps:
        (ox, oy) = direction_to_delta[dir]

        for j in range(int(size)):
            points.add(current)
            current = (current[0] + ox, current[1] + oy)

    start_x = min(x for (x, _) in points) - 1
    start_y = min(y for (_, y) in points) - 1
    end_x = max(x for (x, _) in points) + 1
    end_y = max(y for (_, y) in points) + 1
    
    queue = [(start_x, start_y)]
    visited = set(queue)

    while queue:
        current = queue.pop(0)

        for (ox, oy) in direction_to_delta.values():
            next = (current[0] + ox, current[1] + oy)

            if next not in points and start_x <= next[0] <= end_x and start_y <= next[1] <= end_y:
                if next not in visited:
                    queue.append(next)            
                visited.add(next)

    width = end_x - start_x
    height = end_y - start_y
    
    print(height * width - (len(visited) - width - height - 1))
