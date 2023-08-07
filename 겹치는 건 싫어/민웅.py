# 20922_겹치는 건 싫어_Hate-Overlap
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
sequence = list(map(int, input().split()))

i, j = 0, 0

num = {}
length = 0
ans = 0
while i<=j and j < N:
    if sequence[j] not in num.keys():
        num[sequence[j]] = 1
        j += 1
        length += 1
    else:
        if num[sequence[j]] >= K:
            num[sequence[i]] -= 1
            i += 1
            length -= 1
        else:
            num[sequence[j]] += 1
            j += 1
            length += 1
    if length > ans:
        ans = length

print(ans)
