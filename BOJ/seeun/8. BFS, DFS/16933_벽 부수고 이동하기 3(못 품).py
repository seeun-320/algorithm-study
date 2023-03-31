from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m, k = map(int, input().split())
MAX = float('inf')

board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[MAX]*(k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][k] = 0
q = deque([(0, 0, 1, k)])
result = MAX

while q :
    x, y, t, left = q.popleft()
    if (x, y) == (m-1, n-1) :
            result = min(result, t)
            continue

    daytime = t % 2
    for k in range(4) :
            ax, ay = x + dx[k], y + dy[k]
            if -1 < ax < m and -1 < ay < n :
                if board[ay][ax] == 0 and visited[ay][ax][left] > t:
                    visited[ay][ax][left] = t
                    q.append((ax, ay, t+1, left))
                if board[ay][ax] == 1 and left and visited[ay][ax][left-1] > t :
                    if daytime : 
                        visited[ay][ax][left-1] = t
                        q.append((ax, ay, t+1, left-1))
                    else :
                        q.append((x, y, t+1, left))
    

print(result if result < MAX else -1)
