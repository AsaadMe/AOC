from collections import deque

with open('2022/input.txt', 'r') as file:
    board = [list(a.strip()) for a in file]

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 'S':
            start = (i,j)
        elif board[i][j] == 'E':
            end = (i,j)

board[start[0]][start[1]] = 'a'
board[end[0]][end[1]] = 'z'

def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [[0]*len(a) for a in board]
    dist = [[0]*len(a) for a in board]
    visited[start[0]][start[1]] = 1

    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    while q:
        cur_addr = q.popleft()
        adjs = []
        for dir in dirs:
            adj = (cur_addr[0]+dir[0], cur_addr[1]+dir[1])
            if adj[0] in range(len(board)) and adj[1] in range(len(board[0])):
                adjs.append(adj)
                
        for adj in adjs:
            if ord(board[adj[0]][adj[1]]) - ord(board[cur_addr[0]][cur_addr[1]]) <= 1:
                if not visited[adj[0]][adj[1]]:
                    visited[adj[0]][adj[1]] = 1
                    dist[adj[0]][adj[1]] = dist[cur_addr[0]][cur_addr[1]] + 1
                    q.append(adj)
                
                if cur_addr == end:
                    return dist[end[0]][end[1]]
            
print('Part1:', bfs(start, end))

all_steps = []
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'a':
            if steps:= bfs((i,j), end):
                all_steps.append(steps)
            
print('Part2:', min(all_steps))