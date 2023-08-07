# 1st_study

[1주차] 코딩테스트 준비 1주차
<br/>

[프로그래머스 python 문제 바로가기](https://school.programmers.co.kr/learn/challenges?order=recent)

[백준 문제집 바로가기](https://www.acmicpc.net/workbook/view/16346)

<br/><br/>

# [백준] 어두운 굴다리

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./어두운%20굴다리/성구.py)

```py
# 17266 어두운 굴다리
import sys
import math
input = sys.stdin.readline
# input
N = int(input())
M = int(input())
x = list(map(int, input().split()))
# define
distance = [x[0]]
# logic
# 각 가로등 사이의 거리, 양쪽 사이드와의 거리 중 가장 긴거 찾기
# 각 가로등 사이의 거리는 1/2 값으로 정의
for i in range(M-1):
    distance.append((x[i+1]-x[i])/2)
distance.append(N - x[-1])
# 소수점 자리를 고려하여 올림 max.ceil
print(math.ceil(max(distance)))
```

## [민웅](./어두운%20굴다리/민웅.py)

```py
# 17266_어두운 굴다리
import sys
import math
input = sys.stdin.readline

N = int(input())
M = int(input())

location = list(map(int, input().split()))

case1 = location[0]
case2 = N-location[-1]
case3 = 0

for i in range(M-1):
    temp = math.ceil((location[i+1]-location[i])/2)
    # print(temp)
    if temp > case3:
        case3 = temp

ans = max(case1,case2,case3)

print(ans)
```

## [병국](./어두운%20굴다리/병국.py)

```py
n = int(input())
m = int(input())
arr = list(map(int,input().split()))

answer1 = 0

# n = 1 일때,, 시작점 잡아주는 느낌,,
if len(arr) == 1:
    answer1 = max(arr[0] - 0, n - arr[0])
# n > 1 일때
else:
    for i in range(len(arr)):
        # 시작점
        if i == 0:
            answer = arr[i]-0
        # 끝점
        elif i == len(arr)-1:
            answer = n-arr[i]
        # 중간지점(중요)
        else:
            check = (arr[i]-arr[i-1])
            if check%2:
                answer = check // 2 +1
            else:
                answer = check // 2
        answer1 = max(answer,answer1)
print(answer1)


```

## [상미](./어두운%20굴다리/상미.py)

```py
# 17266_ 어두운 굴다리

n = int(input())  # 굴다리의 길이
m = int(input())  # 가로등의 개수
light = list(map(int, input().split())) # 가로등의 위치

ans = 0
for i in range(1, m):
    ans = max(ans, light[i] - light[i-1])

# 가장 긴 사이거리, 첫 가로등까지 거리, 마지막 가로등까지 거리 
print(max((ans + 1)//2, light[0] - 0, n - light[-1]))

# 처음엔 모든 가로등 위치에서 가로등의 높이를 올려가는걸 시도했으나 시간 초과로 두번째로 가로등 간의 거리//2 를 시도해봄

```

</div>
</details>

<br/><br/><br/>

# [백준] 겹치는 건 싫어

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./겹치는%20건%20싫어/성구.py)

```py
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

```

## [민웅](./겹치는%20건%20싫어/민웅.py)

```py
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
```

## [병국](./겹치는%20건%20싫어/병국.py)

```py

# 하나씩 넣을때마다 갯수 체크할까,,
# n이 총 개수 , k가 허용가능한 개수
# 이게아니었고,, 시작점이 중요한거,, 그 시작점부터 가장 큰 부분수열,,구하는거

# cnt = 0
# max_cnt = 0
# answer_dict = {}
# for i in range(n):
#     if arr[i] in answer_dict:
#         if answer_dict[arr[i]]+1 > k:
#             break
#         else:
#             answer_dict[arr[i]] += 1
#             cnt += 1
#     else:
#         answer_dict[arr[i]] = 1
#         cnt += 1
# max_cnt = (max_cnt,cnt)

n, k = map(int,input().split())
arr = list(map(int,input().split()))

# 투포인터로 풀어볼게요,,
left,right = 0,0 # 처음엔 0부터 시작합시다..
counter = [0]*(max(arr)+1) # 항목 개수세어줄 리스트
answer = 0 # 답

while right < n: # 배열 끝까지 갈때까지할건데,,
    if counter[arr[right]]<k: # k보다 작다면
        counter[arr[right]] += 1
        right += 1
    else: # k보다커져버렸다면,, 이제 left를 한칸땡겨요
        counter[arr[left]] -= 1 # 이건빼줘야겠져
        left += 1
    answer = max(answer, right-left) #이게 답
print(answer)

```

## [상미](./겹치는%20건%20싫어/상미.py)

```py
N, K = map(int, input().split())
nums = list(map(int, input().split()))

start = end = 0
arr = [0] * 200001  # 숫자 개수 확인용 배열
ans = 0
cnt = 0     

while end < N:
    if arr[nums[end]] < K:
        arr[nums[end]] += 1
        cnt += 1
        end += 1
    else:               # K개 넘어가면 중단
        ans = max(ans, cnt)     # 최대 cnt로 답 갱신
        cnt -= 1        # 앞에 꺼 하나 빼기
        arr[nums[start]] -= 1
        start += 1

ans = max(ans, cnt)     # 중단한 지점과 마지막 지점 비교 -> 이거 안 해줘서 틀림
print(ans)
```

</div>
</details>

<br/><br/><br/>

# [백준] 비슷한 단어

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./비슷한%20단어/성구.py)

```py
# 2179 비슷한 단어
import sys
input = sys.stdin.readline
# input
N = int(input())
# define
words = []
maxIndex = [0, 0]
maxValue = 0
# logic
for k in range(N):
    # 입력과 동시에 처리
    word = input().strip()
    for s in range(len(words)):
        for i in range(min(len(word), len(words[s]))):
            # 다를때만 체크
            if word[i] != words[s][i]:
                # 작을 때와 같을 때 구분하여 체크
                if maxValue < i:
                    maxValue = i
                    maxIndex = [s, k]
                elif maxValue == i:
                    if maxIndex[0] > s:
                        maxValue = i
                        maxIndex = [s, k]
                break
        else:
            # 다 돌고 나왔을 때 경우의 수 체크, 같은 단어는 빼기
            if word != words[s]:
                # 길이가 작을 때와 같을 때 나눠서 체크
                if maxValue < min(len(word), len(words[s])):
                    maxValue = min(len(word), len(words[s]))
                    maxIndex = [s, k]
                elif maxValue == min(len(word), len(words[s])):
                    if maxIndex[0] > s:
                        maxValue = min(len(word), len(words[s]))
                        maxIndex = [s, k]

    words.append(word)
print(words[maxIndex[0]], words[maxIndex[1]], sep="\n")

```

## [민웅](./비슷한%20단어/민웅.py)

```py
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

# 2179_비슷한단어_similar-word
# 67%까지 맞음
# 길이 같은데 접두사 다른경우 추가
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
        temp.sort(key=lambda x: x[1])
        ans = idx
    elif idx == ans:  # idx와 ans가 같은 경우를 추가
        if temp[0][0][:ans] == words[i-1][0][:ans]:
            sub = [words[i-1], words[i], temp[0], temp[1]]
            sub.sort(key=lambda x: x[1])
            if sub[0] == sub[1]:
                temp = [sub[0], sub[2]]
            else:
                temp = [sub[0], sub[1]]
        else:
            sub1 = [words[i-1], words[i]]
            sub1.sort(key=lambda x: x[1])
            if sub1[0][1] < temp[0][1]:
                temp = sub1
            else:
                continue
temp.sort(key=lambda x: x[1])
print(temp[0][0])
print(temp[1][0])
```

## [병국](./비슷한%20단어/병국.py)

```py

```

## [상미](./비슷한%20단어/상미.py)

```py

```

</div>
</details>
