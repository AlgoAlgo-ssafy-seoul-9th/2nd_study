# 2nd_study

[2주차] 코딩테스트 준비 2주차
<br/>

[프로그래머스 두 원 사이의 정수](https://school.programmers.co.kr/learn/courses/30/lessons/152996)
[프로그래머스 시소 짝궁](https://school.programmers.co.kr/learn/challenges?order=recent)

[백준 문제집 바로가기](https://www.acmicpc.net/workbook/view/16423)

<br/><br/>

# [프로그래머스] 두 원 사이의 정수쌍

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./두%20원%20사이의%정수쌍/성구.py)

```py
```

## [민웅](./두%20원%20사이의%정수쌍/민웅.py)

```py
import math

def solution(r1, r2):
    ans = 0
    for i in range(0, r1):
        ans += math.floor(math.sqrt(r2**2 - i**2)) - math.floor(math.sqrt(r1**2 - i**2 - 1))
    for i in range(r1, r2):
        ans += math.floor(math.sqrt(r2**2 - i**2))
    return 4 * ans

```

## [병국](./두%20원%20사이의%정수쌍/병국.py)

```py
```

## [상미](./두%20원%20사이의%정수쌍/상미.py)

```py
```

</div>
</details>

<br/><br/><br/>

# [프로그래머스] 시소 짝궁

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./시소%20짝궁/성구.py)

```py
```

## [민웅](./시소%20짝궁/민웅.py)

```py
def solution(weights):
    answer = 0
    num = {}
    weights.sort(reverse=True)
    for v in weights:
        if v in num.keys():
            answer += num[v]
            num[v] += 1
        else:
            num[v] = 1
        if v*3/2 in num.keys():
            answer += num[v*3/2]
        if v*4/3 in num.keys():
            answer += num[v*4/3]
        if v*2 in num.keys():
            answer += num[v*2]

    return answer
```

## [병국](./시소%20짝궁/병국.py)

```py
```

## [상미](./시소%20짝궁/상미.py)

```py
```

</div>
</details>

<br/><br/><br/>

# [백준] 영단어 암기는 괴로워

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./비슷한%20단어/성구.py)

```py
```

## [민웅](./비슷한%20단어/민웅.py)

```py
```

## [병국](./비슷한%20단어/병국.py)

```py

```

## [상미](./비슷한%20단어/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [백준] 1,2,3 더하기 4

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./비슷한%20단어/성구.py)

```py
```

## [민웅](./비슷한%20단어/민웅.py)

```py
```

## [병국](./비슷한%20단어/병국.py)

```py

```

## [상미](./비슷한%20단어/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [백준] 파티

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./비슷한%20단어/성구.py)

```py
```

## [민웅](./비슷한%20단어/민웅.py)

```py
```

## [병국](./비슷한%20단어/병국.py)

```py

```

## [상미](./비슷한%20단어/상미.py)

```py

```

</div>
</details>