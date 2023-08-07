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
