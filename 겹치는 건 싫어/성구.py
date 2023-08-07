# 20922 겹치는 건 싫어
import sys
input = sys.stdin.readline
#input
N, K = map(int, input().split())
arr = list(map(int, input().split()))
# define
i, j = 0, 0
check = [0] * 100001
maxCount = -1

# logic
while j < N:
    # 작을 때는 상관없음, 카운트
    if check[arr[j]] < K:
        check[arr[j]] += 1
        j += 1
    else: # 크거나 같으면 왼쪽 포인터 증가로 길이 줄어듦
        check[arr[i]] -= 1
        i += 1
    # max 저장
    maxCount = max(maxCount, j - i)

print(maxCount)

"""
import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

i = j = 0
check = defaultdict(int)
maxLen = -1
while j < N:
    if arr[j] in arr[i:j]:
        check[arr[j]] += 1
        if check[arr[j]] >= K:
            i = arr[i : j + 1].index(arr[j]) + 1
            check[arr[j]] -= 1
            if N - i <= maxLen:
                break
    maxLen = max(maxLen, j - i + 1)
    j += 1
else:
    maxLen = max(maxLen, j - i + 1)

print(maxLen) if maxLen != -1 else print(N)
"""
