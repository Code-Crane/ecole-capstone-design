import sys
input = sys.stdin.readline

n = int(input().strip())

arr = []
while len(arr) < n:
    line = input().strip()
    if not line:
        continue
    arr.extend(map(int, line.split()))
arr = arr[:n]

arr.sort()
ans = 0

for i in range(n):
    target = arr[i]
    left, right = 0, n - 1
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        s = arr[left] + arr[right]
        if s == target:
            ans += 1
            break
        elif s < target:
            left += 1
        else:
            right -= 1

print(ans)

# gpt 딸깍
