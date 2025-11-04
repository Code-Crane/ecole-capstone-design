import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()
result = []

for i in range(n):
    while dq and dq[-1][0] > arr[i]:
        dq.pop()
    dq.append((arr[i], i))
    
    if dq[0][1] <= i - l:
        dq.popleft()

    result.append(dq[0][0])

print(*result)