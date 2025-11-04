import sys
input = sys.stdin.readline

n = int(input())          # 숫자의 개수
nums = input().strip()    # 붙어서 들어오는 숫자 문자열

ans = sum(map(int, nums)) # 각 자리수를 int로 변환해 합산
print(ans)

# gpt 딸깍