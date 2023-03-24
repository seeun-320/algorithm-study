import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([1,0,0,0])
    visited[0][0][0] = 1
    while q:
        d, k, y, x = q.popleft()
        if y == N-1 and x == M-1:
            return d
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0 and not visited[k][ny][nx]:
                    visited[k][ny][nx] = 1
                    q.append([d+1, k, ny, nx])
                elif graph[ny][nx] == 1 and k < K and not visited[k+1][ny][nx]:
                    if d%2 == 1: # 낮
                        visited[k+1][ny][nx] = 1
                        q.append([d+1, k+1, ny, nx])
                    else: # 밤
                        q.append([d+1, k, y, x])
    return -1

dx = [1,0,-1,0]; dy = [0,1,0,-1]
N, M, K = map(int, input().split())
graph = [ list(map(int, input().rstrip())) for _ in range(N) ]
visited = [ [ [0]*M for _ in range(N) ] for _ in range(11) ]
print(bfs())