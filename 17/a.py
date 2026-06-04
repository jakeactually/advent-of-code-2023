import heapq

def solve():
    with open('input.txt') as f:
        grid = [[int(char) for char in line] for line in f.read().splitlines() if line]
    
    height = len(grid)
    width = len(grid[0])
    
    # Priority queue stores: (heat_loss, r, c, dr, dc, consecutive_steps)
    queue = []
    if width > 1:
        heapq.heappush(queue, (grid[0][1], 0, 1, 0, 1, 1))
    if height > 1:
        heapq.heappush(queue, (grid[1][0], 1, 0, 1, 0, 1))
        
    visited = set()
    
    while queue:
        heat_loss, r, c, dr, dc, consecutive_steps = heapq.heappop(queue)
        
        if r == height - 1 and c == width - 1:
            return heat_loss
            
        state = (r, c, dr, dc, consecutive_steps)
        if state in visited:
            continue
        visited.add(state)
        
        # 1. Continue in the same direction if consecutive_steps < 3
        if consecutive_steps < 3:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width:
                heapq.heappush(queue, (heat_loss + grid[nr][nc], nr, nc, dr, dc, consecutive_steps + 1))
                
        # 2. Turn 90 degrees (left or right)
        for ndr, ndc in [(-dc, dr), (dc, -dr)]:
            nr, nc = r + ndr, c + ndc
            if 0 <= nr < height and 0 <= nc < width:
                heapq.heappush(queue, (heat_loss + grid[nr][nc], nr, nc, ndr, ndc, 1))

if __name__ == '__main__':
    result = solve()
    print(result)