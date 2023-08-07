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