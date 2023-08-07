# 2179_비슷한단어_similar-word
# 26% 까지 맞음
import sys
input = sys.stdin.readline


N = int(input())

words = []

for i in range(N):
    words.append([input().strip(), i])

words.sort(key=lambda x:x[0])
temp = [words[0], words[1]]
ans = 0

for i in range(1, N):
    l1, l2 = len(words[i-1][0]), len(words[i][0])
    r = min(l1, l2)
    idx = 0
    while idx < r:
        if words[i-1][0][idx] == words[i][0][idx]:
            idx += 1
        else:
            break
    if idx > ans:
        temp = [words[i-1], words[i]]
        ans = idx
    elif idx == ans:  # idx와 ans가 같은 경우를 추가
        sub = [words[i - 1], words[i], temp[0], temp[1]]
        sub.sort(key=lambda x: x[1])
        temp = [sub[0], sub[1]]

print(temp[0][0])
print(temp[1][0])