import sys
input = sys.stdin.readline  # 빠른 입력(중요)

n = int(input())
target = []
for _ in range(n):
    target.append(int(input()))

stack = []
ops = []
next_num = 1  # 다음에 push할 숫자(1..n)

for t in target:
    # t가 스택 top에 올라올 때까지 push
    while next_num <= t:
        stack.append(next_num)
        ops.append('+')
        next_num += 1

    # 이제 top이 t면 pop, 아니면 불가능
    if stack and stack[-1] == t:
        stack.pop()
        ops.append('-')
    else:
        print("NO")
        sys.exit(0)  # 즉시 종료! (중요)

# 모두 처리됐으면 연산 기호 출력
print('\n'.join(ops))
#gpt 딸깍