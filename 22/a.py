# https://www.reddit.com/r/adventofcode/comments/18o7014/comment/kefhah0/

from collections import defaultdict

brick = []
for line in open("input.txt").read().split("\n"):
    a,b = line.split("~")
    a = list(map(int, a.split(",")))
    b = list(map(int, b.split(",")))
    brick.append((a,b))

n = len(brick)

brick.sort(key=lambda x: x[0][2])

highest = defaultdict(lambda:(0,-1))
bad = set()
graph = [[] for i in range(n)]
for idx,b in enumerate(brick):
    mxh = -1
    support_set = set()
    for x in range(b[0][0], b[1][0]+1):
        for y in range(b[0][1], b[1][1]+1):
            if highest[x,y][0] + 1 > mxh:
                mxh = highest[x,y][0] + 1
                support_set = {highest[x,y][1]}
            elif highest[x,y][0] + 1 == mxh:
                support_set.add(highest[x,y][1])
    
    for x in support_set:
        if x != -1:
            graph[x].append(idx)

    if len(support_set) == 1:
        bad.add(support_set.pop())
    
    fall = b[0][2] - mxh
    if fall > 0:
        b[0][2] -= fall
        b[1][2] -= fall

    for x in range(b[0][0], b[1][0]+1):
        for y in range(b[0][1], b[1][1]+1):
            highest[x,y] = (b[1][2], idx)

print(len(brick)-len(bad)+1)
