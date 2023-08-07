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